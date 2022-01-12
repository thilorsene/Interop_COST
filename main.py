from fastapi import FastAPI, UploadFile, File, Form, BackgroundTasks
from fastapi.middleware.cors import CORSMiddleware
from databases import Database
from datetime import datetime
from send import send_command_rbmq
from models import Order, OrderFrom
from fastapi.encoders import jsonable_encoder
import json

database = Database("sqlite:///aust_db.sqlite")

app = FastAPI()



origins = ['*']

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


album = [{'key':1,'title':'All the piano you need','artist':'Mireille Dumas','rating':4.1,'price':12},
{'key':2,'title':'Songs to test by','artist':'Francis Quokka','rating':4.9,'price':14},
{'key':3,'title':'The Greatest Show on Earth','artist':'Jean-Luc Kekes','rating':4.3,'price':16.50},
{'key':4,'title':'Dream is collapsing','artist':'Emy Le Iench','rating':4.6,'price':14.50},
{'key':5,'title':'Furious Ferrieu','artist':'Yanis Bensetti','rating':4.2,'price':12.50},
{'key':6,'title':'Mr. Roquefort','artist':'Océane and the Queens','rating':4.8,'price':14}]


@app.on_event("startup")
async def database_connect():
    await database.connect()

@app.on_event("shutdown")
async def database_disconnect():
    await database.disconnect()


@app.get("/stock")
async def fetch_data():
    query = "SELECT * FROM stock"
    results = await database.fetch_all(query=query)
    return  jsonable_encoder(results)


@app.get("/order")
async def get_orders():
    query = "SELECT * FROM orders"
    results = await database.fetch_all(query=query)
    return  jsonable_encoder(results)


@app.post("/send_order_form")
async def send_order(item:OrderFrom):
    send_command_rbmq(jsonable_encoder(item))
    return item

@app.post("/send_order")
async def send_order(item:Order):
    send_command_rbmq(jsonable_encoder(item))
    return item

@app.get("/bons")
async def get_bon():
    query = "SELECT * FROM bon"
    results = await database.fetch_all(query=query)
    return  jsonable_encoder(results)