# fastapi-elasticsearch-dsl

## Overview
This package provides a scalable, maintainable, and production-ready FastAPI package that replicates the features of `django-elasticsearch-dsl` and `django-elasticsearch-dsl-drf`.

## Installation
```bash
pip install fastapi-elasticsearch-dsl
```

## Usage
```python
from fastapi import FastAPI
from fastapi_elasticsearch_dsl import SomeModule

app = FastAPI()

@app.get("/")
def read_root():
    return {"Hello": "World"}
```

## Contribution Guidelines
Please refer to the `CONTRIBUTING.md` for guidelines on how to contribute to this project.