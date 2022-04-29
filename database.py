from pymongo import MongoClient
from enum import Enum
from pymongo.collection import Collection
from settings import Settings


class DataBaseTypeEnum(Enum):
    cloud = "cloud"
    local = "local"
    container_local = "container_local"


SETTINGS = Settings()

DATABASE_TYPE_URL_MAPPING = {
        DataBaseTypeEnum.cloud: SETTINGS.CLOUD_MONGO_URL,
        DataBaseTypeEnum.local: SETTINGS.LOCAL_MONGO_URL,
        DataBaseTypeEnum.container_local: SETTINGS.CONTAINER_MONGO_URL
    }


def get_database_connection(database_type: DataBaseTypeEnum, need_clean: bool) -> Collection:
    mongo_url = DATABASE_TYPE_URL_MAPPING[database_type]
    client = MongoClient(mongo_url)
    database = client.students
    student_collection: Collection = database.get_collection("students_collection")
    if need_clean:
        student_collection.delete_many({})


    return student_collection


