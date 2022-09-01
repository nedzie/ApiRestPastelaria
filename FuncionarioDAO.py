from fastapi import APIRouter
from pydantic import BaseModel

class Funcionario(BaseModel):
  codigo: int = None #Não obrigatório
  nome: str
  matricula: str
  cpf: str
  telefone: str = None
  grupo: int
  senha: str = None

router = APIRouter()

# Criar os 'endpoints' de Funcionario: GET, POST, PUT, DELETE
# Enviar dados: POST, PUT, DELETE OU PATCH
# Não se deve pôr corpo no método GET

@router.get("/funcionario/{id}", tags=["funcionario"])
def get_funcionario(id: int):
  return {"msg": "get executado", "id": id}, 200

@router.post("/funcionario/{id}", tags=["funcionario"])
def post_funcionario(id: int, f: Funcionario):
  return {"msg": "post executado", "id": id, "nome": f.nome, "cpf": f.cpf, "telefone": f.telefone}, 200

@router.put("/funcionario/{id}", tags=["funcionario"])
def put_funcionario(id: int, f: Funcionario):
  return {"msg": "put executado", "id": id, "nome": f.nome, "cpf": f.cpf, "telefone": f.telefone}, 201

@router.delete("/funcionario/{id}", tags=["funcionario"])
def delete_funcionario(id: int):
  return {"msg": "delete executado", "id": id}, 201