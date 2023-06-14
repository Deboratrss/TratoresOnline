from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

produtos_estoque = {
    1: {"Item": "Trator Verde", "Preço unitário": "R$ 300.000,00", "Quantidade em estoque": 3, "Oferta": True},
    2: {"Item": "Trator Amarelo", "Preço unitário": "R$ 300.000,00", "Quantidade em estoque": 4, "Oferta": True},
    3: {"Item": "Trator Azul", "Preço unitário": "R$ 300.000,00", "Quantidade em estoque": 2, "Oferta": True},
    4: {"Item": "Trator Vermelho", "Preço unitário": "R$ 280.000,00", "Quantidade em estoque": 8, "Oferta": False},
    5: {"Item": "Trator de Colheita", "Preço unitário": "R$170.000,00", "Quantidade em estoque": 10, "Oferta": True},
    6: {"Item": "Trator de Fertilizacao", "Preço unitário": "R$170.000,00", "Quantidade em estoque": 8, "Oferta": False},
    7: {"Item": "Trator de Colheita", "Preço unitário": "R$570.000,00", "Quantidade em estoque": 1, "Oferta": True},
    8: {"Item": "Trator Esportivo", "Preço unitário": "R$470.000,00", "Quantidade em estoque": 3, "Oferta": False},
}


produtos_vendidos = {
    1: {"Item": "Trator Verde", "Preço unitário": "R$ 300.000,00", "Quantidade vendida": 3},
    2: {"Item": "Trator Amarelo", "Preço unitário": "R$ 300.000,00", "Quantidade vendida": 8},
    3: {"Item": "Trator Azul", "Preço unitário": "R$ 300.000,00", "Quantidade vendida": 12},
    4: {"Item": "Trator Vermelho", "Preço unitário": "R$ 280.000,00", "Quantidade vendida": 2},
    5: {"Item": "Trator de Colheita", "Preço unitário": "R$170.000,00", "Quantidade vendida": 20},
    6: {"Item": "Trator de Fertilizacao", "Preço unitário": "R$170.000,00", "Quantidade vendida": 20},
    7: {"Item": "Trator de Colheita", "Preço unitário": "R$570.000,00", "Quantidade vendida": 28},
    8: {"Item": "Trator Esportivo", "Preço unitário": "R$470.000,00", "Quantidade vendida": 42},
}


@app.get("/")
def home():
    return {"Tipos de tratotes": len(produtos_estoque)}

@app.get("/estoque/{id_estoque}")
def pegar_estoque(id_estoque: int):
    if id_estoque in produtos_estoque:
        return produtos_estoque[id_estoque]
    else:
        return {"Erro: ID produto inexistente"}


@app.get("/vendas/{id_vendidos}")
def pegar_venda(id_vendidos: int):
    if id_vendidos in produtos_vendidos:
        return produtos_vendidos[id_vendidos]
    else:
        return {"Erro: ID produto inexistente"}


class DadosPessoais(BaseModel):
    nome: str
    num_telefone: str
    email: str
    endereco_entrega: str
    comentarios: str


class FormaPagamento(BaseModel):
    num_cartao: str
    mmaa: str
    cvv: str
    titular_cartao: str


@app.post("/pedido")
def pedido(personal_data: DadosPessoais, card_data: FormaPagamento):
    info = {
        "Dados_Pessoais": DadosPessoais.dict(),
        "Forma_Pagamento": FormaPagamento.dict()
    }
    return {"info": info}