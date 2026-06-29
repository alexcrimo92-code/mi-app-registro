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
                # AÑADIMOS: expand=True y definimos alineación del contenedor
                ft.Container(
                    expand=True,
                    alignment=ft.alignment.center, # Esto centra el contenido vertical y horizontalmente
                    content=ft.Column(
                        [
                            ft.Row(
                                [
                                    ft.Text("Horas: 0", color="white", weight="bold"),
                                    ft.Text("Metros: 0", color="white", weight="bold"),
                                ],
                                alignment=ft.MainAxisAlignment.CENTER,
                            ),
                            ft.Text("Menú Principal", size=33, weight="bold", color="white"),
                            ft.Container(height=25),
                            ft.ElevatedButton("NUEVO REGISTRO", icon="add"),
                            ft.ElevatedButton("VER PARTES", icon="history"),
                        ],
                        # En el Column, esto ayuda a alinear los hijos internos
                        alignment=ft.MainAxisAlignment.CENTER, 
                        horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                        tight=True # tight=True ayuda a que la columna ocupe solo el espacio de sus hijos
                    ),
                )
            ])
        )
        page.update()

    mostrar_menu()

ft.app(target=main)
