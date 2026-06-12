from fastapi import APIRouter, Request, Form
from fastapi.responses import HTMLResponse, RedirectResponse
from fastapi.templating import Jinja2Templates

from data.mock_data import MockDataLayer
from data.data import APIDataLayer
from business.service import RBankServiceLayer

router = APIRouter()
# Ajuste do caminho do template para dentro da pasta presentation
templates = Jinja2Templates(directory="presentation/templates")

mock_data = MockDataLayer()
api_data = APIDataLayer("http://localhost:8000")
servico_bancario = RBankServiceLayer(mock_data, api_layer=api_data)

@router.get("/", response_class=HTMLResponse)
async def visualizar_painel(request: Request, cliente: str = ""):
    if cliente:
        servico_bancario.selecionar_conta(cliente)
        conta = servico_bancario.conta_atual
    else:
        conta = None

    todos_clientes = [c.nome for c in mock_data.contas_salvas]

    contexto = {
        "request": request,
        "nome": conta.nome if conta else "Selecione uma conta",
        "rm": conta.rm if conta else "---",
        "saldo": conta.saldo if conta else 0.0,
        "status": "Premium" if conta else "Aguardando",
        "endereco": conta.endereco if conta else "Endereço não cadastrado", 
        "todos_clientes": todos_clientes,
        "cliente_selecionado": cliente
    }
    
    return templates.TemplateResponse("index.html", contexto)

@router.post("/depositar")
async def realizar_deposito(valor: float = Form(...), cliente_atual: str = Form(...)):
    servico_bancario.selecionar_conta(cliente_atual)
    servico_bancario.realizar_deposito(valor)
    return RedirectResponse(url=f"/?cliente={cliente_atual}", status_code=303)

@router.post("/sacar")
async def realizar_saque(valor: float = Form(...), cliente_atual: str = Form(...)):
    servico_bancario.selecionar_conta(cliente_atual)
    servico_bancario.realizar_saque(valor)
    return RedirectResponse(url=f"/?cliente={cliente_atual}", status_code=303)

@router.post("/buscar-cep")
async def buscar_cep(cep: str = Form(...), cliente_atual: str = Form(...)):
    servico_bancario.selecionar_conta(cliente_atual)
    servico_bancario.atualizar_endereco_conta(cep)
    return RedirectResponse(url=f"/?cliente={cliente_atual}", status_code=303)

@router.get("/hw")
def read_root():
    return {"Hello": "World"}

@router.get("/nome-rm")
def read_name():
    return {
        "Nome": "Ramon Queiroz e Silva",
        "RM": "24213522"
    }