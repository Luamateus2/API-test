import uvicorn
from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session
from app.core.database import get_db
from app.api.routes import roupa, estoque

app = FastAPI(title="Loja API")

@app.get("/")
def read_root(db: Session = Depends(get_db)):
    return {"message": "API funcionando!"}

app.include_router(roupa.router)
app.include_router(estoque.router)

if __name__ == '__main__':
    uvicorn.run(app, host='0.0.0.0', port=8003)
