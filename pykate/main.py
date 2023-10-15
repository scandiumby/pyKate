import uvicorn
from fastapi import FastAPI

from pykate.core_router import core_app

root_app = FastAPI()
root_app.mount("/api", core_app)


@root_app.get("/")
async def read_root():
    return {"Hello": "World"}


if __name__ == "__main__":
    uvicorn.run("pykate.main:root_app", host='127.0.0.1', port=8000, reload=True)
