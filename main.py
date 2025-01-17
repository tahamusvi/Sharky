from fastapi import FastAPI
from general.routers import router as general_router
from users.routers import router as users_router

app = FastAPI()

# Include routers
app.include_router(general_router)
app.include_router(users_router)

@app.get("/")
async def root():
    return {"message": "hello!"}