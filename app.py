import flet as ft

def main(page: ft.Page):
    page.padding = 0
    
    def mostrar_menu(e=None):
        page.clean() # Limpia todo lo anterior
        page.add(
            ft.Stack([
                # Imagen de fondo
                ft.Image(
                    src="fondo.jpg",
                    width=page.width,
                    height=page.height,
                    fit="cover"
                ),
                # Capa de botones
                ft.Container(
                    expand=True,
                    content=ft.Column(
                        [
                            ft.Text("Menú Principal", size=28, weight="bold", color="white"),
                            ft.Container(height=20),
                            ft.ElevatedButton(
                                "NUEVO REGISTRO", 
                                icon="add", 
                                on_click=lambda _: print("Nuevo Registro"), # Cambia esto por tu función
                                style=ft.ButtonStyle(shape=ft.RoundedRectangleBorder(radius=20))
                            ),
                            ft.ElevatedButton(
                                "VER PARTES", 
                                icon="history", 
                                on_click=lambda _: print("Ver Partes"), # Cambia esto por tu función
                                style=ft.ButtonStyle(shape=ft.RoundedRectangleBorder(radius=20))
                            ),
                        ],
                        alignment="center",
                        horizontal_alignment="center",
                    ),
                )
            ])
        )
        page.update()

    # Llamamos al menú
    mostrar_menu()

ft.app(target=main)
