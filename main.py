from fastapi import FastAPI
import os

app = FastAPI()

@app.get("/")
def root():
    return {
        "message": "python_test_2 funcionando 🚀",
        "env": os.getenv("APP_ENV"),
        "port": os.getenv("PORT"),
        "base_path": os.getenv("BASE_PATH")
    }