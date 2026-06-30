import os
import flet as ft
from supabase import create_client

# --- CONFIGURACIÓN ---
URL = "https://bggzywzlusinkwwkwzgj.supabase.co"
KEY = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6ImJnZ3p5d3psdXNpbmt3d2t3emdqIiwicm9sZSI6ImFub24iLCJpYXQiOjE3ODI0MDMxNjMsImV4cCI6MjA5Nzk3OTE2M30.GtEiVvBZXeAYKap7YOK-CxNmUBHIoxxkJjVV4QyJp4c"
supabase = create_client(URL, KEY)



def main(page: ft.Page):
    page.title = "Registro de Partes de Trabajo"
   page.padding = 0
    
    # 1. Definimos el contenido (los botones)
    menu_content = ft.Column(
        [
            ft.Text("Menú Principal", size=33, weight="bold", color="white"),
            ft.Container(height=20),
            ft.Row([ft.ElevatedButton("NUEVO PARTE"), #ft.ElevatedButton("PDF")], alignment=ft.MainAxisAlignment.CENTER),
            ft.Row([ft.ElevatedButton("HISTORIAL"), #ft.ElevatedButton("USUARIO")], alignment=ft.MainAxisAlignment.CENTER),
            ft.Row([ft.ElevatedButton("CONFIGURAR"), #ft.ElevatedButton("TOTAL")], alignment=ft.MainAxisAlignment.CENTER),
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


    def mostrar_formulario(e):
        # Usamos Column con scroll para evitar problemas en pantallas pequeñas
        contenedor_pantalla.content = ft.Column([
            ft.Text("Nuevo Registro", size=24, weight="bold"),
            ft.TextField(label="Fecha", value="26/06/2026"),
            ft.TextField(label="Nº Parte"),
            ft.TextField(label="Horas"),
            ft.TextField(label="Metros"),
            ft.TextField(label="Material Instalado"),
            ft.TextField(label="Direccion"), 
            ft.TextField(label="Constructora"),
            ft.TextField(label="Compañero"),
            
          
            
            ft.ElevatedButton("GUARDAR", icon="SAVE", on_click=mostrar_menu),
            ft.Divider(),
            # BOTÓN ABAJO

            ft.ElevatedButton("← MENÚ", icon="HOME", on_click=mostrar_menu)
        ], scroll=ft.ScrollMode.AUTO, alignment=ft.MainAxisAlignment.START)
        page.update()

    def mostrar_historial(e):
        try:
            response = supabase.table("datos_app").select("*").execute()
            tarjetas = []
            for item in response.data:
                tarjetas.append(
                    ft.Card(
    content=ft.Container(
        content=ft.Column([
            ft.Text(f"PARTE: {item.get('n_parte', 'N/A')}", weight="bold", color="blue"),
            ft.Text(f"Fecha: {item.get('fecha', '')}"),
            ft.Divider(),
            ft.Text(f"🏢 {item.get('constructora', 'N/A')}"),
            ft.Text(f"📍 {item.get('lugar', 'N/A')}"),
            ft.Text(f"⏱ {item.get('horas', '0')} hrs"),
            # Aquí está la corrección:
            ft.Row([
                ft.Text(f"📏 {item.get('metros', '0')} m"),
                ft.Text("|"),
                # Asegúrate de que el nombre aquí coincida exactamente con tu columna en Supabase
                ft.Text(f"🛠 {item.get('material _instalado', 'N/A')}") 
            ])
        ], spacing=5),
        padding=15
                        )
                    )
                )
        except Exception as ex:
            tarjetas = [ft.Text(f"Error: {ex}")]

        contenedor_pantalla.content = ft.Column([
            ft.Text("Historial", size=24, weight="bold"),
            ft.ListView(controls=tarjetas, expand=True, spacing=10),
            ft.Divider(),
            # BOTÓN ABAJO
            ft.ElevatedButton("← VOLVER AL MENÚ", icon="HOME", on_click=mostrar_menu)
        ], expand=True)
        page.update()

    page.add(contenedor_pantalla)
    mostrar_menu()

# Aseguramos el puerto para Render
ft.app(target=main, assets_dir="assets", view=ft.AppView.WEB_BROWSER, port=int(os.environ.get("PORT", 8080)))