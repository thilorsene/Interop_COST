from pydantic import BaseModel
from typing import Optional,List
from fastapi import Form

class Order(BaseModel):
    id : str
    date : str
    client : str
    articles: dict

class OrderFrom(BaseModel):
    id: int = Form(...)
    qte: int = Form(...)
