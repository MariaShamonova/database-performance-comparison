import time

from model import StudentFactory
from pymongo.collection import Collection

def read_data_from_mongo_db(collection: Collection, limit: int) -> list[str]:
    t1 = time.time()
    students = list(collection.find({}).limit(limit))
    t2 = time.time()
    execution_time = t2 - t1
    return students, execution_time


def insert_data_in_mongodb(collection: Collection, data: list[dict[str: str]], one_by_one: bool) -> float:
    t1 = time.time()
    if one_by_one:
        for element in data:
            collection.insert_one(element)
    else:
        collection.insert_many(data)
    t2 = time.time()
    execution_time = t2 - t1
    return execution_time


def generate_test_data(num_of_elements: int) -> list[dict[str: str]]:
    test_data = []

    for i in range(num_of_elements):
        test_data.append(dict(StudentFactory()))

    return test_data

