from fastapi import FastAPI, HTTPException
from starlette.responses import Response

from db.models import UserAnswer
from api import api

import uvicorn

app = FastAPI()

@app.get("/")
def index():
    return {'message': 'Index.'}

@app.get("/user")
def read_user():
    return api.read_user()

@app.get("/photos")
def read_photos():
    return api.read_photos()




if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=5000, log_level="info")

