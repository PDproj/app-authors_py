from fastapi import FastAPI
from server.routes.author import router as AuthorRouter

app = FastAPI()

app.include_router(AuthorRouter, tags=["Author"], prefix="/authors")


@app.get("/", tags=['root'])
async def read_root():
    return {"message": "Authors App"}
