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

    # Función para botones premium
    def crear_boton_menu(texto, icono, funcion):
        return ft.Container(
            content=ft.ElevatedButton(
                content=ft.Row([ft.Icon(icono), ft.Text(texto, size=16)], alignment=ft.MainAxisAlignment.CENTER),
                style=ft.ButtonStyle(
                    bgcolor=ft.colors.WHITE,
                    color=ft.colors.BLUE_700,
                    padding=25,
                    shape=ft.RoundedRectangleBorder(radius=15),
                ),
                on_click=funcion,
            ),
            shadow=ft.BoxShadow(blur_radius=10, color=ft.colors.GREY_300)
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
            ft.Text("CONTROL DE OBRA", size=26, weight="bold", color=ft.colors.BLUE_900),
            ft.Container(
                content=ft.Row([
                    ft.Column([ft.Text("Total Horas", size=12), ft.Text(f"{horas}", size=22, weight="bold")], horizontal_alignment=ft.CrossAxisAlignment.CENTER),
                    ft.VerticalDivider(),
                    ft.Column([ft.Text("Total Metros", size=12), ft.Text(f"{metros}", size=22, weight="bold")], horizontal_alignment=ft.CrossAxisAlignment.CENTER)
                ], alignment=ft.MainAxisAlignment.SPACE_EVENLY),
                bgcolor=ft.colors.WHITE, padding=20, border_radius=20,
                shadow=ft.BoxShadow(blur_radius=10, color=ft.colors.GREY_300)
            ),
            ft.Container(height=20),
            crear_boton_menu("NUEVO REGISTRO", ft.icons.ADD_CIRCLE_OUTLINE, mostrar_formulario),
            crear_boton_menu("VER HISTORIAL", ft.icons.LIST_ALT, mostrar_historial)
        ], alignment=ft.MainAxisAlignment.CENTER, horizontal_alignment=ft.CrossAxisAlignment.CENTER)
        page.update()

    def mostrar_formulario(e):
        contenedor_pantalla.content = ft.Column([
            ft.TextButton("← Volver", icon=ft.icons.ARROW_BACK, on_click=mostrar_menu),
            ft.Text("Nuevo Registro", size=20, weight="bold"),
            ft.TextField(label="Fecha", value="26/06/2026"),
            ft.TextField(label="Horas"),
            ft.TextField(label="Metros"),
            ft.ElevatedButton("GUARDAR", icon=ft.icons.SAVE, on_click=mostrar_menu)
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
            ], spacing=8, horizontal_alignment=ft.CrossAxisAlignment.START))) for item in response.data]
        except:
            tarjetas = [ft.Text("Error al cargar")]

        contenedor_pantalla.content = ft.Column([
            ft.TextButton("← Volver", icon=ft.icons.ARROW_BACK, on_click=mostrar_menu),
            ft.Text("Historial", size=20, weight="bold"),
            ft.ListView(controls=tarjetas, expand=True, spacing=10)
        ], expand=True)
        page.update()

    page.add(contenedor_pantalla)
    mostrar_menu()

ft.app(target=main, view=ft.AppView.WEB_BROWSER, port=int(os.environ.get("PORT", 8080)))