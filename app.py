import os
import flet as ft
from supabase import create_client

# --- CONFIGURACIÓN ---
URL = "https://bggzywzlusinkwwkwzgj.supabase.co"
KEY = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6ImJnZ3p5d3psdXNpbmt3d2t3emdqIiwicm9sZSI6ImFub24iLCJpYXQiOjE3ODI0MDMxNjMsImV4cCI6MjA5Nzk3OTE2M30.GtEiVvBZXeAYKap7YOK-CxNmUBHIoxxkJjVV4QyJp4c"
supabase = create_client(URL, KEY)

def main(page: ft.Page):
    page.title = "Registro de Trabajo"
    page.theme_mode = ft.ThemeMode.LIGHT
    page.bgcolor = "#F0F2F5"
    page.padding = 0

    contenedor_pantalla = ft.Container(expand=True, padding=20)

    # Función para botones con estilo usando parámetros universales
    def crear_boton_menu(texto_boton, funcion):
        return ft.Container(
            content=ft.ElevatedButton(
                text=texto_boton,
                on_click=funcion,
            ),
            padding=5
        )

    def obtener_totales():
        try:
            response = supabase.table("datos_app").select("horas, metros").execute()
            data = response.data
            return sum(float(item.get('horas', 0) or 0) for item in data), \
                   sum(float(item.get('metros', 0) or 0) for item in data)
        except:
            return 0, 0

    def mostrar_menu(e=None):
        horas, metros = obtener_totales()
        contenedor_pantalla.content = ft.Column([
            ft.Text("CONTROL DE OBRA", size=26, weight="bold"),
            # Contenedor para totales sin usar 'color' o argumentos complejos
            ft.Container(
                content=ft.Row([
                    ft.Column([ft.Text("Total Horas"), ft.Text(str(horas), size=22, weight="bold")]),
                    ft.VerticalDivider(),
                    ft.Column([ft.Text("Total Metros"), ft.Text(str(metros), size=22, weight="bold")])
                ]),
                bgcolor="white", padding=20
            ),
            ft.Container(height=20),
            crear_boton_menu("NUEVO REGISTRO", mostrar_formulario),
            crear_boton_menu("VER HISTORIAL", mostrar_historial)
        ])
        page.update()

    def mostrar_formulario(e):
        contenedor_pantalla.content = ft.Column([
            ft.ElevatedButton("← Volver", on_click=mostrar_menu),
            ft.Text("Nuevo Registro", size=20, weight="bold"),
            ft.TextField(label="Fecha", value="26/06/2026"),
            ft.TextField(label="Horas"),
            ft.TextField(label="Metros"),
            ft.ElevatedButton("GUARDAR", on_click=mostrar_menu)
        ])
        page.update()

    def mostrar_historial(e):
        try:
            response = supabase.table("datos_app").select("*").execute()
            tarjetas = [ft.Card(content=ft.Container(padding=15, content=ft.Column([
                ft.Text("PARTE: " + str(item.get('n_parte', 'N/A')), weight="bold"),
                ft.Text("🏢 " + str(item.get('constructora', 'N/A'))),
                ft.Text("📍 " + str(item.get('lugar', 'N/A'))),
                ft.Text("⏱ " + str(item.get('horas', '0')) + " hrs | 📏 " + str(item.get('metros', '0')) + " m")
            ]))) for item in response.data]
        except:
            tarjetas = [ft.Text("Error al cargar")]

        contenedor_pantalla.content = ft.Column([
            ft.ElevatedButton("← Volver", on_click=mostrar_menu),
            ft.Text("Historial", size=20, weight="bold"),
            ft.ListView(controls=tarjetas, expand=True, spacing=10)
        ], expand=True)
        page.update()

    page.add(contenedor_pantalla)
    mostrar_menu()

ft.app(target=main, view=ft.AppView.WEB_BROWSER, port=int(os.environ.get("PORT", 8080)))