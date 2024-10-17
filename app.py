from fastapi import FastAPI

app = FastAPI()

user_list = []

@app.get('/users')
async def all_user():
    return user_list

@app.post('/user')
async def create_user(id: int, name:str, age:int):
    user = {
        "id": id,
        "name": name,
        "age": age,
    }
    user_list.append(user)
    return user

@app.get('/users/{id}')
async def get_user(id: int):
    for user in user_list:
        if id == user["id"]:
            return user
        else:
            return "Такого користувача немає!"