from fastapi import FastAPI  # type: ignore

app = FastAPI()


@app.get("/add")
def add(left: int, right: int) -> dict:
    result: int = left + right
    return {"sum": result}
