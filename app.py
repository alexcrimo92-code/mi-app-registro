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
    page.bgcolor = "#F8F9FA"
    page.padding = 0

    contenedor_pantalla = ft.Container(expand=True)

    # Función auxiliar para botones bonitos
    def boton_menu(texto, icono, color, funcion):
        return ft.Container(
            content=ft.ElevatedButton(
                content=ft.Row([ft.Icon(icono), ft.Text(texto)], alignment=ft.MainAxisAlignment.CENTER),
                style=ft.ButtonStyle(
                    bgcolor=color, 
                    color="white",
                    shape=ft.RoundedRectangleBorder(radius=10),
                    padding=20
                ),
                on_click=funcion,
            ),
            width=280
        )

    def mostrar_menu(e=None):
        contenedor_pantalla.content = ft.Container(
            content=ft.Column([
                ft.Text("MENÚ PRINCIPAL", size=28, weight="bold", color="#333333"),
                ft.Container(height=20),
                boton_menu("NUEVO REGISTRO", "add_circle_outline", "#28A745", mostrar_formulario),
                ft.Container(height=10),
                boton_menu("VER HISTORIAL", "history", "#007BFF", mostrar_historial)
            ], alignment=ft.MainAxisAlignment.CENTER, horizontal_alignment=ft.CrossAxisAlignment.CENTER),
            alignment=ft.alignment.center
        )
        page.update()

    def mostrar_formulario(e):
        contenedor_pantalla.content = ft.Container(
            content=ft.Column([
                ft.TextButton("← Volver", on_click=mostrar_menu),
                ft.Text("Nuevo Parte", size=24, weight="bold"),
                ft.TextField(label="Fecha", value="26/06/2026"),
                ft.TextField(label="Nº Parte"),
                ft.TextField(label="Constructora"),
                ft.TextField(label="Lugar"),
                ft.TextField(label="Horas"),
                ft.TextField(label="Metros"),
                ft.TextField(label="Compañero"),
                ft.ElevatedButton("GUARDAR", icon="SAVE", on_click=mostrar_menu)
            ], scroll=ft.ScrollMode.AUTO),
            padding=20
        )
        page.update()

    def mostrar_historial(e):
        try:
            response = supabase.table("datos_app").select("*").execute()
            tarjetas = [
                ft.Card(
                    content=ft.Container(
                        content=ft.Column([
                            ft.Text(f"PARTE Nº: {item.get('n_parte', 'N/A')}", size=18, weight="bold", color="#007BFF"),
                            ft.Text(f"Fecha: {item.get('fecha', '')}", size=12, color="grey"),
                            ft.Divider(),
                            ft.Text(f"🏢 {item.get('constructora', 'N/A')}"),
                            ft.Text(f"📍 {item.get('lugar', 'N/A')}"),
                            ft.Text(f"⏱ {item.get('horas', '0')} hrs | 📏 {item.get('metros', '0')} m"),
                            ft.Text(f"👥 {item.get('companero', 'N/A')}"),
                        ], spacing=5, horizontal_alignment=ft.CrossAxisAlignment.START),
                        padding=15
                    )
                ) for item in response.data
            ]
        except:
            tarjetas = [ft.Text("Error al cargar datos")]

        contenedor_pantalla.content = ft.Container(
            content=ft.Column([
                ft.TextButton("← Volver", on_click=mostrar_menu),
                ft.Text("Historial de Partes", size=24, weight="bold"),
                ft.ListView(controls=tarjetas, expand=True, spacing=10)
            ], expand=True),
            padding=20
        )
        page.update()

    page.add(contenedor_pantalla)
    mostrar_menu()

ft.app(target=main, view=ft.AppView.WEB_BROWSER, port=int(os.environ.get("PORT", 8080)))