from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from .routes import products, fornecedores, movimentacoes

app = FastAPI(title="Controle de Estoque - Backend")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/health")
def health():
    return {"status": "ok"}


app.include_router(products.router)
app.include_router(fornecedores.router)
app.include_router(movimentacoes.router)
