import flet as ft

def main(page: ft.Page):
    page.padding = 0
    
    def mostrar_menu(e=None):
        page.clean()
        page.add(
            ft.Stack([
                ft.Image(src="fondo.jpg", width=page.width, height=page.height, fit="cover"),
                
                ft.Container(
                    expand=True,
                    alignment="center", # Centrado absoluto
                    content=ft.Column(
                        [
                            # NUEVA FILA PARA LOS DATOS (Izquierda y Derecha)
                            ft.Row(
                                [
                                    ft.Container(content=ft.Text("Horas: 0", color="white"), padding=10),
                                    ft.Container(content=ft.Text("Metros: 0", color="white"), padding=10),
                                ],
                                alignment="center", # Centra los dos contenedores en la fila
                            ),
                            
                            ft.Text("Menú Principal", size=28, weight="bold", color="white"),
                            ft.Container(height=20),
                            ft.ElevatedButton("NUEVO REGISTRO", icon="add"),
                            ft.ElevatedButton("VER PARTES", icon="history"),
                        ],
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
