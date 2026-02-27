from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

from main import process_query

app = FastAPI(
    title="Offline NL to SQL Engine",
    description="Converts natural language to SQL queries",
    version="1.0"
)

class QueryRequest(BaseModel):
    query: str


class QueryResponse(BaseModel):
    sql: str


@app.post("/nl-to-sql/", response_model=QueryResponse)
def convert_query(request: QueryRequest):
    try:
        sql = process_query(request.query)
        return QueryResponse(sql=sql)
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))
