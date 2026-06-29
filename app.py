import flet as ft

def main(page: ft.Page):
    page.padding = 0
    
    def mostrar_menu(e=None):
        page.clean()
        page.add(
            ft.Stack([
                # Imagen de fondo
                ft.Image(
                    src="fondo.jpg",
                    width=page.width,
                    height=page.height,
                    fit="cover"
                ),
                # El contenedor que fuerza el centrado absoluto
                ft.Container(
                    expand=True,
                    alignment=ft.alignment.center, # Alineación del contenedor
                    content=ft.Column(
                        [
                            ft.Text("Menú Principal", size=28, weight="bold", color="white"),
                            ft.Container(height=20),
                            ft.ElevatedButton("NUEVO REGISTRO", icon="add"),
                            ft.ElevatedButton("VER PARTES", icon="history"),
                        ],
                        # Alineación dentro de la columna
                        alignment="center",
                        horizontal_alignment="center",
                        tight=True,
                    ),
                )
            ])
        )
        page.update()

    mostrar_menu()

ft.app(target=main)
