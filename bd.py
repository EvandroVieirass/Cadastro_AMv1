# importando Sqlite
import sqlite3 as lite

# criando conexão
# con de conexão
con = lite.connect(r'C:\Users\Evandro Vieira\OneDrive\Área de Trabalho\AveMaria\AveMaria-env\banco.db')
# Criando tabela
with con:
    cur = con.cursor()
    cur.execute("CREATE TABLE formulario (id INTEGER PRIMARY KEY AUTOINCREMENT, nome TEXT, cpf_rg Text,email TEXT, telefone TEXT, data_cadastro DATE, estado TEXT, cidade TEXT,cep TEXT,logradouro Text,bairro Text,numero Text, obs TEXT)")
