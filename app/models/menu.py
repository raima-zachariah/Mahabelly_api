from enum import Enum
from typing import Optional, List
from pydantic import BaseModel
from uuid import UUID


class Category(str, Enum):
    starters = "starters"
    maincourse = "main course"
    desserts = "desserts"


class Item(BaseModel):
    name: str
    description: Optional[str]
    price: float
    veg: bool
    availability: bool
    category: Category


class ItemResponse(BaseModel):
    itemId: UUID = None
    item: Item


class MenuResponse(BaseModel):
    menu: List[ItemResponse]