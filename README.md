## PyApiServer

Provides a small document management store in Python

## Purpose of project
- Project to explore making small data systems with FastApi and SqlLite or Postgres
- You can use this project for small hackathon or prototype projects

## Getting started

Clone the git repository to a local working folder

``` bash
git clone https://github.com/michaelprosario/py-api-server
```

Navigate to the root of the repository

Setup an environment variable using bash to your Postgres database
```
export PG_CONNECTION_STRING="postgresql://myUserName:myPassword@myHost:5432/myDbName"
```

Please note that you need to edit the connection string environment variable for your credentials and Postgres server

```
pip install -r requirements.txt
cd app
sh start.sh
```
## What does the API look like for managing data?
- The project provides API's for adding, storing, deleting, and searching data
- JSON documents are added to collections
- Visit localhost:8000/docs to view API docs using OpenApi

## How do you setup a Postgres database using docker-compose?
- Install Docker and Docker-compose on your system
- Navigate to the root of the git repository
- Navigate to dockerCompose folder

```
docker-compose up -d
```

This will start a Postgres instance accessible to your local machine.
You can also access PGAdmin via a web browser: 
http://localhost:5050

Please see the docker-compose file for details for default user name and password configuration.

## Docker build

```
docker build -t pyapiserver .
```

## Test container local

```
docker run -d -p 80:80 pyapiserver
```

## Todo
- Write docs
- Create table to store vector for doc
- Write docs / Store data to collection
- Write docs / Getting data to collection
- Write docs /List data to collection

# References
- https://bugbytes.io/posts/vector-databases-pgvector-and-langchain/
- langchain, pgvector - https://www.youtube.com/watch?v=FDBnyJu_Ndg
- https://fastapi.tiangolo.com
- https://docs.pydantic.dev/latest/
- https://www.sqlalchemy.org/
