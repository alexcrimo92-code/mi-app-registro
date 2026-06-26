import os
import flet as ft
from supabase import create_client

# --- CONFIGURACIÓN ---
URL = "https://bggzywzlusinkwwkwzgj.supabase.co"
KEY = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6ImJnZ3p5d3psdXNpbmt3d2t3emdqIiwicm9sZSI6ImFub24iLCJpYXQiOjE3ODI0MDMxNjMsImV4cCI6MjA5Nzk3OTE2M30.GtEiVvBZXeAYKap7YOK-CxNmUBHIoxxkJjVV4QyJp4c"
supabase = create_client(URL, KEY)

def main(page: ft.Page):
    page.title = "App Registro de Trabajo"
    page.theme_mode = ft.ThemeMode.LIGHT
    page.bgcolor = "#F8F9FA"
    page.padding = 0

    contenedor_pantalla = ft.Container(expand=True, padding=20)

    def obtener_totales():
        try:
            response = supabase.table("datos_app").select("horas, metros").execute()
            data = response.data
            t_horas = sum(float(item.get('horas', 0) or 0) for item in data)
            t_metros = sum(float(item.get('metros', 0) or 0) for item in data)
            return t_horas, t_metros
        except:
            return 0, 0

    def mostrar_menu(e=None):
        horas, metros = obtener_totales()
        contenedor_pantalla.content = ft.Column([
            ft.Text("MENÚ PRINCIPAL", size=28, weight="bold"),
            # TARJETA DE RESUMEN
            ft.Card(color="#E3F2FD", content=ft.Container(padding=20, content=ft.Row([
                ft.Column([ft.Text("Total Horas", size=12), ft.Text(f"{horas}", size=24, weight="bold")], horizontal_alignment=ft.CrossAxisAlignment.CENTER),
                ft.VerticalDivider(),
                ft.Column([ft.Text("Total Metros", size=12), ft.Text(f"{metros}", size=24, weight="bold")], horizontal_alignment=ft.CrossAxisAlignment.CENTER)
            ], alignment=ft.MainAxisAlignment.SPACE_EVENLY))),
            ft.Container(height=20),
            ft.ElevatedButton("NUEVO REGISTRO", icon="ADD", on_click=mostrar_formulario, style=ft.ButtonStyle(padding=20)),
            ft.ElevatedButton("VER HISTORIAL", icon="LIST", on_click=mostrar_historial, style=ft.ButtonStyle(padding=20))
        ], alignment=ft.MainAxisAlignment.CENTER, horizontal_alignment=ft.CrossAxisAlignment.CENTER)
        page.update()

    def mostrar_formulario(e):
        contenedor_pantalla.content = ft.Column([
            ft.Text("Nuevo Registro", size=24, weight="bold"),
            ft.TextField(label="Fecha", value="26/06/2026"),
            ft.TextField(label="Nº Parte"),
            ft.TextField(label="Constructora"),
            ft.TextField(label="Lugar"),
            ft.TextField(label="Horas"),
            ft.TextField(label="Metros"),
            ft.TextField(label="Compañero"),
            ft.ElevatedButton("GUARDAR", icon="SAVE", on_click=mostrar_menu),
            ft.Container(height=20),
            ft.ElevatedButton("← VOLVER", icon="ARROW_BACK", on_click=mostrar_menu)
        ], scroll=ft.ScrollMode.AUTO)
        page.update()

    def mostrar_historial(e):
        try:
            response = supabase.table("datos_app").select("*").execute()
            tarjetas = [ft.Card(content=ft.Container(padding=15, content=ft.Column([
                ft.Text(f"PARTE: {item.get('n_parte', 'N/A')}", weight="bold", color="blue"),
                ft.Divider(),
                ft.Text(f"🏢 {item.get('constructora', 'N/A')}"),
                ft.Text(f"📍 {item.get('lugar', 'N/A')}"),
                ft.Text(f"⏱ {item.get('horas', '0')} hrs | 📏 {item.get('metros', '0')} m"),
                ft.Text(f"👥 {item.get('companero', 'N/A')}")
            ], spacing=5))) for item in response.data]
        except:
            tarjetas = [ft.Text("Error al cargar")]

        contenedor_pantalla.content = ft.Column([
            ft.Text("Historial", size=24, weight="bold"),
            ft.ListView(controls=tarjetas, expand=True, spacing=10),
            ft.ElevatedButton("← VOLVER", icon="ARROW_BACK", on_click=mostrar_menu)
        ], expand=True)
        page.update()

    page.add(contenedor_pantalla)
    mostrar_menu()

ft.app(target=main, view=ft.AppView.WEB_BROWSER, port=int(os.environ.get("PORT", 8080)))