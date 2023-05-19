from fastapi import APIRouter
from scripts.utils.mongo_utility import Item_handler
from scripts.core.handler.email_handler import Email
from scripts.schemas.inventory_schemas import Item
from scripts.core.handler.email_handler import Email_handler
from scripts.constant.app_constant import EndPoints
import logging
from scripts.logging.logs import logger

try:
    item_router = APIRouter()
    logger.info({"Message": "succesfully established the api router"})
except Exception as e:
    logger.error({"Error": str(e)})


@item_router.post(EndPoints.adding_item)
def adding_item(item_id: int, item: Item):
    try:
        item_object = Item_handler()
        final_list = item_object.add_item(item_id, item)
        return final_list
    except Exception as e:
        logger.error({"Error": str(e)})
        return {"Error": str(e)}


@item_router.delete(EndPoints.deleting_item)
def deleting_item(item_id: int):
    try:
        item_object = Item_handler()
        del_item = item_object.delete_item(item_id)
        return del_item
    except Exception as e:
        logger.error({"Error": str(e)})
        return {"Error": str(e)}


@item_router.put(EndPoints.updating_item)
def updating_item(item_id: int, item: Item):
    try:
        item_object = Item_handler()
        up_item = item_object.update_item(item_id, item)
        return up_item
    except:
        logger.error({"Error": str(e)})
        return {"Error": str(e)}


@item_router.get(EndPoints.getting_items)
def fetch():
    try:
        item_object = Item_handler()
        get_items = item_object.fetch()
        return get_items
    except Exception as e:
        logger.error({"Error": str(e)})
        return {"Error": str(e)}


@item_router.get(EndPoints.total_amount)
def total_price():
    try:
        item_handler = Item_handler()
        result = item_handler.total_price()
        logger.info({"Message:""Succesfully fetched the total amount"})
        return result
    except Exception as e:
        logger.error({"Error": str(e)})
        return {"Error": str(e)}


@item_router.post(EndPoints.sending_email)
def sending_item(email: Email):
    try:
        item_object = Email_handler()
        send_items = item_object.send_email(email)
        logger.info({"Email sent successfully"})
        return "Email sent successfully"
    except Exception as e:
        logger.error({"Error:": str(e)})
        return ({"Error:": str(e)})


@item_router.get(EndPoints.fetching_total)
def find_total():
    try:
        item_object = Item_handler()
        logger.info({"Message:": "Fetched succesfully"})
        return item_object.find_total()
    except Exception as e:
        logger.error({"Error": str(e)})
        return ({"Error": str(e)})
