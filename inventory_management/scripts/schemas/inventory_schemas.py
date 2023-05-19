from pydantic import BaseModel


class Item(BaseModel):
    """This class takes the parameters for the item in the inventory"""
    item_id: int
    item_name: str
    item_price: int
    item_volume: int


class Email(BaseModel):
    """This class takes the parameters for the Emails"""
    rec_email: str
    subject: str
    body: str