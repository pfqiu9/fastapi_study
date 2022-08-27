from email import message
import enum
from fastapi import FastAPI
from enum import Enum
from pydantic import BaseModel
from typing import Union

class Models(str,Enum):
    alexnet="alexnet"
    lenet="lenet"
    resnet="resnet"

class Item(BaseModel):
    name: str
    description: Union[str, None] = None
    price: float
    tax: Union[float, None] = None

app=FastAPI()

@app.get("/model/{model_name}")
async def model(model_name:Models):
    if model_name is Models.alexnet:
        return {"model_name":model_name,"message":"alexnet is good"}
    
    if model_name.value=="lenet":
        return {"model_name":model_name,"message":"lenet is a good model"}
    
    return {"model_name":model_name,"message":"resnet is the best"}

@app.get("/file/{file_path:path}")
async def read_file(file_path:str):
    return {"file_path":file_path}

@app.post("/items/")
async def create_item(item: Item):
    item_dict = item.dict()
    if item.tax:
        price_with_tax = item.price + item.tax
        item_dict.update({"price_with_tax": price_with_tax})
    return item_dict