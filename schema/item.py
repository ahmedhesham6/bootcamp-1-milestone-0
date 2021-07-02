from typing import List, Optional
from pydantic import BaseModel


class ItemBase(BaseModel):
    name: str
    cost: float
    available_quantity: int


class ItemUpdate(BaseModel):
    name: Optional[str]
    cost: Optional[str]
    available_quantity: Optional[str]

    def dict(self, *args, **kwargs):
        kwargs["exclude_none"] = True
        return BaseModel.dict(self, *args, **kwargs)
