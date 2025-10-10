from fastapi import FastAPI
from util.database import init_db

from controller.person import router as persons_router
from controller.address import router as addresses_router

app = FastAPI(title="FastAPI + SQLModel - Pessoas e Endereços")

init_db()

app.include_router(persons_router)
app.include_router(addresses_router)

@app.get("/")
def health():
    return {"status": "ok"}