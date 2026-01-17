from fastapi import FastAPI  # type: ignore

app = FastAPI()


@app.get("/add")
def add(left: int, right: int):
    return {"sum": left + right}
