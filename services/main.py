from fastapi import FastAPI
from services.users.users import router as users_router
from services.scans.scans import router as scans_router
from services.organisations.organisations import router as organisations_router

app = FastAPI()

app.include_router(users_router, prefix="/api/users", tags=["users"])
app.include_router(scans_router, prefix="/api/scans", tags=["scans"])
app.include_router(organisations_router, prefix="/api/organisations", tags=["organisations"])


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)