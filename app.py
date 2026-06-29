import flet as ft

def main(page: ft.Page):
    page.title = "Test Eyfer Const"
    page.padding = 0
    
    # Pruebas de control
    def cambiar_color(e):
        page.bgcolor = "green"
        page.update()

    # Si ves este botón, la App está funcionando
    page.add(
        ft.Container(
            content=ft.Column([
                ft.Text("PRUEBA DE CONEXIÓN", size=30, color="black"),
                ft.ElevatedButton("Haz clic aquí para ver si responde", on_click=cambiar_color)
            ], alignment="center"),
            bgcolor="yellow",
            expand=True
        )
    )

ft.app(target=main)
