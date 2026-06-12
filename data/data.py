import requests

class APIDataLayer:
    def __init__(self, base_url=""):
        self.base_url = base_url

    def buscar_dados_cliente(self):
        try:
            resposta = requests.get(f"{self.base_url}/nome-rm")
            resposta.raise_for_status() 
            return resposta.json()
        except requests.RequestException as erro:
            return {"erro": f"Falha ao conectar com a API: {erro}"}

    def buscar_endereco_por_cep(self, cep):
        cep_limpo = str(cep).replace("-", "").replace(" ", "")
        url = f"https://viacep.com.br/ws/{cep_limpo}/json/"
        
        try:
            resposta = requests.get(url)
            resposta.raise_for_status() 
            dados = resposta.json()
            
            if "erro" in dados:
                return {"erro": "CEP não encontrado."}
            return dados
        except requests.RequestException as erro:
            return {"erro": f"Falha ao conectar com a API ViaCEP: {erro}"}