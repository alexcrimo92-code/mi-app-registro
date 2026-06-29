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
                # El secreto es usar 'alignment' en el contenedor que contiene la columna
                ft.Container(
                    expand=True,
                    alignment=ft.alignment.center, # <--- Fuerza el centro absoluto
                    content=ft.Column(
                        [
                            ft.Text("Menú Principal", size=28, weight="bold", color="white"),
                            ft.Container(height=20),
                            ft.ElevatedButton("NUEVO REGISTRO", icon="add"),
                            ft.ElevatedButton("VER PARTES", icon="history"),
                        ],
                        # Alineación interna de la columna
                        alignment="center",
                        horizontal_alignment="center",
                        tight=True, # Importante: Columna ajustada a su contenido
                    ),
                )
            ])
        )
        page.update()

    mostrar_menu()

ft.app(target=main)
