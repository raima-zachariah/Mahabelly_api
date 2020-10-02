from fastapi import APIRouter
from models.menu import Item, ItemResponse, MenuResponse
from services.menu import MenuService

router = APIRouter()


@router.post(
    "/menu",
    response_model=ItemResponse,
    status_code=201,
    responses={
        400: {"description": "Bad Request"},
        500: {"description": "Internal Server Error"},
    },
)
def add_item(payload: Item):
    return MenuService().add_item(payload=payload)


@router.get(
    "/menu",
    response_model=MenuResponse,
    status_code=200,
    responses={
        500: {"description": "Internal Server Error"},
    },
)
def get_menu():
    return MenuService().get_menu()


@router.get(
    "/menu/{itemId}",
    response_model=ItemResponse,
    status_code=200,
    responses={
        500: {"description": "Internal Server Error"},
    },
)
def get_menu():
    return MenuService().get_item_by_id()


@router.put(
    "/menu/{itemId}",
    response_model=ItemResponse,
    status_code=200,
    responses={
        500: {"description": "Internal Server Error"},
    },
)
def update_menu():
    return MenuService().update_item()


@router.delete(
    "/menu/{itemId}",
    status_code=204,
    responses={
        500: {"description": "Internal Server Error"},
    },
)
def update_menu():
    return MenuService().delete_item()