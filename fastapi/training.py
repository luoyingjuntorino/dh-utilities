from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from datetime import datetime
import json

class Request(BaseModel):
    username:str
    password:str

class Item(BaseModel):
    info:str

class User(BaseModel):
    id:int

app = FastAPI()

# db = {
#       "IP":"127.0.0.1",
#       "PORT":"8000",
#       "STATE":"IT",
#       "ORG":"POLITO",
#       "USERS":["user01", "user02", "user03"]
#       }

@app.get("/")
async def home():
    return {"Hello": "World"}

@app.post("/login")
async def login(req:Request):
    if req.username == "admin" and req.password == "test":
        return {"message":"success"}
    else:
        return {"message":"faild"}
    
@app.get("/USERS/{id}")
async def users(id:int):
    with open("setting.json") as f:
        db = (json.load(f))
    if id < len(db["USERS"]):
        return db["USERS"][id]
    else:
        raise HTTPException(status_code=404, detail="Item not found")

@app.put("/update/{data}")
async def update(data:str, updated_item: Item):
    with open("setting.json") as f:
        db = (json.load(f))
    if data in db:
        db[data] = updated_item.info
        current_time = datetime.now()
        formatted_time = current_time.strftime("%Y-%m-%d %H:%M")
        db["lastUpdate"] = formatted_time
        with open('setting.json', 'w') as f:
            json.dump(db, f)
        return {f"{data} updated successfully":db}
    else:
        raise HTTPException(status_code=404, detail="Item not found")
    
@app.get("/query/{info}")
async def getInfo(info:str):
    with open("setting.json") as f:
        db = (json.load(f))
    if info in db:
        data = db[info]
        return {f"Query:{info} successfully! {data}"}
    else:
        raise HTTPException(status_code=404, detail=f"Query:{info} not found")
    