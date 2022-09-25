
import tkinter as tk
from tkinter import Button, Entry, Frame, Label, PhotoImage, Place, ttk
from tkinter import messagebox
import datetime as td
from tkinter import *  #  Import window control 
from tkinter import ttk
from view import *
import copy
global tabela
global tabela1
global mostrar_tabela2
#tela
janela = tk.Tk()
janela.title("Ave Maria-Cadastro de Clientes")
janela.geometry("1368x720+0+0")
janela.resizable(width=True, height=True)
janela.minsize(1366,768)
janela.state("zoomed")
janela['bg'] = '#ffffff'#definindo background
janela.iconbitmap(r"C:\Users\Evandro Vieira\OneDrive\Área de Trabalho\AveMaria\AveMaria-env\imagens\icone.ico")
#divisão tela em 3 
frame_cima = Frame(janela, bg="#ffffff",width=1368,height= 300,borderwidth=0,relief='flat')
frame_cima.place(x=0,y=0)
frame_esquerda = Frame(janela, bg="#ffffff",width=685,height= 468,borderwidth=0,relief='flat')
frame_esquerda.place(x=0,y=300)
frame_direita = Frame(janela, bg="#ffffff",width=685,height= 468,borderwidth=0,relief='flat')
frame_direita.place(x=684,y=300)
cadastro_label = tk.Label(janela,text="    Cadastro de Clientes",fg="#cda352",bg="#ffffff",font=('Verdana 40  italic'))
cadastro_label.place(x=0,y=50)
tabela_de_clientes  = Label(janela,text="Ultimos Clientes Cadastrados: ",fg="#cda352",bg="#ffffff",font=('Verdana 20  italic'))
tabela_de_clientes.place(x=150,y=450)
img = PhotoImage(file=r'C:\Users\Evandro Vieira\OneDrive\Área de Trabalho\AveMaria\AveMaria-env\imagens\avemaria.png')
imagem_label = Label(janela, image=img,border=0,width=500,)
imagem_label.place(x=750, y=0)
#formulario dados
nome_label = Label(text="|Nome: *",bg="#ffffff",fg="#cda352",font=('Verdana 20  italic'))
nome_label.place(x=20,y=150)
cpf_rg_label = Label(text="|Cpf ou RG: ",bg="#ffffff",fg="#cda352",font=('Verdana 20  italic'))
cpf_rg_label.place(x=20,y=190)
email_label = Label(text="|Email: ",bg="#ffffff",fg="#cda352",font=('Verdana 20  italic'))
email_label.place(x=20,y=230)
telefone_label = Label(text="|Telefone: ",bg="#ffffff",fg="#cda352",font=('Verdana 20  italic'))
telefone_label.place(x=20,y=270)
estado_label = Label(text="|Estado: ",bg="#ffffff",fg="#cda352",font=('Verdana 20  italic'))
estado_label.place(x=455,y=270)
cidade_label = Label(text="|Cidade: ",bg="#ffffff",fg="#cda352",font=('Verdana 20  italic'))
cidade_label.place(x=20,y=310) 
cep_label = Label(text="|Cep: ",bg="#ffffff",fg="#cda352",font=('Verdana 20  italic'))
cep_label.place(x=455,y=310)
logradouro_label = Label(text="|Logradouro: ",bg="#ffffff",fg="#cda352",font=('Verdana 20  italic'))
logradouro_label.place(x=20,y=350)
bairro_label = Label(text="|Bairro: ",bg="#ffffff",fg="#cda352",font=('Verdana 20  italic'))
bairro_label.place(x=410,y=350)
numero_label = Label(text="|N°: ",bg="#ffffff",fg="#cda352",font=('Verdana 20  italic'))
numero_label.place(x=20,y=390)
obs_label = Label(text="|Observações: ",bg="#ffffff",fg="#cda352",font=('Verdana 20  italic'))
obs_label.place(x=150,y=390)

#entrada de dados
nome_entry = Entry(width=29,fg="#cda352",font=('Verdana 20  italic'),relief='solid')
nome_entry.place(x = 200, y=150)
cpf_rg_entry = Entry(width=29,fg="#cda352",font=('Verdana 20  italic'),relief='solid')
cpf_rg_entry.place(x = 200, y=190)
email_entry = Entry(width=29,fg="#cda352",font=('Verdana 20  italic'),relief='solid')
email_entry.place(x = 200, y=230)
telefone_entry = Entry(width=15,fg="#cda352",font=('Verdana 20  italic'),relief='solid')
telefone_entry.place(x = 200, y=270)
#data cadastro
data_datetime = td.datetime.now().date()
estado_entry = Entry(width=7,fg="#cda352",font=('Verdana 20  italic'),relief='solid')
estado_entry.place(x =575, y=270)
cidade_entry = Entry(width=15,fg="#cda352",font=('Verdana 20  italic'),relief='solid')
cidade_entry.place(x = 200, y=310)
cep_entry = Entry(width=9,fg="#cda352",font=('Verdana 20  italic'),relief='solid')
cep_entry.place(x = 540, y=310)
logradouro_entry = Entry(width=12,fg="#cda352",font=('Verdana 20  italic'),relief='solid')
logradouro_entry.place(x = 200, y=350)
bairro_entry = Entry(width=10,fg="#cda352",font=('Verdana 20  italic'),relief='solid')
bairro_entry.place(x = 525, y=350)
numero_entry = Entry(width=3,fg="#cda352",font=('Verdana 20  italic'),relief='solid')
numero_entry.place(x = 90, y=390)
obs_entry = Entry(width=20,fg="#cda352",font=('Verdana 20  italic'),relief='solid')
obs_entry.place(x = 355, y=390)

pesquisar_entry = Entry(width=15,fg="#cda352",font=('Verdana 32  italic'),relief='solid')
pesquisar_entry.place(x=910,y=430)
#lembrar de fazer cadastro pela data

# botão inserir 
def botao_inserir():
    nome = nome_entry.get()
    cpf_rg = cpf_rg_entry.get()
    email = email_entry.get()
    telefone = telefone_entry.get()
    data = data_datetime
    estado = estado_entry.get()
    cidade = cidade_entry.get()
    cep = cep_entry.get()
    logradouro = logradouro_entry.get()
    bairro = bairro_entry.get()
    numero = numero_entry.get()
    obs = obs_entry.get()
    lista = [nome,cpf_rg,email,telefone,data,estado,cidade,cep,logradouro,bairro,numero,obs]
    if nome == '':
        messagebox.showerror('Erro', 'Nome obrigatorio')
    elif telefone == '':
        messagebox.showerror('Erro', 'Numero de telefone obrigatorio')
    else:
        inserir_dados(lista)
        messagebox.showinfo("Sucesso", "Os dados foram inseridos com sucesso!")
        nome_entry.delete(0,'end')
        cpf_rg_entry.delete(0,'end')
        email_entry.delete(0,'end')
        telefone_entry.delete(0,'end')
        estado_entry.delete(0,'end')
        cidade_entry.delete(0,'end')
        cep_entry.delete(0,'end')
        logradouro_entry.delete(0,'end')
        bairro_entry.delete(0,'end')
        numero_entry.delete(0,'end')
        obs_entry.delete(0,'end')
        try:
            mostrar_tabela()
        except NameError as e:
            mostrar_tabela2()
            messagebox.showerror('Erro', 'Tabela')
        
#botão atualizar ensar sobre resolver problema 
global botao_atualizar
def botao_atualizar():
        try:
            tabela_dados =  tabela.focus()
            tabela_dicionario = tabela.item(tabela_dados)
            tabela_lista = tabela_dicionario['values']
            valor = tabela_lista[0]
            nome_entry.delete(0,'end')
            cpf_rg_entry.delete(0,'end')
            email_entry.delete(0,'end')
            telefone_entry.delete(0,'end')
            estado_entry.delete(0,'end')
            cidade_entry.delete(0,'end')
            cep_entry.delete(0,'end')
            logradouro_entry.delete(0,'end')
            bairro_entry.delete(0,'end')
            numero_entry.delete(0,'end')
            obs_entry.delete(0,'end')

            nome_entry.insert(0,tabela_lista[1])
            cpf_rg_entry.insert(0,tabela_lista[2])
            email_entry.insert(0,tabela_lista[3])
            telefone_entry.insert(0,tabela_lista[4])
            estado_entry.insert(0,tabela_lista[6])
            cidade_entry.insert(0,tabela_lista[7])
            cep_entry.insert(0,tabela_lista[8])
            logradouro_entry.insert(0,tabela_lista[9])
            bairro_entry.insert(0,tabela_lista[10])
            numero_entry.insert(0,tabela_lista[11])
            obs_entry.insert(0,tabela_lista[12])
            
            def atualizar():
                nome = nome_entry.get()
                cpf_rg = cpf_rg_entry.get()
                email = email_entry.get()
                telefone = telefone_entry.get()
                data = data_datetime
                estado = estado_entry.get()
                cidade = cidade_entry.get()
                cep = cep_entry.get()
                logradouro = logradouro_entry.get()
                bairro = bairro_entry.get()
                numero = numero_entry.get()
                obs = obs_entry.get()
                lista = [nome,cpf_rg,email,telefone,data,estado,cidade,cep,logradouro,bairro,numero,obs,valor]
                if nome == '':
                    messagebox.showerror('Erro', 'Nome obrigatorio')
                else:
                    atualizar_cadastro(lista)
                    messagebox.showinfo("Sucesso", "Os dados foram atualizados com sucesso!")
                    nome_entry.delete(0,'end')
                    cpf_rg_entry.delete(0,'end')
                    email_entry.delete(0,'end')
                    telefone_entry.delete(0,'end')
                    estado_entry.delete(0,'end')
                    cidade_entry.delete(0,'end')
                    cep_entry.delete(0,'end')
                    logradouro_entry.delete(0,'end')
                    bairro_entry.delete(0,'end')
                    numero_entry.delete(0,'end')
                    obs_entry.delete(0,'end')
                    confirmar_button.destroy()
                    tabela.destroy()
                    try:
                        mostrar_tabela()
                    except NameError as e:
                        mostrar_tabela2()
                        messagebox.showerror('Erro', 'Tabela')

                
            confirmar_button = Button(text="Confirmar",command=atualizar,fg="#cda352", bg="#ffffff",font=('Verdana 20  italic'),relief='groove',border=2)
            confirmar_button.place(x=835,y=360)
            
        except IndexError as e:
            messagebox.showerror('Erro','Seleciona um item da tabela')
global botao_atualizar_tabela2
def botao_atualizar_tabela2():
        try:
            tabela_dados =  tabela1.focus()
            tabela_dicionario = tabela1.item(tabela_dados)
            tabela_lista = tabela_dicionario['values']
            valor = tabela_lista[0]
            nome_entry.delete(0,'end')
            cpf_rg_entry.delete(0,'end')
            email_entry.delete(0,'end')
            telefone_entry.delete(0,'end')
            estado_entry.delete(0,'end')
            cidade_entry.delete(0,'end')
            cep_entry.delete(0,'end')
            logradouro_entry.delete(0,'end')
            bairro_entry.delete(0,'end')
            numero_entry.delete(0,'end')
            obs_entry.delete(0,'end')

            nome_entry.insert(0,tabela_lista[1])
            cpf_rg_entry.insert(0,tabela_lista[2])
            email_entry.insert(0,tabela_lista[3])
            telefone_entry.insert(0,tabela_lista[4])
            estado_entry.insert(0,tabela_lista[6])
            cidade_entry.insert(0,tabela_lista[7])
            cep_entry.insert(0,tabela_lista[8])
            logradouro_entry.insert(0,tabela_lista[9])
            bairro_entry.insert(0,tabela_lista[10])
            numero_entry.insert(0,tabela_lista[11])
            obs_entry.insert(0,tabela_lista[12])
            
            def atualizar():
                nome = nome_entry.get()
                cpf_rg = cpf_rg_entry.get()
                email = email_entry.get()
                telefone = telefone_entry.get()
                data = data_datetime
                estado = estado_entry.get()
                cidade = cidade_entry.get()
                cep = cep_entry.get()
                logradouro = logradouro_entry.get()
                bairro = bairro_entry.get()
                numero = numero_entry.get()
                obs = obs_entry.get()
                lista = [nome,cpf_rg,email,telefone,data,estado,cidade,cep,logradouro,bairro,numero,obs,valor]
                if nome == '':
                    messagebox.showerror('Erro', 'Nome obrigatorio')
                else:
                    atualizar_cadastro(lista)
                    messagebox.showinfo("Sucesso", "Os dados foram atualizados com sucesso!")
                    nome_entry.delete(0,'end')
                    cpf_rg_entry.delete(0,'end')
                    email_entry.delete(0,'end')
                    telefone_entry.delete(0,'end')
                    estado_entry.delete(0,'end')
                    cidade_entry.delete(0,'end')
                    cep_entry.delete(0,'end')
                    logradouro_entry.delete(0,'end')
                    bairro_entry.delete(0,'end')
                    numero_entry.delete(0,'end')
                    obs_entry.delete(0,'end')
                    confirmar_button.destroy()
                    
                    try:
                        mostrar_tabela()
                    except NameError as e:
                        mostrar_tabela2()
                        messagebox.showerror('Erro', 'Tabela')

                
            confirmar_button = Button(text="Confirmar",command=atualizar,fg="#cda352", bg="#ffffff",font=('Verdana 20  italic'),relief='groove',border=2)
            confirmar_button.place(x=835,y=360)
        except IndexError as e:
            messagebox.showerror('Erro','Seleciona um item da tabela')

def botao_deletar():
    try:
        tabela_dados = tabela.focus()
        tabela_dicionario = tabela.item(tabela_dados)
        tabela_lista = tabela_dicionario['values']
        valor = [tabela_lista[0]]
        deletar_cadastro(valor)
        messagebox.showinfo("Sucesso", "Os dados foram excluidos com sucesso!")
        tabela.destroy()
        try:
            mostrar_tabela()
        except NameError as e:
            mostrar_tabela2()
            messagebox.showerror('Erro', 'Tabela')
        
        

    except IndexError as e:
        messagebox.showerror("Erro","Selecione um dos itens da tabela")
global botao_deletar_tabela2
def botao_deletar_tabela2():
    try:
        tabela_dados = tabela1.focus()
        tabela_dicionario = tabela1.item(tabela_dados)
        tabela_lista = tabela_dicionario['values']
        valor = [tabela_lista[0]]
        deletar_cadastro(valor)
        messagebox.showinfo("Sucesso", "Os dados foram excluidos com sucesso!")
        tabela.destroy()
        try:
            mostrar_tabela()
        except NameError as e:
            mostrar_tabela2()
            messagebox.showerror('Erro', 'Tabela')
        
        

    except IndexError as e:
        messagebox.showerror("Erro","Selecione um dos itens da tabela")

def botao_pesquisar():
    
        lista = pesquisar_cadastro(pesquisar_entry.get())
        janela1 = Toplevel()
        largura1 = janela1.winfo_screenwidth()
        altura1 = janela1.winfo_screenheight()
        largura = 800
        altura = 600
        posx = largura1/2 - (largura/2)
        posy = altura1/2 - (altura/2)
        janela1.geometry("%dx%d+%d+%d"%(largura,altura,posx,posy))
        janela1.resizable(width=False, height=False)
        janela1['bg'] = '#ffffff'#definindo background
        janela1.title("Ave-Maria Pesquisa")
        janela1.iconbitmap(r"C:\Users\Evandro Vieira\OneDrive\Área de Trabalho\AveMaria\AveMaria-env\imagens\icone.ico")
        pesquisar = tk.Label(janela1,text="Pesquisa 🔎",fg="#cda352",bg="#ffffff",font=('Verdana 40  italic'))
        pesquisar.place(x=250,y=20)
        atualizar_button1 = Button(janela1,text="Atualizar",command=botao_atualizar_tabela2,fg="#cda352", bg="#ffffff",font=('Verdana 20  italic'),relief='groove',border=2)
        atualizar_button1.place(x=150,y=130)
        excluir_button1 = Button(janela1,text="Excluir",command=botao_deletar_tabela2,fg="#cda352", bg="#ffffff",font=('Verdana 20  italic'),relief='groove',border=2,)
        excluir_button1.place(x=480,y=130)
        global mostrar_tabela2
        def mostrar_tabela2():
            global tabela1
            lista = pesquisar_cadastro(pesquisar_entry.get())
            pesquisar_entry.delete(0,'end')
            tabela1 = ttk.Treeview(janela1,columns=('id','nome','cpf_rg','email','telefone','data',
            'estado','cidade','cep','logradouro','bairro','numero','observacoes'),show='headings',selectmode='extended')
            tabela1.column('id',minwidth=0,width=15) 
            tabela1.column('nome',minwidth=0,width=75) 
            tabela1.column('cpf_rg',minwidth=0,width=75) 
            tabela1.column('email',minwidth=0,width=75) 
            tabela1.column('telefone',minwidth=0,width=50) 
            tabela1.column('data',minwidth=0,width=50) 
            tabela1.column('estado',minwidth=0,width=25) 
            tabela1.column('cidade',minwidth=0,width=75) 
            tabela1.column('cep',minwidth=0,width=50) 
            tabela1.column('logradouro',minwidth=0,width=50) 
            tabela1.column('bairro',minwidth=0,width=25) 
            tabela1.column('numero',minwidth=0,width=20) 
            tabela1.column('observacoes',minwidth=0,width=50) 
            tabela1.heading('id', text='ID')
            tabela1.heading('nome', text='Nome')
            tabela1.heading('cpf_rg', text='Cpf ou RG')
            tabela1.heading('email', text='Email')
            tabela1.heading('telefone', text='Telefone')
            tabela1.heading('data', text='Data')
            tabela1.heading('estado', text='Estado')
            tabela1.heading('cidade', text='Cidade')
            tabela1.heading('cep', text='Cep')
            tabela1.heading('logradouro', text='Logradouro')
            tabela1.heading('bairro', text='Bairro')
            tabela1.heading('numero', text='Numero')
            tabela1.heading('observacoes', text='Observações')
            
            for (id, nome, cpf_rg, email,telefone, data,
                    estado, cidade, cep, logradouro, bairro, numero, observacoes) in lista:
                    tabela1.insert("",-1, values=(id, nome, cpf_rg, email,telefone, data,
                    estado, cidade, cep, logradouro, bairro, numero, observacoes))
            
            # centralizar tela
            
            tabela1.place(x=0,y=200,bordermode="inside",width=800,height=400)
            scroll_bar = tk.Scrollbar(tabela,orient=VERTICAL,command=tabela1.yview,width=15,)
            tabela1.configure(yscroll=scroll_bar.set,)
            scroll_bar.pack(side=RIGHT, fill=Y,)
            
        try:
            mostrar_tabela()
        except NameError as e:
            mostrar_tabela2()
            messagebox.showerror('Erro', 'Tabela')
        finally:
            mostrar_tabela2()


# botoes
inserir_button = Button(text="Inserir",command=botao_inserir,fg="#cda352",bg="#ffffff",font=('Verdana 20  italic'),relief='groove',border=2)
inserir_button.place(x=720,y=360)
atualizar_button = Button(text="Atualizar",command=botao_atualizar,fg="#cda352", bg="#ffffff",font=('Verdana 20  italic'),relief='groove',border=2,)
atualizar_button.place(x=840,y=360)
excluir_button = Button(text="Excluir",command=botao_deletar,fg="#cda352", bg="#ffffff",font=('Verdana 20  italic'),relief='groove',border=2,)
excluir_button.place(x=989,y=360)
exportar_button = Button(text="Exportar Excel",fg="#cda352", bg="#ffffff",font=('Verdana 20  italic'),relief='groove',border=2)
exportar_button.place(x=1109,y=360)
pesquisar_button = Button(text="Pesquisar🔎",command=botao_pesquisar,fg="#cda352", bg="#ffffff",font=('Verdana 20  italic'),relief='groove',border=2)
pesquisar_button.place(x=720,y=430)


######################## CODIGO TABELA #######################



def mostrar_tabela():
    global tabela
    lista = acessar_dados()
    tabela = ttk.Treeview(janela,columns=('id','nome','cpf_rg','email','telefone','data',
    'estado','cidade','cep','logradouro','bairro','numero','observacoes'),show='headings',selectmode='extended')
    tabela.column('id',minwidth=0,width=30) 
    tabela.column('nome',minwidth=0,width=150) 
    tabela.column('cpf_rg',minwidth=0,width=150) 
    tabela.column('email',minwidth=0,width=150) 
    tabela.column('telefone',minwidth=0,width=100) 
    tabela.column('data',minwidth=0,width=100) 
    tabela.column('estado',minwidth=0,width=50) 
    tabela.column('cidade',minwidth=0,width=150) 
    tabela.column('cep',minwidth=0,width=100) 
    tabela.column('logradouro',minwidth=0,width=100) 
    tabela.column('bairro',minwidth=0,width=50) 
    tabela.column('numero',minwidth=0,width=40) 
    tabela.column('observacoes',minwidth=0,width=100) 
    tabela.heading('id', text='ID')
    tabela.heading('nome', text='Nome')
    tabela.heading('cpf_rg', text='Cpf ou RG')
    tabela.heading('email', text='Email')
    tabela.heading('telefone', text='Telefone')
    tabela.heading('data', text='Data')
    tabela.heading('estado', text='Estado')
    tabela.heading('cidade', text='Cidade')
    tabela.heading('cep', text='Cep')
    tabela.heading('logradouro', text='Logradouro')
    tabela.heading('bairro', text='Bairro')
    tabela.heading('numero', text='Numero')
    tabela.heading('observacoes', text='Observações')
    
    for (id, nome, cpf_rg, email,telefone, data,
            estado, cidade, cep, logradouro, bairro, numero, observacoes) in lista:
            tabela.insert("",-1, values=(id, nome, cpf_rg, email,telefone, data,
            estado, cidade, cep, logradouro, bairro, numero, observacoes))
    
    
    tabela.place(x=0,y=500,bordermode="inside",width=1360,height=200)
    scroll_bar = tk.Scrollbar(tabela,orient=VERTICAL,command=tabela.yview,width=15,)
    tabela.configure(yscroll=scroll_bar.set,)
    scroll_bar.pack(side=RIGHT, fill=Y,)


mostrar_tabela()
janela.mainloop()