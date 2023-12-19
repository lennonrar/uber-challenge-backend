from fastapi import FastAPI
from app.core.models import UserModel, UserModelPost, UserModelUpdate
from adapters.http import create_user_route, update_user_route

app = FastAPI()

app.include_router(create_user_route, update_user_route)



# TODO refactor
# @app.get("/")
# async def root():
#     return {"message": "Hello World"}


# @app.get("/items/{item_id}")
# async def get_update_item(item_id: int) -> object:
#     return {"item_id": item_id}


# @app.get("/user/{user_name}")
# async def get_item_by_name(user_name: UserModel) -> object:
#     if user_name is UserModel.alexnet:
#         return {"model_name": user_name}
#     return {"model_name": UserModel.resnet}


# @app.get("/user/")
# async def get_user(search: str = None) -> object:
#     if search:
#         return {"search": search.upper()}
#     else:
#         return {"search": None}
