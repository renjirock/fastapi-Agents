from __future__ import annotations

from pydantic import ConfigDict, BaseModel, Field, EmailStr
from typing import Optional, List

from config.db import PyObjectId, db
from bson import ObjectId
from datetime import datetime


user_collection = db.get_collection("user")


class UserModel(BaseModel):
    id: Optional[PyObjectId] = Field(alias="_id", default=None)
    name: str = Field(...)
    email: EmailStr = Field(...)
    password: Optional[str] = Field(...)
    type: str = Field(...)
    allowed_customers: List[str] = Field(default_factory=list)
    customer_id: Optional[str] = ''
    elastic_password: Optional[str] = ''
    created_at: Optional[datetime] = datetime.now()
    model_config = ConfigDict(
        populate_by_name=True,
        arbitrary_types_allowed=True,
        json_schema_extra={
            "example": {
                "name": "Jane Doe",
                "email": "jdoe@example.com",
                "password": "admin123",
                "type": 'admin'
            }
        },
    )


class UpdateUserModel(BaseModel):
    name: Optional[str] = None
    email: Optional[EmailStr] = None
    password: Optional[str] = None
    type: Optional[str] = None
    allowed_customers: List[str] = Field(default_factory=list)
    customer_id: Optional[str] = None
    elastic_password: Optional[str] = None
    model_config = ConfigDict(
        arbitrary_types_allowed=True,
        json_encoders={ObjectId: str},
        json_schema_extra={
            "example": {
                "name": "Jane Doe",
                "email": "jdoe@example.com",
                "password": "admin123",
                "type": 'admin',
                "customer_id": '',
                'elastic_password': ''
            }
        },
    )


class UserCollection(BaseModel):

    users: List[UserModel]


class Token(BaseModel):
    access_token: str
