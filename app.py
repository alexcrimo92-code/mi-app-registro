import flet as ft

def main(page: ft.Page):
    # Configuración base
    page.padding = 0
    
    # Este es el contenedor "maestro" que mantiene todo centrado
    menu_layout = ft.Container(
        expand=True,
        # alignment.center coloca el contenido justo en el medio
        alignment=ft.alignment.center, 
        content=ft.Column(
            [
                ft.Text("Menú Principal", size=33, weight="bold", color="white"),
                ft.ElevatedButton("NUEVO REGISTRO", icon="add"),
                ft.ElevatedButton("VER PARTES", icon="history"),
            ],
            # MainAxisAlignment centra los elementos DENTRO de la columna
            alignment=ft.MainAxisAlignment.CENTER,
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            tight=True 
        )
    )

    page.add(
        ft.Stack([
            ft.Image(src="fondo.jpg", fit="cover", width=page.width, height=page.height),
            menu_layout
        ])
    )

ft.app(target=main)
