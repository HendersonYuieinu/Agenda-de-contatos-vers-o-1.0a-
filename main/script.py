from database.scriptDB import Session, contato, telefone, email
from sqlalchemy import exc
import flet as ft

#funcao para adicionar o contato (nome, sobrenome e nota)
def addContato(nome, sobrenome, nota=""):
    try:                                                                    #caso nao ocorrer um erro, deve executar
        with Session() as session:                                              #abrir o Session e fechar ele após o termino da ação.
            newcontato = contato(nome=nome, sobrenome=sobrenome, nota=nota)         #instanciando um objeto com a classe da tabela
            session.add(newcontato)                                                 #criando uma sessao para adicionar o objeto na tabela dentro do banco de dados
            session.commit()                                                        #enviando as informações da sessão
            return newcontato.id                                                             #caso ocorra tudo certo, retornar True
    except Exception as error:                                              #caso ocorra um error, deve executar
        print(f'Error adding {nome}, {sobrenome}, {error}')                     #executa uma mensagem informando o erro.
        return False
    
#funcao para adicionar o telefone do contato (chave estrangeira do contato e numero de telefone(obrigatorio))
def addTelefone(id_contato, numero):
    try:    
        with Session() as session:
            newtelefone = telefone(id_contato = id_contato, numero=numero)
            session.add(newtelefone)
            session.commit()
            return True
    except Exception as error:
        print(f'Error adding {id_contato}, {numero}, {error}')
        if isinstance(error, exc.IntegrityError):                           #caso ocorra um erro da instancia, identificado pelo sqlalchemy, deve informar o erro                       
            print("Error details: Integrity Violation of data base (ex:foreign key not exist or null datas)") #nesse caso é quando o dado informado é nulo, já que o numero é um campo obrigatorio not null
        return False

#funcao para adicionar o telefone do contato (chave estrangeira do contato e endereco do email)
def addEmail(id_contato, endereco):
    try:    
        with Session() as session:
            newemail = email(id_contato = id_contato, endereco=endereco)
            session.add(newemail)
            session.commit()
            return True
    except Exception as error:
        print(f'Error adding {id_contato}, {endereco}, {error}')
        return False

def editContato(id_contato, nome, sobrenome, nota):
    try:
        with Session() as session:
            contato_to_edit = session.query(contato).filter(contato.id == id_contato).first()
            
            contato_to_edit.nome = nome
            contato_to_edit.sobrenome = sobrenome
            contato_to_edit.nota = nota
            session.commit()
            return True
    except Exception as error:
        print(f'Error editing contato with id {id_contato}: {error}')
        return False

def editTelefone(id_contato, numero):
    try:
        with Session() as session:
            telefone_to_edit = session.query(telefone).filter(telefone.id_contato == id_contato).first()
            telefone_to_edit.numero = numero
            session.commit()
            return True
    except Exception as error:
        print(f'Error editing telefone with id contat {id_contato}: {error}')
        return False

def editEmail(id_contato, endereco):
    try:
        with Session() as session:
            email_to_edit = session.query(email).filter(email.id_contato == id_contato).first()
            email_to_edit.endereco = endereco
            session.commit()
            return True
    except Exception as error:
        print(f'Error editing email with id {id_contato}: {error}')
        return False

def GetContatos():
    try:
        with Session() as session:
            Contatos = session.query(contato).all()
            return Contatos
    except Exception as error:
        print(f'Erro ao pegar os contatos da tabela.')


def GetEmails():
    try:
        with Session() as session:
            Emails = session.query(email).all()
            return Emails
    except Exception as error:
        print(f'Erro ao pegar os Emails da tabela.')


def GetTelefones():
    try:
        with Session() as session:
            Telefones = session.query(telefone).all()
            return Telefones
    except Exception as error:
        print(f'Erro ao pegar os Telefones da tabela.')

#funçao para pegar todos os dados e organizar eles para usar no App_run.py
def Getall(): 
    try:
        dadoscompletos = []
        contatos = GetContatos()
        telefones = GetTelefones()
        emails = GetEmails()
        
        telefonesDIC = {} #cria um dicionario para os telefones
        for tel in telefones:
            telefonesDIC.setdefault(tel.id_contato, []).append(tel.numero)
        
        emailsDIC = {} #cria um dicionario para os emails
        for em in emails:
            emailsDIC.setdefault(em.id_contato, []).append(em.endereco)
            
        for c in contatos: #cria um dicionario para os contatos, tendo todas as informaçoes
            contatosDIC = {
                "id_contato" : c.id,
                "nome": c.nome,
                "sobrenome": c.sobrenome,
                "nota": c.nota,
                "telefone": telefonesDIC.get(c.id, []),
                "email": emailsDIC.get(c.id, [])
            }
            dadoscompletos.append(contatosDIC)
        return dadoscompletos #retorna os dados
    except Exception as e:
        print(f'ERROR to load data from database: {e}')
        return []

def DeleteContato(id_contato): #funcao para deleter o contato incluindo o telefone e email associado a ele.
    try:
        with Session() as session:
            contato_to_delete = session.query(contato).filter(contato.id == id_contato)            #filtra o contato pelo id
            telefone_to_delete = session.query(telefone).filter(telefone.id_contato == id_contato) #.
            email_to_delete = session.query(email).filter(email.id_contato == id_contato)          #.
            
            contato_to_delete.delete()  #deleta o contato                                          #chama a funcao que deleta o item da base de dados
            telefone_to_delete.delete() #deleta o telefone associado ao contato                    #.
            email_to_delete.delete()    #deleta o email associado ao contato                       #.

            session.commit()
            
    
    except Exception as error:
        print(f'Error deleting contato with id {id_contato}: {error}')
    


#funcao para criar o card com o contato
def create_card(dados_completos, on_delete, on_edit=None):
    # Lógica para formatar telefone e email para o subtítulo
    telefone_exibir = dados_completos["telefone"][0] if dados_completos["telefone"] else "N/A"
    email_exibir = dados_completos["email"][0] if dados_completos["email"] else "N/A"
    
    botao_delete = ft.IconButton(icon=ft.Icons.DELETE, icon_color=ft.Colors.RED, icon_size=30, tooltip="Apagar")
    botao_edit = ft.IconButton(ft.Icons.EDIT, icon_color=ft.Colors.BLUE, icon_size=30, tooltip="Editar")
    
    card = ft.Card(
        content=ft.Container(
            content=ft.Column(
                [
                    ft.ListTile(
                        leading=ft.Icon(ft.Icons.PERSON_ROUNDED,size=40),
                        title=ft.Text(f'{("Sem nome" if dados_completos["nome"] == "" else dados_completos["nome"])} {dados_completos['sobrenome']}', selectable=True, weight="bold", width=200, no_wrap=False),
                        subtitle=ft.Column([ft.Text(f'{telefone_exibir}', selectable=True), ft.Text(f'{email_exibir}', selectable=True, no_wrap=False)], spacing=0.5),

                    ),
                    ft.Row(
                        controls=[
                            ft.Row([ft.Text(f'{dados_completos['nota']}', width=230, no_wrap=False, selectable=True)],alignment=ft.MainAxisAlignment.START),
                            ft.Row(
                                [botao_delete, botao_edit],
                                alignment=ft.MainAxisAlignment.END,
                            )
                        ], spacing=80
                        
                    )
                ],
                spacing=0,
            ),
            width=430,
            border_radius=10,
            padding=10,
            alignment=ft.alignment.center,
        ),
        shadow_color=ft.Colors.ON_SURFACE_VARIANT
    )
    botao_delete.on_click = lambda e: on_delete(dados_completos["id_contato"])
    botao_edit.on_click = lambda e: on_edit(dados_completos) if on_edit else None
    
    return card