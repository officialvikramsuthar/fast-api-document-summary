# FastAPI File Upload and Summary Project

This project is a FastAPI application that allows users to upload `.docx`, `.pptx`, and `.pdf` files. The uploaded files are stored on the server, and a summary of each file is generated and stored in a MongoDB database. The application provides three endpoints: one for uploading files, one for listing all uploaded files, and one for retrieving the summary of a specific file.

## Features

- Upload `.docx`, `.pptx`, and `.pdf` files.
- Store files on the server.
- Generate a 3-line summary of each file using the Predibase API.
- Store file metadata and summaries in a MongoDB database.
- List all uploaded files.
- Retrieve the summary of a specific file.

## Requirements

- Python 3.8+
- MongoDB
- Predibase API Key

## Installation

### 1. Clone the repository


git clone https://github.com/yourusername/fast-api-document-summary.git
cd fastapi-file-upload-summary


python -m venv venv
source venv/bin/activate

pip install -r requirements.txt

Create the storage folder

mkdir storage

Run the application
uvicorn doc_app.main:app --reload
