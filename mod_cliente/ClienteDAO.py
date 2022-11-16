from fastapi import APIRouter
from pydantic import BaseModel

import db
from mod_cliente.ClienteModel import ClienteDB


class Cliente(BaseModel):
    codigo: int = None
    nome: str
    cpf: str
    telefone: str
    compra_fiado: int
    dia_fiado: int
    senha: str


router = APIRouter()

# Criar os 'endpoints' de cliente: GET, POST, PUT, DELETE


@router.get("/cliente/", tags=["cliente"])
def get_cliente():
    try:
        session = db.Session()
        dados = session.query(ClienteDB).all()
        return dados, 200
    except Exception as e:
        return {"msg": "Erro ao listar", "erro": str(e)}, 404
    finally:
        session.close()


@router.get("/cliente/", tags=["cliente"])
def get_cliente_id(id: int):
    try:
        session = db.Session()
        dados = session.query(ClienteDB).filter(
            ClienteDB.id_cliente == id).all()
        return dados, 200
    except Exception as e:
        return {"msg": "Erro ao listar", "erro": str(e)}, 404
    finally:
        session.close()


@router.post("/cliente/", tags=["cliente"])
def post_cliente(corpo: Cliente):
    try:
        session = db.Session()

        dados = ClienteDB(None, corpo.nome, corpo.cpf, corpo.telefone,
                          corpo.compra_fiado, corpo.dia_fiado, corpo.senha)

        session.add(dados)
        session.commit()

        return {"msg": "Cadastrado com sucesso", "id": dados.id_cliente}, 200

    except Exception as e:
        session.rollback()
        return {"msg": "Erro ao cadastrar", "erro": str(e)}, 406

    finally:
        session.close()


@router.put("/cliente/{id}", tags=["cliente"])
def put_cliente(id: int, corpo: Cliente):
    try:
        session = db.Session()
        dados = session.query(ClienteDB).filter(
            ClienteDB.id_cliente == id).one()

        dados.nome = corpo.nome
        dados.cpf = corpo.cpf
        dados.telefone = corpo.telefone
        dados.compra_fiado = corpo.compra_fiado
        dados.dia_fiado = corpo.dia_fiado
        dados.senha = corpo.senha

        session.add(dados)
        session.commit()

        return {"msg": "Editado com sucesso", "id": dados.id_cliente}, 201
    except Exception as e:
        session.rollback()
        return {"msg": "Erro ao editar", "erro": str(e)}, 406

    finally:
        session.close()


@router.delete("/cliente/{id}", tags=["cliente"])
def delete_cliente(id: int):
    try:
        session = db.Session()
        dados = session.query(ClienteDB).filter(ClienteDB.id_cliente).one()
        session.delete(dados)
        session.commit()

        return {"msg": "Excluído com sucesso", "id": dados.id_cliente}, 201
    except Exception as e:
        session.rollback()
        return {"msg": "Erro ao excluir", "erro": str(e)}, 406

    finally:
        session.close()
