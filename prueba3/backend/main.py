import uvicorn

from typing import Optional
from fastapi import FastAPI
from requests.auth import HTTPBasicAuth
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware
    
import requests
app = FastAPI()


origins = [
    "http://localhost:3000",
    "https://prueba4redsis.netlify.app"
]
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


class Payload(BaseModel):
    payloadId: str
    nombre:str
    apellido:str

@app.get("/createPayload")
def create_payload():
    url = "https://securetransfer.redsis.com/rest/forms/v1/teamGoAny/payload"
    r = requests.get(url, auth=("ingresoRedsis","Qwerty0909$"))
    
    return r.json()


@app.post("/submit")
def submit(payload: Payload):
    
    url = f"https://securetransfer.redsis.com/rest/forms/v1/teamGoAny/payload/{payload.payloadId}/submit"
    print(payload.nombre)
    r = requests.post(url,json={"nombre":payload.nombre, "apellido": payload.apellido},auth=("ingresoRedsis","Qwerty0909$"))
    
    return r.json()


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8080)