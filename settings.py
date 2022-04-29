from pydantic import BaseModel


class Settings(BaseModel):
    NUM_OF_TEST_DATA: int = 1000

    CLOUD_MONGO_URL: str = "mongodb+srv://mariashamonova:MashaMaria@cluster0.hsv42.mongodb.net/myFirstDatabase?retryWrites=true&w=majority"
    LOCAL_MONGO_URL: str = 'mongodb://localhost:27017/MyFirstDatabase'
    CONTAINER_MONGO_URL: str = 'mongodb://localhost:27018/MyFirstDatabase'