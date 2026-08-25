import flet as ft

def main(page: ft.Page):
    page.title = "Minha Lista de Tarefas"
    page.vertical_alignment = ft.MainAxisAlignment.START
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.window_width = 400
    page.window_height = 600

    lista_tarefas = ft.Column()

    def adicionar_tarefa_click(e):
        if not campo_texto.value:
            campo_texto.error_text = "Por favor, digite uma tarefa"
            page.update()
        else:
            nova_tarefa = ft.Checkbox(label=campo_texto.value)
            lista_tarefas.controls.append(nova_tarefa)
            
            campo_texto.value = ""
            campo_texto.error_text = None
            campo_texto.focus()
            
            page.update()

    campo_texto = ft.TextField(
        hint_text="O que precisa ser feito?", 
        expand=True,
        on_submit=adicionar_tarefa_click
    )
    
    botao_adicionar = ft.FloatingActionButton(
        icon=ft.icons.ADD, 
        on_click=adicionar_tarefa_click
    )

    page.add(
        ft.Text("Lista de Tarefas", size=30, weight=ft.FontWeight.BOLD),
        ft.Row(
            controls=[
                campo_texto,
                botao_adicionar,
            ],
        ),
        ft.Divider(),
        lista_tarefas
    )

ft.app(target=main)