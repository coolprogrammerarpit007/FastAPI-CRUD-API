from fastapi import FastAPI,Query
from fastapi import HTTPException
from pydantic import BaseModel,Field

import random
from typing import Annotated

app = FastAPI()

items_db = []

# Pydantic  Request Model
class Item(BaseModel):
    name:str = Field(
        min_length = 1,
        max_length = 100,
        description="The Item Name"
    )
    
# Pydantic Response Model

class ItemResponse(BaseModel):
    status:bool
    message:str
    item:str
    
class ItemUpdateResponse(BaseModel):
    message:str
    old_item:str
    new_item:str
    
class ItemDeletedResponse(BaseModel):
    message:str
    deleted_item:str
    items_remaining:int
    
class ItemListResponse(BaseModel):
    original_order: list[str]
    randomized_order:list[str]
    count:int
@app.get("/")

def welcome_home():
    return {"msg":"WELCOME TO THE RANDOMIZER API!"}


@app.get("/random/{max_value}")

def get_random_number(max_value : int):
    return {
        "max":max_value,
        "random_number":random.randint(1,max_value)
    }
    
    
@app.get("/random-between")

def random_number_between(
    min_value: Annotated[int,Query(
        title="Minimum Value",
        description="Minimum Random Value",
        ge = 1,
        le = 1000
    )] = 1,
    max_value:Annotated[int,Query(
        title = "Maximum Value",
        description="Maximum Random Value",
        ge = 1,
        le = 1000
    )] = 99
):
    if min_value > max_value:
        raise HTTPException(status_code=400, detail="Min value can not be greater than Max value")
    
    data = {
        "min-value":min_value,
        "max-value":max_value,
        "random-number":random.randint(min_value,max_value)
    }
    
    return data
    
@app.post("/items",response_model=ItemResponse)
def add_item(item:Item):
        
    if item.name in items_db:
        raise HTTPException(status_code=400,detail="Item already added into list!",status=False)
    
    items_db.append(item.name)
    
    return ItemResponse(status=True,message="Item added successfully!",item=item.name)

@app.get("/items",response_model=ItemListResponse)

def get_randomized_items():
    randomized = items_db.copy()
    random.shuffle(randomized)
    
    return ItemListResponse(
        original_order=items_db,
        randomized_order=randomized,
        count=len(randomized)
        
    )
    
    
@app.put("/items/{updated_name}",response_model=ItemUpdateResponse)

def update_item(updated_name:str,item:Item):
     
    if updated_name not in items_db:
        raise HTTPException(status_code=400,detail="ITEM NOT FOUND!")
    
    if item.name in items_db:
        raise HTTPException(status_code=409,detail="This name item already in the items list!")
    
    index = items_db.index(updated_name)
    items_db[index] = item.name
    
    return ItemUpdateResponse(
        message="Item updated successfully!",
        old_item=updated_name,
        new_item=item.name
    )
    
    
@app.delete("/items/{item}",response_model=ItemDeletedResponse)

def delete_item(item:str):
    if item not in items_db:
        raise HTTPException(status_code=404,detail="Item not found!")
    
    items_db.remove(item)
    
    return ItemDeletedResponse(
        message="Item deleted successfully!",
        deleted_item=item,
        items_remaining=len(items_db)
    )