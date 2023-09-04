from fastapi import FastAPI,HTTPException
from pydantic import BaseModel
from typing import List
import db_helper
from datetime import datetime
from fastapi.middleware.cors import CORSMiddleware
import json
from Modal import Orders, User, Books, Admins

app  = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins = ["*"],
    allow_credentials = True,
    allow_methods = ["*"],
    allow_headers = ["*"],
)

orders: List[User] = [
    
]

@app.get('./')
async def root():
    return {"message": "Hello World"}



@app.get('/get_books/')
async def get_books():
    books =  db_helper.get_books()
    return {"books":books}

@app.post('/add_order/')
async def add_order(order:Orders):
    order = db_helper.add_order(order)
    return {"order":order}



@app.delete('/remove_order/{order_id}')
async def delete_order(order_id):
    db_helper.remove_order(order_id)
    return {"order_id":order_id}