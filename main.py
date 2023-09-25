from fastapi.middleware.cors import CORSMiddleware
from fastapi import FastAPI, Form, BackgroundTasks, HTTPException
from pydantic import BaseModel
from typing import Annotated
import uvicorn
from send_mail import send_mail

app = FastAPI()

origins = [
    "http://127.0.0.1:5500",
    "https://alika.uz",
    "http://alika.uz",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.post("/api/submit")
async def submit_form(name: Annotated[str, Form()],
                      email: Annotated[str, Form()],
                      message: Annotated[str, Form()]):
    try:
        send_mail(name, email, message)
        return {'message': 'Email sent successfully'}
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

if __name__ == '__main__':
    uvicorn.run('main:app', reload=True)
