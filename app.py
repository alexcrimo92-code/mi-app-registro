import flet as ft

def main(page: ft.Page):
    page.padding = 0
    
    # 1. Definimos el contenido (los botones)
    menu_content = ft.Column(
        [
            ft.Text("Menú Principal", size=33, weight="bold", color="white"),
            ft.Container(height=20),
            ft.Row([ft.ElevatedButton("NUEVO"), ft.ElevatedButton("PDF")], alignment=ft.MainAxisAlignment.CENTER),
            ft.Row([ft.ElevatedButton("HISTORIAL"), ft.ElevatedButton("USUARIO")], alignment=ft.MainAxisAlignment.CENTER),
            ft.Row([ft.ElevatedButton("CONFIGURAR"), ft.ElevatedButton("TOTAL")], alignment=ft.MainAxisAlignment.CENTER),
        ],
        alignment=ft.MainAxisAlignment.CENTER,
        horizontal_alignment=ft.CrossAxisAlignment.CENTER,
        tight=True
    )

    # 2. El Stack debe ocupar el tamaño completo de la página
    # Usamos page.window_width y page.window_height para asegurar que el Stack sea grande
    page.add(
        ft.Stack(
            [
                ft.Image(src="fondo.jpg", fit="cover", width=page.width, height=page.height),
                
                # 3. Este contenedor es la clave:
                # Al ponerle expand=True, obliga a ocupar todo el espacio del Stack.
                ft.Container(
                    content=menu_content,
                    alignment=ft.alignment.Alignment(0, 0), # Alineación absoluta al centro
                    expand=True
                )
            ],
            expand=True
        )
    )
    page.update()

ft.app(target=main)
