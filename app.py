import flet as ft

def main(page: ft.Page):
    page.padding = 0
    
    def mostrar_menu(e=None):
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
                    # Usamos strings en lugar de constantes para evitar errores de atributos
                    alignment="center", 
                    content=ft.Column(
                        [
                            ft.Text("Menú Principal", size=28, weight="bold", color="white"),
                            ft.Container(height=20),
                            ft.ElevatedButton("NUEVO REGISTRO", icon="add"),
                            ft.ElevatedButton("VER PARTES", icon="history"),
                        ],
                        # Alineación mediante strings
                        alignment="center",
                        horizontal_alignment="center",
                    ),
                )
            ])
        )
        page.update()

    mostrar_menu()

ft.app(target=main)
