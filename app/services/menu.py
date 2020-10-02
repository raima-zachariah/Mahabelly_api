from models.menu import Item, ItemResponse
import uuid
from uuid import UUID
import copy


class MenuService:
    def __init__(self):
        self.itemId: UUID = None

    def add_item(self, payload: Item):
        try:
            self.itemId = uuid.uuid4()
            return {"itemId": self.itemId, "item": payload}
        except Exception as e:
            raise e

    def get_menu(self):
        raise NotImplementedError

    def get_item_by_id(self, itemId):
        raise NotImplementedError

    def update_item(self, itemId, payload: Item):
        raise NotImplementedError

    def delete_item(self, itemId):
        raise NotImplementedError
