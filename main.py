from fastapi import FastAPI
from pydantic import BaseModel
# import db_helper
from datetime import datetime
from fastapi.middleware.cors import CORSMiddleware
from datetime import datetime
import json

app  = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins = ["*"],
    allow_credentials = True,
    allow_methods = ["*"],
    allow_headers = ["*"],
)

@app.get('./')
def root():
    return {"message": "Hello World"}

now = datetime.now()
datestring  = now.strftime("%Y-%m-%d")
