import os
import flet as ft
from supabase import create_client

# --- CONFIGURACIÓN ---
URL = "https://bggzywzlusinkwwkwzgj.supabase.co"
KEY = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6ImJnZ3p5d3psdXNpbmt3d2t3emdqIiwicm9sZSI6ImFub24iLCJpYXQiOjE3ODI0MDMxNjMsImV4cCI6MjA5Nzk3OTE2M30.GtEiVvBZXeAYKap7YOK-CxNmUBHIoxxkJjVV4QyJp4c"
supabase = create_client(URL, KEY)


def main(page: ft.Page):
    page.title = "App Registro"
    page.theme_mode = "light"
    page.bgcolor = "#F0F2F5"
    page.padding = 0

    contenedor_pantalla = ft.Container(padding=20, expand=True)

    def obtener_totales():
        try:
            response = supabase.table("datos_app").select("horas, metros").execute()
            data = response.data
            t_h = sum(float(i.get('horas', 0) or 0) for i in data)
            t_m = sum(float(i.get('metros', 0) or 0) for i in data)
            return t_h, t_m
        except:
            return 0, 0

    def mostrar_menu(e=None):
        h, m = obtener_totales()
        contenedor_pantalla.content = ft.Column([
            ft.Text("MENÚ PRINCIPAL", size=24, weight="bold"),
            # Tarjeta de resumen (usando bgcolor en vez de color para evitar errores)
            ft.Card(content=ft.Container(padding=20, content=ft.Row([
                ft.Column([ft.Text("Total Horas"), ft.Text(str(h), size=20, weight="bold")]),
                ft.VerticalDivider(),
                ft.Column([ft.Text("Total Metros"), ft.Text(str(m), size=20, weight="bold")])
            ], alignment="center"))),
            ft.ElevatedButton("NUEVO REGISTRO", icon="add", on_click=mostrar_formulario),
            ft.ElevatedButton("VER HISTORIAL", icon="list", on_click=mostrar_historial)
        ], alignment="center", horizontal_alignment="center")
        page.update()

    def mostrar_formulario(e):
        contenedor_pantalla.content = ft.Column([
            ft.Text("Nuevo Registro", size=20, weight="bold"),
            ft.TextField(label="Fecha", value="26/06/2026"),
            ft.TextField(label="Horas"),
            ft.TextField(label="Metros"),
            ft.ElevatedButton("GUARDAR", icon="save", on_click=mostrar_menu),
            # Botón de regreso abajo
            ft.ElevatedButton("← VOLVER AL MENÚ", icon="arrow_back", on_click=mostrar_menu)
        ])
        page.update()

    def mostrar_historial(e):
        try:
            response = supabase.table("datos_app").select("*").execute()
            tarjetas = [ft.Card(content=ft.Container(padding=15, content=ft.Column([
                ft.Text(f"PARTE: {item.get('n_parte', 'N/A')}", weight="bold"),
                ft.Divider(),
                ft.Text(f"🏢 {item.get('constructora', 'N/A')}"),
                ft.Text(f"📍 {item.get('lugar', 'N/A')}"),
                ft.Text(f"⏱ {item.get('horas', '0')} hrs | 📏 {item.get('metros', '0')} m"),
                ft.Text(f"👥 {item.get('companero', 'N/A')}")
            ]))) for item in response.data]
        except:
            tarjetas = [ft.Text("Error al cargar")]

        contenedor_pantalla.content = ft.Column([
            ft.Text("Historial", size=20, weight="bold"),
            ft.ListView(controls=tarjetas, expand=True, spacing=10),
            # Botón de regreso abajo
            ft.ElevatedButton("← VOLVER AL MENÚ", icon="arrow_back", on_click=mostrar_menu)
        ], expand=True)
        page.update()

    page.add(contenedor_pantalla)
    mostrar_menu()

ft.app(target=main, port=int(os.environ.get("PORT", 8080)))