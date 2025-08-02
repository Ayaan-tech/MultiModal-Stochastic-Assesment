import pinecone
from pinecone import Pinecone , ServerlessSpec
from langchain_community.vectorstores import PineconeHybridSearchRetriever
from langchain_huggingface import HuggingFaceEmbeddings
from config import settings
from pinecone_text.sparse import BM25Encoder

Pinecone.init(api_key=settings.PINECONE_API_KEY)
if not Pinecone.has_index(settings.PINECONE_INDEX_NAME):
    Pinecone.create_index(
        settings.PINECONE_INDEX_NAME,
        dimension=384, 
        metric="cosine",
        sparse_fields=["text"],
        serverless_spec=ServerlessSpec(
            cloud="aws", region="us-east-1"
        )
    )
index = Pinecone.Index(settings.PINECONE_INDEX_NAME)

embeddings = HuggingFaceEmbeddings(api_key=settings.HF_TOKEN,model_name="all-MiniLM-L6-v2")

bm25_encoder = BM25Encoder()

retriever = PineconeHybridSearchRetriever(
    embeddings=embeddings,
    sparse_encoder=bm25_encoder,
    index=index
)