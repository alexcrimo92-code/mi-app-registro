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
                            # Aquí van tus elementos
                            ft.Text("Menú Principal", size=28, weight="bold", color="white"),
                            ft.Container(height=20),
                            ft.ElevatedButton("NUEVO REGISTRO", icon="add"),
                            ft.ElevatedButton("VER PARTES", icon="history"),
                        ],
                        # Estas dos líneas son las que centran el bloque entero
                        alignment=ft.MainAxisAlignment.CENTER, 
                        horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                    ),
                )
            ])
        )
        page.update()

    mostrar_menu()

ft.app(target=main)
