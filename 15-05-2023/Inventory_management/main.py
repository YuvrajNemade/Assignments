from fastapi import FastAPI
from scripts.services.inventory_services import item_router


app = FastAPI()
item_data = {}


app.include_router(item_router)

