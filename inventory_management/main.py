from fastapi import FastAPI
from scripts.services.inventory_services import item_router
from scripts.logging.logs import logger
from scripts.constant.app_constant import *
from scripts.constant.app_configuration import *
import uvicorn

app = FastAPI()
item_data = {}

try:
    app.include_router(item_router)
except:
    logger.error({"Error:": "Unexpected method happened with the router"})

if __name__ == "__main__":
    uvicorn.run("main:app", host=SERVICE_HOST, port=int(SERVICE_PORT), reload=True)
