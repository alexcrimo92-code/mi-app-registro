import os
import flet as ft
from supabase import create_client

# --- CONFIGURACIÓN ---
URL = "https://bggzywzlusinkwwkwzgj.supabase.co"
KEY = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6ImJnZ3p5d3psdXNpbmt3d2t3emdqIiwicm9sZSI6ImFub24iLCJpYXQiOjE3ODI0MDMxNjMsImV4cCI6MjA5Nzk3OTE2M30.GtEiVvBZXeAYKap7YOK-CxNmUBHIoxxkJjVV4QyJp4c"
supabase = create_client(URL, KEY)



def main(page: ft.Page):
    page.padding = 0  # <--- Esto elimina el marco blanco
    page.title = "Registro de Partes de Trabajo"
    page.theme_mode = ft.ThemeMode.LIGHT
    page.bgcolor = "#F8F9FA"

    # Esta línea debe tener EXACTAMENTE 4 espacios de sangría
    contenedor_pantalla = ft.Container(expand=True, padding=0)

    # Esta función también debe tener EXACTAMENTE 4 espacios de sangría
    def mostrar_menu(e=None):
        contenedor_pantalla.content = ft.Stack([
            # 1. Imagen de fondo
            ft.Image(
                src="fondo.jpg",
                width=page.width,
                height=page.height,
                fit="cover",
            ),
            # 2. Contenedor de control (con color sólido para probar)
            ft.Container(
                content=ft.Column(
                    [
                        ft.Text("MENÚ PRINCIPAL", size=30, weight="bold", color="blue"), # Texto azul fuerte
                        ft.ElevatedButton("NUEVO REGISTRO", icon="add"),
                        ft.ElevatedButton("VER PARTES", icon="history"),
                    ],
                    alignment="center",
                    horizontal_alignment="center",
                ),
                bgcolor="white", # Fondo blanco sólido para ver si aparecen
                opacity=0.9,     # Casi opaco para que se vea bien
                padding=40,
                alignment="center",
                expand=True,
            )
        ])
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
