import flet as ft

def main(page: ft.Page):
    page.padding = 0
    
    # Crear un contenedor que ocupa toda la pantalla
    # Usamos 'alignment=ft.alignment.center' que es el estándar.
    # SI te da error 'no attribute center', cambia esa línea por:
    # alignment=ft.alignment.Alignment(0, 0)
    
    contenido_centrado = ft.Container(
        expand=True,
        alignment=ft.alignment.Alignment(0, 0), 
        content=ft.Column(
            [
                ft.Text("Menú Principal", size=33, weight="bold", color="white"),
                ft.Container(height=20),
                
                # Botones (usando controles básicos para evitar errores)
                ft.Row([
                    ft.ElevatedButton("NUEVO"), 
                    ft.ElevatedButton("PDF")
                ], alignment=ft.MainAxisAlignment.CENTER),
                
                ft.Row([
                    ft.ElevatedButton("HISTORIAL"), 
                    ft.ElevatedButton("USUARIO")
                ], alignment=ft.MainAxisAlignment.CENTER),
                
                ft.Row([
                    ft.ElevatedButton("CONFIGURAR"), 
                    ft.ElevatedButton("TOTAL")
                ], alignment=ft.MainAxisAlignment.CENTER),
            ],
            alignment=ft.MainAxisAlignment.CENTER,
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            tight=True
        )
    )

    page.add(
        ft.Stack([
            ft.Image(src="fondo.jpg", fit="cover", width=page.width, height=page.height),
            contenido_centrado
        ])
    )
    page.update()

ft.app(target=main)
