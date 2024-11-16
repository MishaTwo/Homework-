from fastapi import FastAPI

app = FastAPI()

user_list = []

@app.get('/users')
async def all_user():
    with open('info.txt', 'r') as file:
        lines = file.readlines()
        for line in lines:
            strip_line = line.split()
            user = {
                "id": int(strip_line[0]),
                "name": strip_line[1],
                "age": int(strip_line[2]),
            }
            user_list.append(user)
    return user_list

@app.post('/user')
async def create_user(id: int, name:str, age:int):
    with open('info.txt', 'a') as file:
        file.write(f'{id} {name} {age}\n')
    user = {
        "id":id,
        "name": name,
        "age":age,
    }
    user_list.append(user)

@app.get('/users/{id}')
async def get_user(id: int):
    for user in user_list:
        if user["id"] == id:
            return user
        else:
            return {"message": "Такого користувача нема"}
