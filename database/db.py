from fastapi import FastAPI, Depends
from prisma import Prisma
from prisma.models import Document as DocumentModel
from contextlib import asynccontextmanager

import os

db = Prisma()

@asynccontextmanager
async def lifespan(app: FastAPI):
    await db.connect()
    yield
    await db.disconnect()

app = FastAPI(lifespan=lifespan)
@app.post("/documents/")
async def create_document(url:str , prisma:Prisma =Depends()):
    doc = await prisma.document.create(
        data={"url":url}
        
    )
    return {"id": doc.id, "url": doc.url, "uploadedAt": doc.uploadedAt}
