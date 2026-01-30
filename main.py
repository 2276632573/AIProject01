from typing import Union
from fastapi import FastAPI, Depends, Response
from sqlmodel import SQLModel, Field, Session
from dotenv import load_dotenv
from config.database import get_session
from entity.User import User
from models.UserModel import UserModel
import os

load_dotenv()



app = FastAPI()

@app.get("/")
def read_root() -> dict[str, str]:
    return {"message": "Hello, World!"}

@app.get("/items/{item_id}")
def read_item(item_id: int, q: Union[str, None] = None) -> dict[str, Union[int, str, None]]:
    return {"item_id": item_id, "q": q}

@app.post("/db")
def testdb(session: Session = Depends(get_session)):
    new_user = User(name="exampleName", type="exampleType")
    session.add(new_user)
    session.flush()
    session.refresh(new_user)
    return {"id": new_user.id, "name": new_user.name, "type": new_user.type}

@app.post("/user/save")
def save_user(userModel: User, session: Session = Depends(get_session)) -> User:
    if not userModel.id:
        # return {"error": "User not found"}
        new_user = User(
            name=userModel.name,
            type=userModel.type
        )
        session.add(new_user)
        # session.flush()
        # session.refresh(new_user)
        return new_user
    else:
        existing_user: User | None = session.get(User, userModel.id)
        if not existing_user:
            return existing_user
        existing_user.name = userModel.name
        existing_user.type = userModel.type
        session.add(existing_user)
        # session.flush()
        # print("Received userModel:", userModel)

        return existing_user
        # return {"id": existing_user.id, "name": existing_user.name, "type": existing_user.type}
    

