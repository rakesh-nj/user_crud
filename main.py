from typing import Union
from fastapi import FastAPI,Query,HTTPException
from models import User,UserUpdate
from typing import List,Optional


app = FastAPI(title="user management api")

# i am using dict for in-memory storage
db = {}

@app.post("/users/",status_code=201)
async def create_user(user : User):
    if user.id in db:
        raise HTTPException(status_code = 400, detail="User with this id already exists")
    db[user.id] = user
    return {"Message": "user created successfully"}


@app.get("/users/search", response_model=List[User])
async def search_users(name: str = Query(..., description="Name to search for")):
    result = [user for user in db.values() if name.lower() in user.name.lower()]
    return result


# sample 
@app.get("/users/{user_id}", response_model=User)
async def get_user(user_id: int):
    if user_id not in db:
        raise HTTPException(status_code=404, detail="User not found")
    return db[user_id]


@app.put("/update/{user_id}")
async def update_user(user_id: int, user_update: UserUpdate):
    if user_id not in db:
        raise HTTPException(status_code = 404,detail= "user not found")

    current_user = db[user_id]
    updated_user = User(
            id = current_user.id,
            name = user_update.name,
            phone_num = user_update.phone_num,
            address = user_update.address
            )
    db[user_id] = updated_user
    return {"message":"User updated successfully"}

@app.delete("/delete/{user_id}")
async def delete_user(user_id: int):
    if user_id not in db:
        raise HTTPException(status_code=404, detail="User not found")
    del db[user_id]
    return {"message": "User deleted successfully"}

@app.get('/')
async def root():
    return {"message":"Welcome to User management API :)"}

