from typing import Any, Dict, Optional

from pydantic import BaseModel

from fastapi import FastAPI, HTTPException, Path, Query, status

# Creates a API object
app = FastAPI()


# Inherits from BaseModel
class Item(BaseModel):
    name: str
    price: float
    brand: Optional[str] = None


class UpdateItem(BaseModel):
    name: Optional[str] = None
    price: Optional[float] = None
    brand: Optional[str] = None


"""
    Creates the endpoint
"""


@app.get("/")
def home():
    # Returns when we go to the above root or endpoint "/"
    return {"Data": "Test"}


@app.get("/about")
def about():
    return {"Data": "About"}


inventory: Dict[Any, Any] = {}


@app.get("/get-item/{item_id}")
# http://127.0.0.1:8000/get-item/1
def get_item(
    item_id: int = Path(
        None, description="The ID of the item you want to search", gt=0
    )  # NoQA
):
    return inventory[item_id]


@app.get("/get-by-name/{item_id}")
# http://127.0.0.1:8000/get-by-name/1?name=Milk&test=1
def get_item_by_name(*, item_id: int, name: Optional[str] = None, test: int):
    for id in inventory:
        if inventory[id].name == name:
            return inventory[item_id]
    # return {"Data": "Not Found"}
    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND, detail="Item name not found."
    )


@app.post("/create-item/{item_id}")
def create_item(item_id: int, item: Item):
    if item_id in inventory:
        raise HTTPException(status_code=400, detail="Item ID already exists.")

    # inventory[item_id] = {
    # "name": item.name,
    # "brand": item.brand,
    # "price": item.price}
    inventory[item_id] = item
    # item is directly converted from python object into JSON
    # since it inherits from the BaseModel
    return inventory[item_id]


@app.put("/update-item/{item_id")
def update_item(item_id: int, item: UpdateItem):
    if item_id not in inventory:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Item ID not found."
        )

    if item.name is not None:
        inventory[item_id].name = item.name
    if item.price is not None:
        inventory[item_id].price = item.price
    if item.brand is not None:
        inventory[item_id].brand = item.brand

    return inventory[item_id]


@app.delete("/delete-item")
# ... means required not optional
def delete_item(
    item_id: int = Query(
        ..., description="The ID of the item to delete and >=0"
    )  # NoQA
):
    if item_id not in inventory:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Item ID not found."
        )
    del inventory[item_id]
    return {"Success": "Item deleted!"}
