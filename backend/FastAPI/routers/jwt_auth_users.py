
from fastapi import APIRouter, Depends, HTTPException, status
from pydantic import BaseModel
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from jose import jwt, JWTError
from passlib.context import CryptContext
from datetime import datetime, timedelta

ALGORITHM = "HS256" 
ACCESS_TOKEN_DURATION = 1
SERCRET = "13e478a80821fe7cf32674c7b5593506c324cb1abe0cbb624cddfeec6c8f1018"

router = APIRouter()

oauth2 = OAuth2PasswordBearer(tokenUrl='login')

crypt = CryptContext(schemes=["bcrypt"])


# Entidad user
class User(BaseModel):
    username: str
    full_name: str
    email: str
    disabled: bool

class UserDB(User):
    password: str

users_db = {
    "elkindev": {
        "username": "elkindev",
        "full_name": "Elkin Carreño",
        "email": "correo@correo.com",
        "disabled": False,
        "password": "$2a$12$2RZ.Cz.3nNf6pxcNX59ynuWpNro8nSJy./69rkcdgSjLBtBm9z2bW"
    },
        "elkindev2": {
        "username": "elkindev2",
        "full_name": "Elkin Carreño2",
        "email": "correo2@correo.com",
        "disabled": True,
        "password": "$2a$12$ANowr4oM1kNFr4N8R0yMFuG.XsAZ8Cms.1rfCJ9ZquYMBWTdW2s3e"
    }
}


def search_user_db(username: str):
    if username in users_db:
        return UserDB(**users_db[username])
    
def search_user(username: str):
    if username in users_db:
        return User(**users_db[username])
    
async def auth_user(token: str = Depends(oauth2)):

    exception = HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail='Credenciales de autenticación inválidas', headers={"WWW-Authenticate": "Bearer"})

    try:
        username = jwt.decode(token, SERCRET, algorithms=[ALGORITHM]).get('sub')
        if username is None:
            raise exception
        
    except JWTError:
        raise exception

    return search_user(username)

async def current_user(user: User = Depends(auth_user)):

    if user.disabled:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail='Usuario Inactivo')

    return user



@router.post('/login')
async def login(form: OAuth2PasswordRequestForm = Depends()):
    user_db = users_db.get(form.username)
    if not user_db:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail='EL usuario no es correcto')
    
    user = search_user_db(form.username)

    if not crypt.verify(form.password, user.password):
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail='La contraseña no es correcta')


    access_token = {
        "sub": user.username,
        "exp": datetime.utcnow() + timedelta(minutes=ACCESS_TOKEN_DURATION)
    }

    return {"access_token": jwt.encode(access_token, SERCRET, algorithm=ALGORITHM), "token_type": "bearer"}


@router.get('/users/me')
async def me(user: User = Depends(current_user)):
    return user