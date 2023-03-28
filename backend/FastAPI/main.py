
from fastapi import FastAPI
from routers import products, users, basic_auth_users, jwt_auth_users, users_db
from fastapi.staticfiles import StaticFiles

app = FastAPI()

# Routers
app.include_router(products.router)
app.include_router(users.router)

app.include_router(basic_auth_users.router)
app.include_router(jwt_auth_users.router)
app.include_router(users_db.router)

# Carpeta Estática
app.mount('/static', StaticFiles(directory='static'), name='static')

@app.get('/')
async def root():
    return '¡Hola FastAPI!'


@app.get('/url')
async def root():
    return {
        'url': 'https://mouredev.com/python'
    }




# Inicia el server: python3 -m uvicorn main:app --reload

# Documentación con Swagger: http://localhost:8000/docs
# Documentación con Redocly: http://localhost:8000/redoc



