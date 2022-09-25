import sqlite3 as lite
#conexão banco de dados
con = lite.connect('banco.db')
lista = ['Evandro Vieria','03777990094','evandro@gmail.com','51995803465',
    '20/09/2022','Rs','Gramado','95670000','Faustino Rissi','Varzea Grande', '820','Morador da Cidade']
#inserir dados 
def inserir_dados(lista):
    with con :
        cur = con.cursor()
        query = "INSERT INTO formulario(nome, cpf_rg, email, telefone, data_cadastro, estado, cidade, cep, logradouro, bairro, numero, obs) VALUES(?,?,?,?,?,?,?,?,?,?,?,?)"
        cur.execute(query,lista)

#acessar informações banco de dados
def acessar_dados():
    lista = []
    with con :
        cur = con.cursor()
        query = "SELECT * FROM formulario"
        cur.execute(query)
        dados = cur.fetchall()
        
        for dado in dados:
            lista.append(dado)
        return lista

def atualizar_cadastro(lista):
#atualizar cadastro
    with con :
        cur = con.cursor()
        query = "UPDATE formulario SET nome=?, cpf_rg=?, email=?, telefone=?, data_cadastro=?, estado=?, cidade=?, cep=?, logradouro=?, bairro=?, numero=?, obs=? WHERE id=?"
        cur.execute(query,lista)

#deletar cadastro
def deletar_cadastro(id):
    with con :

        cur = con.cursor()
        query = "DELETE FROM formulario WHERE id=?"
        cur.execute(query,id)

#pesquisar

def pesquisar_cadastro(i):
    cur = con.cursor()
    #colocar todos os campos para pesquisar
                                                                                                                                                                            #(nome, cpf_rg, email, telefone, data_cadastro, estado, cidade, cep, logradouro, bairro, numero, obs)
    query = f"SELECT id,nome,cpf_rg,email,telefone,data_cadastro,estado,cidade,cep, logradouro, bairro, numero, obs FROM formulario WHERE nome LIKE '%{i}%' or  cpf_rg LIKE '%{i}%' or  email LIKE '%{i}%' or telefone LIKE '%{i}%' or  data_cadastro LIKE '%{i}%' or  estado LIKE '%{i}%' or  cidade LIKE '%{i}%' or cep LIKE '%{i}%' or  logradouro LIKE '%{i}%' or  bairro LIKE '%{i}%' or  numero LIKE '%{i}%' or  obs LIKE '%{i}%'"
    cur.execute(query)
    dados = cur.fetchall()
    return dados

def pesquisar_ultimo_usuario():
    cur = con.cursor()
    query = f"SELECT * FROM formulario WHERE id=(SELECT max(id) FROM formulario)"
    cur.execute(query)
    dados = cur.fetchall()
    return dados


