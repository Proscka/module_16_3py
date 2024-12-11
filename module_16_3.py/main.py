from fastapi import FastAPI,Path
from typing import Annotated
from pyexpat.errors import messages

app = FastAPI()

users = {'1': 'Имя:Example, возраст:18'}

@app.get('/users')
async def get_all_messages()->dict:
    return users

@app.post('/user/{username}/{age}')
async def create_message (username: Annotated[str,Path(min_length=5, max_length=20, description = 'Enter username',example='Виктория')]
                                                    ,age:int = Path(ge=18, le=100, discription= 'Enter age', example='51'))->dict:
    current_index = str(int(max(users,key=int))+1)
    users[current_index]=username,age
    return (f"Пользователь{current_index} зарегистрирован")

@app.put('/user/{username}/{user_id}/{age}')
async def update_user(user_id:str = Path(min_length=5,max_length=20, description= 'Enter username', example='Виктория'),
                   username : str = Path(ge=18, le=100, discription= 'Enter age', example='51'),
                   age: int =30)-> dict:
    users[user_id] = user_id,username, age
    return (f"The user  {user_id} is opdated")

@app.delete('/user/{user_id}')
async def delite_user(user_id: str)-> str:
    users.pop(user_id)
    return (f"Пользователь{user_id} удалён")
