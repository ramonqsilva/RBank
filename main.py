import uvicorn
from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
# Ajuste do import do roteador para a nova estrutura de pastas
from presentation.routes.route import router

app = FastAPI()

app.include_router(router)

if __name__ == "__main__":
    print("Iniciando o servidor Web do RBank...")
    uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True)