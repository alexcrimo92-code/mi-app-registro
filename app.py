import flet as ft

def main(page: ft.Page):
    page.padding = 0
    
    def mostrar_menu(e=None):
        # Todo esto debe tener 8 espacios de sangría porque está dentro de 'mostrar_menu'
        page.clean() 
        page.add(
            ft.Stack([
                ft.Image(
                    src="fondo.jpg",
                    width=page.width,
                    height=page.height,
                    fit="cover"
                ),
                ft.Container(
                    expand=True,
                    alignment=ft.alignment.center,
                    content=ft.Column(
                        [
                            ft.Text("Menú Principal", size=28, weight="bold", color="white"),
                            ft.Container(height=20),
                            ft.ElevatedButton("NUEVO REGISTRO", icon="add"),
                            ft.ElevatedButton("VER PARTES", icon="history"),
                        ],
                        alignment=ft.MainAxisAlignment.CENTER,
                        horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                        tight=True,
                    ),
                )
            ])
        )
        page.update()

    # Esto tiene 4 espacios porque está dentro de 'main'
    mostrar_menu()

ft.app(target=main)
