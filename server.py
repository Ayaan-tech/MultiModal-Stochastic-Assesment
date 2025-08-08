import os
import tempfile
import requests
import uuid
from fastapi import FastAPI, HTTPException, Depends, Header
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
from schemas import RunRequest, RunResponse
from loader import load_document
from embedder import embed_and_store
from rag_chain import run_rag_chain


TOKEN = os.getenv("TEAM_TOKEN" , "Bearer b7d3cc8816551848e9f232feb64f6b0e318ec8bb2b623a8efb7bb55a055ff1a8")

security = HTTPBearer()
app = FastAPI(title="Context-Aware RAG API", version="1.0.0" )

def check_token(creds: HTTPAuthorizationCredentials = Depends(security)):
    if creds.scheme.lower() != "bearer" or creds.credentials != TOKEN:
        raise HTTPException(status_code=401, detail="Invalid or missing token")
    return creds.credentials

@app.post("/api/v1/hackrx/run", response_model=RunResponse , status_code=200)
async def hackrx_run(
    payload : RunRequest,
    token:str = Depends(check_token)

): 
    tmp_dir = tempfile.gettempdir()
    local_path = os.path.join(tmp_dir, f"{uuid.uuid4()}{os.path.splitext(payload.documents.path)[1]}")
    r = requests.get(str(payload.documents))
    if not r.ok:
        raise HTTPException(status_code=400, detail="Failed to download document")
    with open(local_path, "wb") as f:
        f.write(r.content)

    try:
        text = load_document(local_path)
    except  Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    vector_db = embed_and_store(text, local_path)
    
    answers = []
    session_id  = uuid.uuid4().hex
    for q in payload.questions:
        response = run_rag_chain(q, session_id=session_id, file_path=local_path)
        answers.append(response)
    return RunResponse(answers=answers)
if __name__ == "__main__":
    import uvicorn
    uvicorn.run("server:app", host="0.0.0.0", port=8000, reload=True)