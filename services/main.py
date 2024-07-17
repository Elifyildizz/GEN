from fastapi import FastAPI
from users.users import router as users_router
from scans.scans import router as scans_router
from organisations.organisations import router as organisations_router

app = FastAPI()

app.include_router(users_router, prefix="/api/users", tags=["users"])
app.include_router(scans_router, prefix="/api/scans", tags=["scans"])
app.include_router(organisations_router, prefix="/api/organisations", tags=["organisations"])
