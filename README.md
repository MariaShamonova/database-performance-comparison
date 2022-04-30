# Backend


### Install packages
```
pip install requirements.txt
```


### Run FastAPI
```
uvicorn main:app --reload
```

### Run local server
#### Install MongoDB
- Download the binaries from the [MongoDB Download Center](https://www.mongodb.com/try/download)
- Ensure the location of the binaries is in the PATH variable
    ```
    export PATH=<mongodb-install-directory>/bin:$PATH
    ```
- Run MongoDB
    ```
    mongod --dbpath <path to data directory>
    ```
### Running a local server using containerization technologies (Docker)
```
docker-compose up -d
```
