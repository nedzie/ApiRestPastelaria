from fastapi import FastAPI

# imports de rota
from mod_funcionario import FuncionarioDAO
from mod_cliente import ClienteDAO
from mod_produto import ProdutoDAO

# imports de modelos
from mod_funcionario.FuncionarioModel import FuncionarioDB
from mod_cliente.ClienteModel import ClienteDB
from mod_produto.ProdutoModel import ProdutoDB

import db

app = FastAPI()

app.include_router(FuncionarioDAO.router)
app.include_router(ClienteDAO.router)
app.include_router(ProdutoDAO.router)

db.criarTabelas()
