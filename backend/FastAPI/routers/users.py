
from fastapi import APIRouter, HTTPException
from pydantic import BaseModel

router = APIRouter()

# Entidad user
class User(BaseModel):
    id: int
    name: str
    surname: str
    url: str
    age: int

users_list = [User(id=1, name='Elkin', surname='Carreño', url='https://elkin.dev', age=22),
              User(id=2, name='Moure', surname='Brais', url='https://elkin.dev', age=33),
              User(id=3, name='Fabian', surname='Riquelme', url='https://elkin.dev', age=22)]

@router.get('/usersjson')
async def usersjson():
    return [{'name': 'Elkin', 'surname': 'Carreño', 'url': 'https://elkin.dev', 'age': 23},
            {'name': 'Moure', 'surname': 'Brais', 'url': 'https://elkin.dev', 'age': 23},
            {'name': 'Fabian', 'surname': 'Dev', 'url': 'https://elkin.dev', 'age': 23}]

@router.get('/users')
async def users():
    return users_list

# Path
@router.get('/user/{id}')
async def user(id: int):
    return search_user(id)
    
# Query
@router.get('/user/')
async def user(id: int):
    return search_user(id)


@router.post('/user/', response_model=User, status_code=201)
async def user(user: User):
    if type(search_user(user.id)) == User:
        raise HTTPException(status_code=404, detail='El usuario ya existe')
    else:
        users_list.append(user)
        return user


@router.put('/user/')
async def user(user: User):

    found = False

    for index, saved_user in enumerate(users_list):
        if saved_user.id == user.id:
            users_list[index] = user
            found = True

    if not found:
        return {'error': 'No se ha actualizado el usuario'}
    else:
        return user

@router.delete('/user/{id}')
async def user(id: int):

    found = False

    for index, saved_user in enumerate(users_list):
        if saved_user.id == id:
            del users_list[index]
            found = True

    if not found:
        return {'error': 'No se ha eliminado el usuario'}


def search_user(id: int):
    users = filter(lambda user: user.id == id, users_list)
    try:
        return list(users)[0]
    except:
        return {'error': 'No se ha encontrado el usuario'}
    







