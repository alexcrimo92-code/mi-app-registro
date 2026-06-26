import os
import flet as ft
from supabase import create_client

# --- CONFIGURACIÓN ---
URL = "https://bggzywzlusinkwwkwzgj.supabase.co"
KEY = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6ImJnZ3p5d3psdXNpbmt3d2t3emdqIiwicm9sZSI6ImFub24iLCJpYXQiOjE3ODI0MDMxNjMsImV4cCI6MjA5Nzk3OTE2M30.GtEiVvBZXeAYKap7YOK-CxNmUBHIoxxkJjVV4QyJp4c"
supabase = create_client(URL, KEY)


def main(page: ft.Page):
    # Configuración de la página para que se vea bien en móvil
    page.title = "App Registro"
    page.theme_mode = ft.ThemeMode.LIGHT
    page.bgcolor = "#F0F2F5"
    page.padding = 0

    # Contenedor principal donde cambiaremos de "pantalla"
    content_area = ft.Container(padding=20)

    def crear_boton(texto, icon, on_click, color="#007AFF"):
        return ft.ElevatedButton(
            content=ft.Row([ft.Icon(icon, color="white"), ft.Text(texto)], alignment=ft.MainAxisAlignment.CENTER),
            style=ft.ButtonStyle(bgcolor=color, color="white", padding=20),
            on_click=on_click
        )

    def mostrar_inicio(e=None):
        content_area.content = ft.Column([
            ft.Text("Bienvenido", size=30, weight="bold", color="#1C1C1E"),
            ft.Text("Registro de Trabajo", size=16, color="gray"),
            ft.Container(height=30),
            crear_boton("NUEVO REGISTRO", "add", mostrar_formulario),
            ft.Container(height=10),
            crear_boton("VER HISTORIAL", "history", mostrar_historial, color="#5856D6")
        ], alignment=ft.MainAxisAlignment.CENTER, horizontal_alignment=ft.CrossAxisAlignment.CENTER)
        page.update()

    def mostrar_formulario(e):
        # Campos con diseño mejorado
        campos = [
            ft.TextField(label="Fecha", value="26/06/2026", border_color="#007AFF"),
            ft.TextField(label="Horas", border_color="#007AFF"),
            ft.TextField(label="Lugar", border_color="#007AFF")
        ]
        content_area.content = ft.Column([
            ft.IconButton("arrow_back", on_click=mostrar_inicio),
            ft.Text("Nuevo Registro", size=24, weight="bold"),
            *campos,
            crear_boton("GUARDAR", "save", mostrar_inicio)
        ], spacing=20)
        page.update()

    def mostrar_historial(e):
        # Aquí cargaríamos los datos, pero primero definimos el diseño
        content_area.content = ft.Column([
            ft.IconButton("arrow_back", on_click=mostrar_inicio),
            ft.Text("Historial", size=24, weight="bold"),
            ft.Card(content=ft.Container(content=ft.Text("Registro #1: 8 horas - Gamiz"), padding=20)),
            ft.Card(content=ft.Container(content=ft.Text("Registro #2: 7 horas - Meco"), padding=20))
        ])
        page.update()

    page.add(content_area)
    mostrar_inicio()

ft.app(target=main, view=ft.AppView.WEB_BROWSER, port=int(os.environ.get("PORT", 8080)))