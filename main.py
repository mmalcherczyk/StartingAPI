from fastapi import FastAPI
from db import keyvalue

import uvicorn

app = FastAPI()

@app.get("/")
def index():
    return {'message': 'Index.'}

@app.get("/users")
def read_users():
    return keyvalue.get(args=None)
        

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=5000, log_level="info")
    

