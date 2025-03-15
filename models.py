from pydantic import BaseModel

class User(BaseModel):
    id : int 
    name : str
    phone_num : str
    address : str

class UserUpdate(BaseModel):
    name : str
    phone_num : str
    address : str


