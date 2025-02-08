from fastapi import FastAPI
from datetime import datetime

app = FastAPI()

@app.get("/number/{num}")
def show_number(num: int):
    return {"number": num}

@app.get("/datetime")
def show_datetime():
    return {"datetime": datetime.now().isoformat()}
