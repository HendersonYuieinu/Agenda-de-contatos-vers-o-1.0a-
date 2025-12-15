from main.script import addContato, addTelefone, addEmail, Getall, create_card, DeleteContato, editContato, editEmail, editTelefone
import flet as ft
import re

def main(page:ft.Page):
    page.theme_mode = ft.ThemeMode.LIGHT
    page.title = "AGENDA DE CONTATOS"
    page.window.width = 480
    page.window.height = 800
    page.window.maximizable = False
    page.window.resizable = False
    page.horizontal_alignment = ft.MainAxisAlignment.CENTER
    page.window.center()
    page.scroll = True
    
    _id_contato_ = ft.Text("", visible=False)
    campo_nome = ft.TextField(label="Nome", width=350, text_size=24)
    campo_sobrenome = ft.TextField(label="Sobrenome", width=350, text_size=24)
    campo_nota = ft.TextField(label="Nota", width=350, text_size=24)
    campo_telefone = ft.TextField(label="Telefone", width=350, text_size=24)
    campo_email = ft.TextField(label="Email", width=350, text_size=24)
    
    add_botao = ft.IconButton(icon=ft.Icons.PERSON_ADD, icon_size=35, on_click=lambda e: addframe_to_main(e), tooltip="Novo contato")
    
    page.appbar = ft.AppBar(
        bgcolor=ft.Colors.BLUE_300,
        title=ft.Text("Agenda de contatos"),
        actions=[add_botao, ft.IconButton(icon=ft.Icons.SEARCH, icon_size=35, tooltip="Pesquisar contato (sem funcionalidade ainda)")],
        toolbar_height=60,

    )
    
    area_contatos =ft.Column(
        expand=True,
        controls=[],
        )

    _container_contatos_ = ft.Container(
        content=area_contatos,
        alignment=ft.alignment.center,
    )
    _main_ = ft.Column(  #passando a usar isso para abrir a aba de editar ou adicionar contato substituindo a lista de contatos.
        controls=[_container_contatos_],
    )
    
    add_frame = ft.Container(
        content=ft.Column(
            [
                ft.Row(
                    controls=[ft.IconButton(icon=ft.Icons.CLOSE, tooltip="Fechar", icon_size=40, on_click=lambda e: fechar_frame(e))],
                    alignment=ft.MainAxisAlignment.END
                ),
                ft.Column(
                    controls=[campo_nome,
                              campo_sobrenome,
                              campo_telefone,
                              campo_email,
                              campo_nota],
                    horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                    spacing=30
                ),
                ft.Row(
                    controls=[ft.CupertinoButton(content=ft.Text("Adicionar", color=ft.Colors.BLACK),bgcolor=ft.Colors.BLUE_300, tooltip="Adicionar Contato", height=50, width=120, on_click=lambda e: adicionar_to_database(e, campo_nome.value, campo_sobrenome.value, campo_nota.value, format_phone(e), campo_email.value))],
                    alignment=ft.MainAxisAlignment.END,
                    width=350
                )
            ],
            horizontal_alignment=ft.CrossAxisAlignment.CENTER
        ),
        bgcolor=ft.Colors.WHITE,
        border_radius=10,
        shadow=ft.BoxShadow(color=ft.Colors.BLACK54, blur_radius=5, spread_radius=1),
        padding=15,
        height=680,
        expand=True,
    )
    
    edit_frame = ft.Container(
        content=ft.Column(
            [
                ft.Row(
                    controls=[_id_contato_,ft.IconButton(icon=ft.Icons.CLOSE, icon_size=40, tooltip="Fechar", on_click=lambda e: fechar_frame(e))],
                    alignment=ft.MainAxisAlignment.END
                ),
                ft.Column(
                    controls=[campo_nome,
                              campo_sobrenome,
                              campo_telefone,
                              campo_email,
                              campo_nota],
                    horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                    spacing=30
                ),
                ft.Row(
                    controls=[ft.CupertinoButton(content=ft.Text("Confirmar", color=ft.Colors.BLACK), bgcolor=ft.Colors.BLUE_300, tooltip="Confirmar edição", height=50, width=120, on_click=lambda e: editar_database(e, _id_contato_.value,campo_nome.value, campo_sobrenome.value, campo_nota.value, format_phone(e), campo_email.value))],
                    alignment=ft.MainAxisAlignment.END,
                    width=350,
                )
            ],
            horizontal_alignment=ft.CrossAxisAlignment.CENTER
        ),
        bgcolor=ft.Colors.WHITE,
        border_radius=10,
        shadow=ft.BoxShadow(color=ft.Colors.BLACK54, blur_radius=5, spread_radius=1),
        padding=10,
        height=680,
        expand=True,
    )
    
    def format_phone(e):
        raw = re.sub(r'\D', '', campo_telefone.value)
        
        formatted = ""

        if len(raw) >= 2:
            formatted += f'({raw[:2]}) '
        if len(raw) >= 7:
            formatted += f'{raw[2:7]}-{raw[7:11]}'
        elif len(raw) > 2:
            formatted += raw[2:]
        
        return formatted
    
    def load():
        dados = Getall()
        area_contatos.controls.clear()
        _id_contato_.value = ""
        campo_nome.value = ""
        campo_sobrenome.value = ""
        campo_nota.value = ""
        campo_telefone.value = ""
        campo_email.value = ""

        if not dados:
            area_contatos.controls.append(ft.Text("nenhum contato encontrado",text_align=ft.TextAlign.CENTER, expand=True))
        else:
            for dado_contato in dados:
                newcard = create_card(dado_contato, on_delete=_on_delete_, on_edit=editframe_to_main)
                area_contatos.controls.append(newcard)
        
        page.update()

    def _on_delete_(id_contato):
        def confirm(e):
            DeleteContato(id_contato)
            page.close(alert)
            load()
            page.update()
        
        def cancel(e):
            page.close(alert)
            page.update()
        
        alert = ft.AlertDialog(
            title=ft.Text("Apagar contato"),
            content=ft.Text("Tem certeza que deseja apagar este contato?"),
            actions=[
                ft.TextButton(text="Cancelar",  on_click=lambda e: cancel(e)),
                ft.TextButton(text="Confirmar", on_click=lambda e: confirm(e))
            ]
        )
        
        page.open(alert)
        page.update()

    def fechar_frame(e):
        _main_.controls[0] = _container_contatos_
        load()
        page.update()
        
    def addframe_to_main(e):
        _main_.controls[0] = add_frame
        page.update()
    
    def editframe_to_main(e):
        _id_contato_.value = e["id_contato"]
        if e["nome"] == "Sem nome":
            campo_nome.value = ""
        else:
            campo_nome.value = e["nome"]
        campo_sobrenome.value = e["sobrenome"]
        campo_nota.value = e["nota"]
        campo_telefone.value = e["telefone"][0]
        campo_email.value = e["email"][0]
        
        _main_.controls[0] = edit_frame
        page.update()

    def adicionar_to_database(e, nome, sobrenome, nota, telefone, email):
        
        if telefone == "":
            pass
        else:
            if nome == "":
                contator = addContato("Sem nome", sobrenome, nota)
            else:
                contator = addContato(nome, sobrenome, nota)
                        
            addTelefone(contator, telefone)
            addEmail(contator, email)
            
        load()
        _main_.controls[0] = _container_contatos_
        page.update()
    
    def editar_database(e, id_contato, nome, sobrenome, nota, telefone, email):
        
        editContato(id_contato, nome, sobrenome, nota)    
        editTelefone(id_contato, telefone)
        editEmail(id_contato, email)
        load()
        _main_.controls[0] = _container_contatos_
        page.update()

    page.add(_main_)
    load()

ft.app(target=main)
