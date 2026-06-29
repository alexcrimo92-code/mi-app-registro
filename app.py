import flet as ft

def main(page: ft.Page):
    page.padding = 0
    
    # Función para crear botones uniformes
    def crear_boton(texto, icono):
        return ft.ElevatedButton(
            content=ft.Row(
                [
                    ft.Icon(name=icono, size=20),
                    ft.Text(value=texto)
                ],
                alignment=ft.MainAxisAlignment.CENTER,
            ),
            width=140,
            height=50,
        )

    # Contenido principal
    menu_content = ft.Column(
        [
            ft.Text("Menú Principal", size=33, weight="bold", color="white"),
            ft.Container(height=20),
            
            # Filas de botones
            ft.Row([crear_boton("NUEVO", "add"), crear_boton("PDF", "picture_as_pdf")], 
                   alignment=ft.MainAxisAlignment.CENTER),
            ft.Row([crear_boton("HISTORIAL", "history"), crear_boton("USUARIO", "person")], 
                   alignment=ft.MainAxisAlignment.CENTER),
            ft.Row([crear_boton("CONFIGURAR", "settings"), crear_boton("TOTAL", "analytics")], 
                   alignment=ft.MainAxisAlignment.CENTER),
        ],
        alignment=ft.MainAxisAlignment.CENTER,
        horizontal_alignment=ft.CrossAxisAlignment.CENTER,
        tight=True
    )

    page.add(
        ft.Stack([
            ft.Image(src="fondo.jpg", fit="cover", width=page.width, height=page.height),
            ft.Container(
                expand=True,
                alignment=ft.alignment.center,
                content=menu_content
            )
        ])
    )
    page.update()

ft.app(target=main)
