import flet as ft

def main(page: ft.Page):
    page.padding = 0
    
    def mostrar_menu(e=None):
        page.clean()
        page.add(
            ft.Stack([
                # Imagen original (sin opacidad)
                ft.Image(
                    src="fondo.jpg",
                    width=page.width,
                    height=page.height,
                    fit="cover"
                ),
                # Contenedor para el contenido
                ft.Container(
                    expand=True,
                    # Quitamos alineación total para que no interfiera con la opacidad
                    content=ft.Column(
                        [
                            # Este contenedor vacío superior actúa como "empujador"
                            ft.Container(expand=True), 
                            
                            ft.Text("Menú Principal", size=28, weight="bold", color="white"),
                            ft.Container(height=20),
                            ft.ElevatedButton("NUEVO REGISTRO", icon="add"),
                            ft.ElevatedButton("VER PARTES", icon="history"),
                            
                            # Este contenedor vacío inferior equilibra el espacio
                            ft.Container(expand=True)
                        ],
                        alignment="center",
                        horizontal_alignment="center",
                    ),
                )
            ])
        )
        page.update()

    mostrar_menu()

ft.app(target=main)
