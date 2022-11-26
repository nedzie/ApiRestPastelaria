from fastapi import APIRouter
from pydantic import BaseModel

# Imports de persistência
import db
from mod_funcionario.FuncionarioModel import FuncionarioDB


class Funcionario(BaseModel):
    codigo: int = None  # Não obrigatório
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

# selecionarTodos()


@router.get("/funcionario/", tags=["funcionario"])
def get_funcionario():
    try:
        session = db.Session()
        # Query para selecionar todos os dados
        dados = session.query(FuncionarioDB).all()
        return dados, 200  # Retorna em JSON
    except Exception as e:
        # Informações do erro + código 404
        return {"msg": "Erro ao listar", "erro": str(e)}, 404
    finally:
        session.close()


@router.post("/teste/", tags=["teste"])
def validar_login(cpf: str, senha: str):
    print(cpf, senha)
    session = db.Session()

    ehValido: bool = False

    x = session.query(FuncionarioDB).filter(
        (FuncionarioDB.cpf == cpf)).filter(FuncionarioDB.senha == senha).first()

    if x is not None:
        ehValido = True

    if ehValido:
        return 1, x, 200
    else:
        return 0, 200


# selecionarPorId()
@router.get("/funcionario/{id}", tags=["funcionario"])
def get_funcionario_id(id: int):
    try:
        session = db.Session()
        # Query para buscar por id
        dados = session.query(FuncionarioDB).filter(
            FuncionarioDB.id_funcionario == id).all()
        return dados, 200
    except Exception as e:
        return {"msg": "Erro ao listar", "erro": str(e)}, 404
    finally:
        session.close()


# inserir()
@router.post("/funcionario/", tags=["funcionario"])
def post_funcionario(corpo: Funcionario):
    try:
        session = db.Session()

        dados = FuncionarioDB(None, corpo.nome, corpo.matricula,
                              corpo.cpf, corpo.telefone, corpo.grupo, corpo.senha)

        session.add(dados)

        session.commit()

        return {"msg": "Cadastrado com sucesso", "id": dados.id_funcionario}, 200

    except Exception as e:
        session.rollback()
        return {"msg": "Erro ao cadastrar", "erro": str(e)}, 406

    finally:
        session.close()


# editar()
@router.put("/funcionario/{id}", tags=["funcionario"])
def put_funcionario(id: int, corpo: Funcionario):
    try:
        session = db.Session()
        dados = session.query(FuncionarioDB).filter(
            FuncionarioDB.id_funcionario == id).one()

        dados.nome = corpo.nome
        dados.cpf = corpo.cpf
        dados.telefone = corpo.telefone
        dados.senha = corpo.senha
        dados.matricula = corpo.matricula
        dados.grupo = corpo.grupo

        session.add(dados)
        session.commit()

        return {"msg": "Editado com sucesso", "id": dados.id_funcionario}, 201

    except Exception as e:
        session.rollback()
        return {"msg": "Erro ao editar", "erro": str(e)}, 406

    finally:
        session.close()


# excluir()
@router.delete("/funcionario/{id}", tags=["funcionario"])
def delete_funcionario(id: int):
    try:
        session = db.Session()

        dados = session.query(FuncionarioDB).filter(
            FuncionarioDB.id_funcionario).one()
        session.delete(dados)
        session.commit()

        return {"msg": "Excluído com sucesso", "id": dados.id_funcionario}, 201
    except Exception as e:
        session.rollback()
        return {"msg": "Erro ao excluir", "erro": str(e)}, 406

    finally:
        session.close()
