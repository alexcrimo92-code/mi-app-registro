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
                # Contenedor principal que centra todo
                ft.Container(
                    expand=True,
                    alignment="center", # Alineación absoluta al centro
                    content=ft.Column(
                        [
                            # Fila de datos (Horas y Metros)
                            ft.Row(
                                [
                                    ft.Container(content=ft.Text("Total Horas: 0", color="white"), padding=10),
                                    ft.Container(content=ft.Text("Total Metros: 0", color="white"), padding=10),
                                ],
                                alignment="center",
                            ),
                            
                            # Título y Botones
                            ft.Text("Menú Principal", size=28, weight="bold", color="white"),
                            ft.Container(height=20),
                            ft.ElevatedButton("NUEVO REGISTRO", icon="add"),
                            ft.ElevatedButton("VER PARTES", icon="history"),
                        ],
                        alignment="center",
                        horizontal_alignment="center",
                        tight=True, # Mantiene el bloque compacto para centrarse mejor
                    ),
                )
            ])
        )
        page.update()

    mostrar_menu()

ft.app(target=main)
