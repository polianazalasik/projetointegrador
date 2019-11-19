import os
from peewee import *

arq = "pessoa.db" 
db = SqliteDatabase(arq)

class BaseModel(Model):
    class Meta:
        database = db

class Pessoa(BaseModel):
    nome = CharField()
    dia = CharField()
    mes = CharField()
    ano = CharField()
    rg = CharField()
    cpf = CharField()
    rua = CharField()
    numero = CharField()
    bairro = CharField()
    estado = CharField()
    cidade = CharField()
    cep = CharField()
    email = CharField()
    login = CharField()
    passs = CharField()
    passconfirm = CharField()

db.connect()
db.create_tables([Pessoa])




        