from typing import Union
from fastapi import FastAPI
from pydantic import BaseModel


app = FastAPI()


class Item(BaseModel):
    name: str
    price: int
    is_offer: Union[bool, None] = None


@app.get("/")
async def read_root():
    return {"Hello": "World"}


@app.get("/items/{item_id}")
async def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}


@app.put("/items/{item_id}")
async def update_item(item_id: int, item:Item):
    return {
        "item_id": item_id,
        "item_name": item.name, 
        "item_price": item.price,
        "item_discount": item.is_offer
    }


# Try out the update_item API using the below CURL
"""
curl --location --request PUT 'http://127.0.0.1:8000/items/12345' \
--header 'Content-Type: application/json' \
--data '{
  "name": "star",
  "price": 999,
  "is_offer": true
}'
"""
