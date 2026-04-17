from fastapi import FastAPI
from pydantic import BaseModel
from typing import Optional, List

app = FastAPI()


from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def root():
    message = "Debugger test running"
    print(message)
    return {"message": message}


@app.get("/debug")
def debug_test():
    number = 10
    result = number * 2   # ← set breakpoint here
    return {"result": result}


@app.get("/sum/{a}/{b}")
def sum_numbers(a: int, b: int):
    total = a + b   # ← breakpoint here
    return {"a": a, "b": b, "sum": total}