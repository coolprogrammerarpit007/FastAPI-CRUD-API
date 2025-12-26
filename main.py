from fastapi import FastAPI,Query
from fastapi import HTTPException

import random
from typing import Annotated

app = FastAPI()

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
    
items_db = []
@app.post("/items")
def add_item(body:dict):
    name = body.get("name")
    
    if not name:
        raise HTTPException(status_code=400,detail="Item name can not be empty")
    
    if name in items_db:
        raise HTTPException(status_code=400,detail="Item already added into list!")
    
    items_db.append(name)
    
    return {"message":"Item added successfully!","item_name":name}

@app.get("/items")

def get_randomized_items():
    randomized = items_db.copy()
    random.shuffle(randomized)
    
    return {
        "oridinal_list":items_db,
        "shuffled_item_list":randomized,
        "count":len(items_db)
    }
    
    
@app.put("/items/{updated_name}")

def update_item(updated_name:str,body:dict):
    new_item_name = body.get("new_item_name")
    
    if not new_item_name:
        raise HTTPException(status_code=400,detail="New item name could not be empty!")
    
    if new_item_name in items_db:
        raise HTTPException(status_code=400,detail="New item name already in the list!")
    
    if updated_name not in items_db:
        raise HTTPException(status_code=404,detail="ITEM NOT FOUND!")
    
    index = items_db.index(updated_name)
    items_db[index] = new_item_name
    
    return {
        "message":"Item updated successfully!",
        "old_item":updated_name,
        "new_name":new_item_name
    }
    
    
@app.delete("/items/{item}")

def delete_item(item:str):
    if item not in items_db:
        raise HTTPException(status_code=404,detail="Item not found!")
    
    items_db.remove(item)
    
    return {
        "message" : "Item removed successfully!",
        "deleted_item":item,
        "remaining_items_count":len(items_db)
    }