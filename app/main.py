from fastapi import FastAPI


router = FastAPI()


@router.get('/')
async def main():
    return {'Привет': 5 + 10}

