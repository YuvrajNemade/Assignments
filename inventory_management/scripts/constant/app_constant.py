class EndPoints:
    """ this class helps in creating constants for the end points"""

    getting_items = "/"
    adding_item = "/add/{item_id}"
    updating_item = "/update/{item_id}"
    deleting_item = "/remove/{item_id}"
    total_amount = "/total_amount"
    sending_email = "/send_email"
    fetching_total = "/total"


class DatabaseConstants:
    """ this class is used to create database constants """
    database_name = "interns_b2_23"
    collection_name = "yuvraj_nemade"
    uri = "mongodb://intern_23:intern%40123@192.168.0.220:2717/interns_b2_23"


db_constant_object = DatabaseConstants()


class Aggregation:
        aggregate = [
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
                    '_id': 0,
                    'total_price': {
                        '$sum': '$mul'
                    }
                }
            }, {
                '$project': {
                    '_id': 0
                }
            }]


class CommonConstant:
    APP_KEY = "main:app"