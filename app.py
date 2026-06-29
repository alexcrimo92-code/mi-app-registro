import os
import flet as ft
from supabase import create_client

# --- CONFIGURACIÓN ---
URL = "https://bggzywzlusinkwwkwzgj.supabase.co"
KEY = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6ImJnZ3p5d3psdXNpbmt3d2t3emdqIiwicm9sZSI6ImFub24iLCJpYXQiOjE3ODI0MDMxNjMsImV4cCI6MjA5Nzk3OTE2M30.GtEiVvBZXeAYKap7YOK-CxNmUBHIoxxkJjVV4QyJp4c"
supabase = create_client(URL, KEY)



def main(page: ft.Page):
    page.title = "Registro de Partes de Trabajo"
    page.theme_mode = ft.ThemeMode.LIGHT
    page.bgcolor = "#F8F9FA"

    # Contenedor principal que ocupa toda la pantalla
    contenedor_pantalla = ft.Container(expand=True, padding=10)

    def mostrar_menu(e=None):
        contenedor_pantalla.content = ft.Column([
            ft.Text("Menú Principal", size=28, weight="bold"),
            ft.Container(height=20),
            ft.ElevatedButton("NUEVO REGISTRO", icon="ADD", on_click=mostrar_formulario),
            ft.ElevatedButton("VER PARTES", icon="HISTORY", on_click=mostrar_historial)
        ], alignment=ft.MainAxisAlignment.CENTER, horizontal_alignment=ft.CrossAxisAlignment.CENTER)
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
ft.Text(f"📏 {item.get('metros', '0')} m | 🛠 {item.get('material', 'N/A')}") 
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
ft.app(target=main, view=ft.AppView.WEB_BROWSER, port=int(os.environ.get("PORT", 8080)))