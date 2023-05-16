from scripts.schemas.inventory_schemas import Item
import pymongo
from pymongo import MongoClient
from scripts.db.mongo import collection




class Item_handler:

    def add_item(self, item_id: int, item: Item):
            if list(collection.find({"item_id": item_id})):
                return {"error": "This ID is already present"}

            collection.insert_one(item.dict())
            return {"message": "Successfully Added"}



    def delete_item(self, item_id: int):
            if list(collection.find({"item_id": item_id})) == []:
                return {"error", "Item not found"}

            else:
                collection.delete_one({"item_id": item_id})
                return {"Message": "Item deleted succesfully"}


    def update_item(self, item_id: int, item: Item):
            if list(collection.find({"item_id": item_id})) != []:
                collection.update_one({"item_id": item_id}, {
                                      "$set": item.dict()})
                return {"Message": "It is updated successfully"}
            else:
                return {"error": "Item not found"}



    def total_price(self):
        item_price = [item["item_price"] * item["item_volume"]
                      for item in collection.find()]
        total_price = sum(item_price)
        return total_price

    def fetch(self):
            items = list(collection.find({}))
            final_items = []
            for each in items:
                del each["_id"]
                final_items.append(each)
            return final_items


    def find_total(self):
        total = collection.aggregate([
    {
        '$project': {
            '_id': 0,
            'mul': {
                '$multiply': [
                    '$item_price', '$item_volume'
                ]
            }
        }
    }, {
        '$group': {
            '_id': None,
            'total_price': {
                '$sum': '$mul'
            }
        }
    }, {
        '$project': {
            '_id': 0
        }
    }
])
        return (list(total))[0]['total_price']
