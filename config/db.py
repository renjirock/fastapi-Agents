import motor.motor_asyncio
from typing_extensions import Annotated
from pydantic.functional_validators import BeforeValidator
import certifi
from config.config import settings

client = motor.motor_asyncio.AsyncIOMotorClient(settings.url_db, tlsCAFile=certifi.where())

db = client[settings.name_db]

PyObjectId = Annotated[str, BeforeValidator(str)]