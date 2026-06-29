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
                # El truco es este Container con alignment.center y expand=True
                ft.Container(
                    expand=True,
                    alignment=ft.alignment.center, # Fuerza el centro absoluto del stack
                    content=ft.Column(
                        [
                            ft.Row(
                                [
                                    ft.Text("Horas: 0", color="white", weight="bold"),
                                    ft.Text("Metros: 0", color="white", weight="bold"),
                                ],
                                alignment=ft.MainAxisAlignment.CENTER,
                            ),
                            ft.Text("Menú Principal", size=28, weight="bold", color="white"),
                            ft.Container(height=20),
                            ft.ElevatedButton("NUEVO REGISTRO", icon="add"),
                            ft.ElevatedButton("VER PARTES", icon="history"),
                        ],
                        alignment=ft.MainAxisAlignment.CENTER,
                        horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                        tight=True, # Esto es clave para que el alignment.center funcione
                    ),
                )
            ])
        )
        page.update()

    mostrar_menu()

ft.app(target=main)
