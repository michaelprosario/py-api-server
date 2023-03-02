## PyApiServer

Provides a small document management store in Python

## Purpose of project
- Project to explore making small data systems with FastApi and SqlLite
- You can use this project for small hackathon or prototype projects

## How to start server

```
pip install -r requirements.txt
sh start.sh
```
## What does the API look like for managing data?
- The project provides API's for adding, storing, deleting, and searching data
- JSON documents are added to collections
- Visit localhost:8000/docs to view API docs using OpenApi

## Todo
- on add - set createBy
- on update - set updatedBy 
- store
    - make sure following are required
        - name
        - collection
        - userId



