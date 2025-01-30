from fastapi import APIRouter, Depends, HTTPException, status
from models.user import UserModel, user_collection, UpdateUserModel, UserCollection
from bson import ObjectId
from pymongo import ReturnDocument
from fastapi.responses import Response
from config.config import settings

user = APIRouter(prefix=f"/v{settings.api_version}/user")

@user.get(
    "/permissions/{email}",
    tags=["users"],
    description="Get user permissions",
)
async def get_user_permissions(email:str):
    user = await user_collection.find_one({"email": email})
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="User not found")
    return {"permissions": user.get("allowed_customers", [])}
