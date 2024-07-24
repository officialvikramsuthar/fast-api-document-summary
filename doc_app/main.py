
from typing import List
from uuid import uuid4

import aiofiles
from fastapi import FastAPI, Depends, HTTPException, UploadFile, File

from doc_app.auth import get_current_user
from doc_app.crud import add_file, get_file, list_files
from doc_app.dependencies import get_db
from doc_app.utils import extract_text_from_file, get_summary

app = FastAPI()


@app.post("/v1/files", response_model=str)
async def upload_file(
    file: UploadFile = File(...),
    db = Depends(get_db),
    current_user: str = Depends(get_current_user)
):
    if file.content_type not in ["application/vnd.openxmlformats-officedocument.wordprocessingml.document", "application/vnd.openxmlformats-officedocument.presentationml.presentation", "application/pdf"]:
        raise HTTPException(status_code=400, detail="Invalid file type")
    
    file_id = str(uuid4())
    file_path = f"storage/{file_id}_{file.filename}"

    async with aiofiles.open(file_path, 'wb') as out_file:
        content = await file.read()
        await out_file.write(content)
    text = extract_text_from_file(file_path, file.content_type)
    summary = await get_summary(text)

    file_metadata = {
        "file_id": file_id,
        "file_name": file.filename,
        "file_summary": summary
    }

    await add_file(db, file_metadata)
    return file_id


@app.get("/v1/files", response_model=List[dict])
async def list_uploaded_files(
    db = Depends(get_db),
    current_user: str = Depends(get_current_user)
):
    return await list_files(db)


@app.get("/v1/files/{file_id}", response_model=str)
async def get_file_summary(
    file_id: str,
    db = Depends(get_db),
    current_user: str = Depends(get_current_user)
):
    file = await get_file(db, file_id)
    if not file:
        raise HTTPException(status_code=404, detail="File not found")
    return file["file_summary"]

