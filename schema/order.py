from typing import List, Optional
from pydantic import BaseModel


class OrderBase(BaseModel):
    item_id: int
    shopping_cart_id: int
    requested_quantity: int


class OrderUpdate(BaseModel):
    item_id: Optional[int]
    shopping_cart_id: Optional[int]
    requested_quantity: Optional[int]
