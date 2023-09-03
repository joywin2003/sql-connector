import datetime
from typing import Optional,List
from pydantic import BaseModel

class Admins(BaseException):
    adminID:int
    email :str
    password: str

class User(BaseException):
    userID: int
    username: str
    password: str
    email: str
    
class Books(BaseException):
    bookID: int
    title :str
    author:str
    genre:str
    price:float
    
class Orders(BaseException):
    orderID:int
    bookID:int
    orderdate:datetime
    orderamount:int
    userID:int