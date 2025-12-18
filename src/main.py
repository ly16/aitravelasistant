from fastapi import FastAPI, UploadFile
from contextlib import asynccontextmanager
from pydantic import BaseModel
from src.ingest import ingest_pdf

#  AiTravelAssistant % uvicorn src.main:app --reload
@asynccontextmanager
async def lifespan(app: FastAPI):
    # Initialize resources here (e.g., database connections, models)
    # Initialize Qdrant database
    print("Initializing Qdrant database...")
    print("Database initialization complete.")
    yield


app = FastAPI(lifespan=lifespan)

# query request validator
class QueryRequest(BaseModel):
    query: str

@app.post("/ask")
async def ask_question(req: QueryRequest):
    return {"response": "resp"}


@app.post("/upload")
async def upload_file(file: UploadFile = None):
    if not file:
        return {"message": "No file uploaded"}

    if not file.filename.endswith('.pdf'):
        return {"message": "Please upload a PDF file"}

    try:
        await ingest_pdf(file)
        return {"message": "File processed successfully"}
    except Exception as e:
        return {"message": f"Error processing file: {str(e)}"}
