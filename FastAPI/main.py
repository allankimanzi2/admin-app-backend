# main.py
import uvicorn
import pyrebase
from fastapi import FastAPI, HTTPException
from models import LoginSchema, SignUpSchema
from fastapi.responses import JSONResponse
from fastapi.requests import Request
from firebase_admin import credentials, auth, initialize_app

app = FastAPI()

if not firebase_admin._apps:
    cred = credentials.Certificate("serviceAccountKey.json")
    initialize_app(cred)

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
    return {"message": ""}

@app.post('/signup')
async def create_an_account(user_data: SignUpSchema):
    email = user_data.email
    password = user_data.password

    try:
        user = auth.create_user(
            email=email,
            password=password
        )

        return JSONResponse(content={"message": f"User account created successfully for user {user.uid}"},
                            status_code=201
                           )
    except auth.EmailAlreadyExistsError:
        raise HTTPException(
           status_code=400,
           detail=f"Account already created for the email {email}"
        )

@app.post('/login')
async def create_access_token(user_data: LoginSchema):
    email = user_data.email
    password = user_data.password

    try:
        user = auth.sign_in_with_email_and_password(
            email=email,
            password=password
        )
        token = user['idToken']

        return JSONResponse(
            content={"token": token},
            status_code=200
        )

    except:
        raise HTTPException(
            status_code=400, detail="Invalid Credentials"
        )

@app.post('/ping')
async def validate_token(request: Request):
    headers = request.headers
    jwt = headers.get('authorization')

    user = auth.verify_id_token(jwt)

    return user.uid

if __name__ == "__main__":
    uvicorn.run("main:app")
