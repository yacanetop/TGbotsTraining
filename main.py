from fastapi import FastAPI
from fastapi.responses import FileResponse
app = FastAPI()

@app.get("/")
def root():
    return FileResponse("public/file1.jpg")
