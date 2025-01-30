from fastapi import FastAPI
from routes.user import user
from config.openapi import tags_metadata
from config.config import settings

app = FastAPI(
    title=settings.app_name,
    description="a REST API using python and mongoDB",
    version="0.0.1",
    openapi_tags=tags_metadata,
)

app.include_router(user)
