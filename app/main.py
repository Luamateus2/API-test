import uvicorn
from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session
from app.core.database import Base, engine, SessionLocal
from app.api.routes import roupa, estoque  # Importando os routers

# Criação da aplicação FastAPI
app = FastAPI(title="Loja API")

# Função para obter a sessão do banco de dados
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# Rota de exemplo
@app.get("/")
def read_root(db: Session = Depends(get_db)):
    return {"message": "API funcionando!"}

# Registrando as rotas
app.include_router(roupa.router)  # Incluindo as rotas de Roupa
app.include_router(estoque.router)  # Incluindo as rotas de Estoque

if __name__ == '__main__':
    uvicorn.run(app, host='0.0.0.0', port=8003)
