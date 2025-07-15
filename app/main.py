from fastapi import FastAPI
from app.users.router import router as router_users
from app.diagnosiss.router import router as router_diagnosiss


app = FastAPI()


@app.get("/")
def home_page():
    return {"message": "Привет!"}


app.include_router(router_users)
app.include_router(router_diagnosiss)