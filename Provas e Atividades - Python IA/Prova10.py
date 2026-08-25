import flet as ft

def main(page: ft.Page):
    page.title = "Formulário de Contato"
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.theme_mode = ft.ThemeMode.LIGHT
    page.window_width = 400
    page.window_height = 550

    nome_input = ft.TextField(label="Nome", placeholder="Digite seu nome completo", width=300)
    email_input = ft.TextField(label="E-mail", placeholder="seuemail@exemplo.com", width=300)
    mensagem_input = ft.TextField(
        label="Mensagem", 
        placeholder="Como podemos ajudar?", 
        multiline=True, 
        min_lines=3, 
        width=300
    )
    
    msg_confirmacao = ft.Text(size=16, weight=ft.FontWeight.BOLD)

    def enviar_click(e):
        if not nome_input.value or not email_input.value or not mensagem_input.value:
            msg_confirmacao.value = "Por favor, preencha todos os campos!"
            msg_confirmacao.color = ft.colors.RED
        else:
            msg_confirmacao.value = f"Obrigado, {nome_input.value}! Enviado com sucesso."
            msg_confirmacao.color = ft.colors.GREEN
            
            nome_input.value = ""
            email_input.value = ""
            mensagem_input.value = ""
        
        page.update()

    page.add(
        ft.Column(
            [
                ft.Text("Entre em Contato", size=30, weight="bold"),
                nome_input,
                email_input,
                mensagem_input,
                ft.ElevatedButton("Enviar Mensagem", on_click=enviar_click, icon=ft.icons.SEND),
                msg_confirmacao
            ],
            alignment=ft.MainAxisAlignment.CENTER,
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            spacing=20
        )
    )

if __name__ == "__main__":
    ft.app(target=main)