# Usage Examples

## FastAPI Integration

```python
from fastapi import FastAPI
from elasticsearch import Elasticsearch

app = FastAPI()
es = Elasticsearch()

@app.get("/")
def read_root():
    return {"Hello": "World"}
```

// ...additional usage examples...
