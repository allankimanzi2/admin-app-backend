# main.py
import uvicorn
import pyrebase
from fastapi import FastAPI

app = FastAPI()


import firebase_admin
from firebase_admin import credentials

if not firebase_admin._apps:
    cred = credentials.Certificate("serviceAccountKey.json")
    firebase_admin.initialize_app(cred)

firebaseConfig = {

  "apiKey": "AIzaSyA4jJ_OW8wOxjD36yr7FPiTNAmavmLGYbI",
  "authDomain": "admin-app-71c16.firebaseapp.com",
  "projectId": "admin-app-71c16",
  "storageBucket": "admin-app-71c16.appspot.com",
  "messagingSenderId": "483305910482",
  "appId": "1:483305910482:web:0a00e66f316cee45afbd0b",
  "measurementId": "G-9THRNVXY2S"
}

firebase = pyrebase.initialize_app(firebaseConfig)



@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.post('/signup')
async def create_an_account():
    pass

@app.post('/login')
async def create_access_token():
    pass

@app.post('/ping')
async def validate_token():
    pass


if __name__ == "__main__":
    uvicorn.run("main:app")