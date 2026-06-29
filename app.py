import flet as ft

def main(page: ft.Page):
    page.padding = 0
    
    def mostrar_menu(e=None):
        page.clean()
        page.add(
            ft.Stack([
                # Imagen de fondo original
                ft.Image(
                    src="fondo.jpg",
                    width=page.width,
                    height=page.height,
                    fit="cover"
                ),
                # Este contenedor obliga al contenido a centrarse en la pantalla
                ft.Container(
                    expand=True,
                    content=ft.Column(
                        [
                            # Nueva fila de datos agregada
                            ft.Row(
                                [
                                    ft.Text("Horas: 0", color="white", weight="bold"),
                                    ft.Text("Metros: 0", color="white", weight="bold"),
                                ],
                                alignment=ft.MainAxisAlignment.CENTER, # Centra horizontalmente
                            ),
                            # Elementos originales
                            ft.Text("Menú Principal", size=28, weight="bold", color="white"),
                            ft.Container(height=20),
                            ft.ElevatedButton("NUEVO REGISTRO", icon="add"),
                            ft.ElevatedButton("VER PARTES", icon="history"),
                        ],
                        # Estas líneas mantienen el centrado vertical y horizontal del bloque completo
                        alignment=ft.MainAxisAlignment.CENTER, 
                        horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                    ),
                )
            ])
        )
        page.update()

    mostrar_menu()

ft.app(target=main)
