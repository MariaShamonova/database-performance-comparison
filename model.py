import factory
from pydantic import BaseModel


class UserModel(BaseModel):
    name: str
    email: str
    address: str

    class Config:
        schema_extra = {
            "example": {
                "name": "Jane Doe",
                "email": "jdoe@example.com",
                "address": "791 Crist Parks, Sashabury, IL 86039-9874",
            }
        }

class Chart(BaseModel):
    nums_of_data: list[int]
    times: list[float]

class Response(BaseModel):
    data: list[UserModel] | None = None
    chart: Chart

class StudentFactory(factory.Factory):
    name = factory.Faker("name")
    email = factory.Faker("email")
    address = factory.Faker("address")

    class Meta:
        model = UserModel

