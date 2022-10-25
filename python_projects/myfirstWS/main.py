from fastapi import FastAPI

app = FastAPI()

@app.get("/test")
def index():
    return {"value":"test service"}
