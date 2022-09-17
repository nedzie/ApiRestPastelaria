from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

STR_DB = "sqlite:///pastelaria_db.db"

# Criando conexão com o SQLite
engine = create_engine(STR_DB, future=True)
# echo=True irá mostrar os comandos executados, no console

# O objeto que irá que envia comandos para o banco
Session = sessionmaker(bind=engine, future=True)

# O objeto que irá criar os modelos
Base = declarative_base()


# Criará todas as tabelas caso não hajam
def criarTabelas():
    Base.metadata.create_all(engine)
