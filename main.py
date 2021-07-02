import models
from fastapi import FastAPI, Request, Depends
from starlette.responses import RedirectResponse
from api import items, orders
from db.database import engine
from sqlalchemy.orm import Session

app = FastAPI()
app.include_router(items.router)
app.include_router(orders.router)


models.Base.metadata.create_all(bind=engine)


@app.get("/")
async def index():
    return RedirectResponse(url='/docs')
