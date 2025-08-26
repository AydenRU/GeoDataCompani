from fastapi import APIRouter
from fastapi import Request, Response



authorization = APIRouter(prefix='/login', tags=['authorization'])

@authorization.post('/login')
async def check_users():
    pass