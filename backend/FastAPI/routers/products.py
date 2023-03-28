
from fastapi import APIRouter

router = APIRouter(prefix='/products', 
                   tags=['products'],
                   responses={404: {"message": "No ecnontrado"}})

products_list = ['Productos 1', 'Productos 2', 'Productos 3', 'Productos 4', 'Productos 5']

@router.get('/')
async def products():
    return products_list


@router.get('/{id}')
async def products(id: int):
    return products_list[id]

