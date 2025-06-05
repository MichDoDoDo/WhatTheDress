from fastapi import FastAPI
from clothing.routes.clothing_router import clothing_router
from user.routes.user_router import user_router
from core.session import get_db
app = FastAPI()

app.include_router(clothing_router, prefix="/api")
app.include_router(user_router, prefix="/api")

if __name__ =="__main__":
    import uvicorn
     
    uvicorn.run(app, host ="0.0.0.0", port=8080)
  