## PyApiServer

Provides a small document management store in Python

## Purpose of project
- Project to explore making small data systems with FastApi and SqlLite or Postgres
- You can use this project for small hackathon or prototype projects

## How to start server

```
pip install -r requirements.txt
cd app
sh start.sh
```
## What does the API look like for managing data?
- The project provides API's for adding, storing, deleting, and searching data
- JSON documents are added to collections
- Visit localhost:8000/docs to view API docs using OpenApi

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
- Write validators for other requests
    - get docs
    - get doc
    - delete
- Find docker container with pgvector installed
- Create table to store vector for doc

# References
- https://bugbytes.io/posts/vector-databases-pgvector-and-langchain/
- langchain, pgvector - https://www.youtube.com/watch?v=FDBnyJu_Ndg

