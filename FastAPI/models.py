from pydantic import BaseModel



class SignUpSchema(BaseModel):
    email:str
    password:str

    class Config:
        schema_extra ={
            "example":{
                "email":"test@gmail.com",
                "password":"123456"
            }
        }


class LoginSchema(BaseModel):
    email:str
    password:str

    class Config:
        schema_extra ={
            "example":{
                "email":"test@gmail.com",
                "password":"123456"
            }
        }