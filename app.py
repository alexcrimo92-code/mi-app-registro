import flet as ft

def main(page: ft.Page):
    page.padding = 0
    
    # Creamos una función auxiliar para que los botones sean uniformes
    def crear_boton(texto, icono):
    return ft.ElevatedButton(
        content=ft.Row(
            [ft.Icon(icono), ft.Text(texto)],
            alignment=ft.MainAxisAlignment.CENTER
        ),
        width=140,
        height=50
        )

    # Definimos la estructura de botones en filas
    menu_content = ft.Column(
        [
            ft.Text("Menú Principal", size=33, weight="bold", color="white"),
            ft.Container(height=20), # Espaciador
            
            # Fila 1
            ft.Row([crear_boton("NUEVO", "add"), crear_boton("PDF", "picture_as_pdf")], 
                   alignment=ft.MainAxisAlignment.CENTER),
            
            # Fila 2
            ft.Row([crear_boton("HISTORIAL", "history"), crear_boton("USUARIO", "person")], 
                   alignment=ft.MainAxisAlignment.CENTER),
            
            # Fila 3
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
            # El contenedor padre asegura el centrado de toda la columna
            ft.Container(
                expand=True,
                alignment=ft.alignment.center,
                content=menu_content
            )
        ])
    )
    page.update()

ft.app(target=main)
