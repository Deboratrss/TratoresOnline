from fastapi import FastAPI
from pydantic import BaseModel
import sqlite3
import traceback

app = FastAPI()

DATABASE = 'ecommerce.db'

conn = sqlite3.connect(DATABASE)
cursor = conn.cursor()

cursor.execute("""
    CREATE TABLE IF NOT EXISTS informacoes_pessoais (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nome TEXT,
        endereco TEXT,
        email TEXT
    )
""")

cursor.execute("""
    CREATE TABLE IF NOT EXISTS informacoes_pagamento (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        numero_cartao TEXT,
        data_validade TEXT,
        codigo_seguranca INTEGER
    )
""")

produtos_estoque = {
    1: {"Item": "Trator Verde", "Preço unitário": "R$ 300.000,00", "Quantidade em estoque": 3, "Oferta": True, "Descricao": "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Maecenas mattis orci cursus, lacinia nisl ac, tempor lorem. Duis in vestibulum felis, id molestie sapien"},
    2: {"Item": "Trator Amarelo", "Preço unitário": "R$ 300.000,00", "Quantidade em estoque": 4, "Oferta": True, "Descricao": "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Maecenas mattis orci cursus, lacinia nisl ac, tempor lorem. Duis in vestibulum felis, id molestie sapien"},
    3: {"Item": "Trator Azul", "Preço unitário": "R$ 300.000,00", "Quantidade em estoque": 2, "Oferta": True, "Descricao": "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Maecenas mattis orci cursus, lacinia nisl ac, tempor lorem. Duis in vestibulum felis, id molestie sapien"},
    4: {"Item": "Trator Vermelho", "Preço unitário": "R$ 280.000,00", "Quantidade em estoque": 8, "Oferta": False, "Descricao": "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Maecenas mattis orci cursus, lacinia nisl ac, tempor lorem. Duis in vestibulum felis, id molestie sapien"},
    5: {"Item": "Trator de Colheita", "Preço unitário": "R$170.000,00", "Quantidade em estoque": 10, "Oferta": True, "Descricao": "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Maecenas mattis orci cursus, lacinia nisl ac, tempor lorem. Duis in vestibulum felis, id molestie sapien"},
    6: {"Item": "Trator de Fertilizacao", "Preço unitário": "R$170.000,00", "Quantidade em estoque": 8, "Oferta": False, "Descricao": "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Maecenas mattis orci cursus, lacinia nisl ac, tempor lorem. Duis in vestibulum felis, id molestie sapien"},
    7: {"Item": "Trator de Colheita", "Preço unitário": "R$570.000,00", "Quantidade em estoque": 1, "Oferta": True, "Descricao": "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Maecenas mattis orci cursus, lacinia nisl ac, tempor lorem. Duis in vestibulum felis, id molestie sapien"},
    8: {"Item": "Trator Esportivo", "Preço unitário": "R$470.000,00", "Quantidade em estoque": 3, "Oferta": False, "Descricao": "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Maecenas mattis orci cursus, lacinia nisl ac, tempor lorem. Duis in vestibulum felis, id molestie sapien"},
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


class InformacoesPessoais(BaseModel):
    nome: str
    endereco: str
    email: str


class InformacoesPagamento(BaseModel):
    numero_cartao: str
    data_validade: str
    codigo_seguranca: int


@app.get("/")
def home():
    return {"Tipos de tratores": len(produtos_estoque)}


@app.get("/estoque/{id_estoque}")
def pegar_estoque(id_estoque: int):
    if id_estoque in produtos_estoque:
        return produtos_estoque[id_estoque]
    else:
        return {"Erro: ID de produto inexistente"}


@app.get("/tratores")
async def listar_tratores():
    return produtos_estoque


@app.get("/vendas/{id_vendidos}")
def pegar_venda(id_vendidos: int):
    if id_vendidos in produtos_vendidos:
        return produtos_vendidos[id_vendidos]
    else:
        return {"Erro: ID de produto inexistente"}


@app.post("/informacoes_pessoais")
def salvar_informacoes_pessoais(info_pessoais: InformacoesPessoais):
    try:
        nome = info_pessoais.nome
        endereco = info_pessoais.endereco
        email = info_pessoais.email
        cursor.execute("INSERT INTO informacoes_pessoais (nome, endereco, email) VALUES (?, ?, ?)", (nome, endereco, email))
        conn.commit()
        return {"Mensagem": "Informações pessoais salvas com sucesso"}
    except:
        return {"Erro": "Ocorreu um erro ao salvar as informações pessoais"}


@app.post("/informacoes_pagamento")
def salvar_informacoes_pagamento(info_pagamento: InformacoesPagamento):
    try:
        numero_cartao = info_pagamento.numero_cartao
        data_validade = info_pagamento.data_validade
        codigo_seguranca = info_pagamento.codigo_seguranca
        cursor.execute("INSERT INTO informacoes_pagamento (numero_cartao, data_validade, codigo_seguranca) VALUES (?, ?, ?)", (numero_cartao, data_validade, codigo_seguranca))
        conn.commit()
        return {"Mensagem": "Informações de pagamento salvas com sucesso"}
    except:
        return {"Erro": "Ocorreu um erro ao salvar as informações de pagamento"}