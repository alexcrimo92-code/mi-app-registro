import flet as ft

def main(page: ft.Page):
    page.title = "Mi App de Registro"
    entrada = ft.TextField(label="Escribe algo...", width=300)
    lista = ft.Column()

    def enviar(e):
        lista.controls.append(ft.Text(f"- {entrada.value}"))
        entrada.value = ""
        page.update()

    page.add(entrada, ft.ElevatedButton("Enviar", on_click=enviar), lista)

ft.app(target=main, port=8000, view=ft.AppView.WEB_BROWSER)