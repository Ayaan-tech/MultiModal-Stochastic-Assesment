import os
from pydantic_settings import BaseSettings
import os
class Settings(BaseSettings):
    BEARER_TOKEN: str 
    PINECONE_API_KEY: str
    PINECONE_INDEX_NAME:str
    AZURE_ENDPOINT: str
    AZURE_KEY: str
    AZURE_MODEL: str = "openai/gpt-4.1"
    HF_TOKEN:str
    GROQ_API_KEY:str
    DATABASE_URL:str

    class Config:
        env_file = ".env"
       
settings = Settings()
