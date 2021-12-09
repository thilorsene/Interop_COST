from fastapi import FastAPI, UploadFile, File, Form
from fastapi.middleware.cors import CORSMiddleware
from databases import Database

database = Database("sqlite:///aust_db.sqlite")

app = FastAPI()
@app.on_event("startup")
async def database_connect():
    await database.connect()


@app.on_event("shutdown")
async def database_disconnect():
    await database.disconnect()


@app.get("/test")
async def fetch_data():
    query = "SELECT * FROM stock"
    results = await database.fetch_all(query=query)
    return  results