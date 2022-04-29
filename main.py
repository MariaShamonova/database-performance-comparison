import time

from database import get_database_connection, DataBaseTypeEnum
from fastapi import FastAPI
import service
from model import Response, Chart
from settings import Settings

app = FastAPI()

SETTINGS = Settings()

print('Generating test data ...')
TEST_DATA = service.generate_test_data(SETTINGS.NUM_OF_TEST_DATA)
print('Test data is ready!')


@app.get("/test-write",
         description=f"Current num of test data {SETTINGS.NUM_OF_TEST_DATA} elements.")
async def run_benchmark(one_by_one: bool, database_connection: DataBaseTypeEnum):
    length_of_data = SETTINGS.NUM_OF_TEST_DATA
    step = int(SETTINGS.NUM_OF_TEST_DATA / 10)
    if one_by_one:
        length_of_data = int(SETTINGS.NUM_OF_TEST_DATA / 10)
        step = int(SETTINGS.NUM_OF_TEST_DATA / 100)

    nums_of_data = []
    times = []

    for i in range(0, length_of_data + step, step):
        if i == 0:
            i += 1
        connection = get_database_connection(database_connection, True)
        data = TEST_DATA[0: i]

        execution_time = service.insert_data_in_mongodb(connection, data=data, one_by_one=one_by_one)
        nums_of_data.append(len(data))
        times.append(execution_time)

    return Response(chart=Chart(nums_of_data=nums_of_data, times=times)).dict(exclude={'data'})

@app.get("/test-read",
         description=f"Current num of test data {SETTINGS.NUM_OF_TEST_DATA} elements.")
async def run_benchmark(database_type: DataBaseTypeEnum) -> Response:

    connection = get_database_connection(database_type, False)
    t1 = time.time()
    students = service.read_data_from_mongo_db(connection)
    t2 = time.time()
    execution_time = t2 - t1
    return Response(data=students, execution_time=execution_time)
