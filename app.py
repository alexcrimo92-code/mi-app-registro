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
            # Contenedor que ocupa toda la pantalla y centra el contenido
            ft.Container(
                expand=True,
                alignment=ft.alignment.center, # <--- ESTO CENTRA TODO (Vertical y Horizontal)
                content=ft.Column(
                    [
                        ft.Text("Menú Principal", size=28, weight="bold", color="white"),
                        ft.Container(height=20),
                        ft.ElevatedButton("NUEVO REGISTRO", icon="add"),
                        ft.ElevatedButton("VER PARTES", icon="history"),
                    ],
                    alignment=ft.MainAxisAlignment.CENTER, # Centrado vertical de la columna
                    horizontal_alignment=ft.CrossAxisAlignment.CENTER, # Centrado horizontal
                    tight=True, # Hace que la columna ocupe solo el espacio de los elementos
                ),
            )
        ])
    )
    page.update()

    # Llamamos al menú
    mostrar_menu()

ft.app(target=main)
