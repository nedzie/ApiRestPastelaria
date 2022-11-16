from fastapi import FastAPI, Depends

# imports de rota
from mod_funcionario import FuncionarioDAO
from mod_cliente import ClienteDAO
from mod_produto import ProdutoDAO

import db
import security

app = FastAPI(dependencies=[Depends(
    security.verify_token), Depends(security.verify_key)])

app.include_router(FuncionarioDAO.router)
app.include_router(ClienteDAO.router)
app.include_router(ProdutoDAO.router)

db.criarTabelas()
