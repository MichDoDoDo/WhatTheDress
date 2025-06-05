from fastapi import FastAPI
from clothing.routes.clothing_router import clothing_router
from user.routes.user_router import user_router
from core.database import get_db_sessiion
app = FastAPI()

app.include_router(clothing_router, prefix="/api")
app.include_router(user_router, prefix="/api")

if __name__ =="__main__":
    import uvicorn
    uvicorn.run(app, host ="0.0.0.0", port=8080)
    
    db = get_db_sessiion()
    if(db):
        print("hellpo db")
    