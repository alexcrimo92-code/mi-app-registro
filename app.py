import os
import flet as ft
from supabase import create_client

# --- CONFIGURACIÓN ---
URL = "https://bggzywzlusinkwwkwzgj.supabase.co"
KEY = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6ImJnZ3p5d3psdXNpbmt3d2t3emdqIiwicm9sZSI6ImFub24iLCJpYXQiOjE3ODI0MDMxNjMsImV4cCI6MjA5Nzk3OTE2M30.GtEiVvBZXeAYKap7YOK-CxNmUBHIoxxkJjVV4QyJp4c"
supabase = create_client(URL, KEY)


def main(page: ft.Page):
    # Configuración de la página
    page.title = "App Registro"
    page.theme_mode = ft.ThemeMode.LIGHT
    page.bgcolor = "#F0F2F5"
    page.padding = 10

    # Contenedor principal que controla el cambio de vistas
    main_view = ft.Container(expand=True)

    def cambiar_vista(contenido):
        main_view.content = contenido
        page.update()

    def mostrar_inicio(e=None):
        cambiar_vista(ft.Column([
            ft.Text("Bienvenido", size=30, weight="bold", color="#1C1C1E"),
            ft.Text("Registro de Trabajo", size=16, color="gray"),
            ft.Container(height=40),
            ft.ElevatedButton("NUEVO REGISTRO", icon="ADD", on_click=mostrar_formulario),
            ft.ElevatedButton("VER HISTORIAL", icon="HISTORY", on_click=mostrar_historial)
        ], alignment=ft.MainAxisAlignment.CENTER, horizontal_alignment=ft.CrossAxisAlignment.CENTER))

    def mostrar_formulario(e):
        cambiar_vista(ft.Column([
            ft.IconButton(icon="ARROW_BACK", on_click=mostrar_inicio),
            ft.Text("Nuevo Registro", size=24, weight="bold"),
            ft.TextField(label="Fecha", value="26/06/2026"),
            ft.TextField(label="Horas"),
            ft.TextField(label="Lugar"),
            ft.ElevatedButton("GUARDAR", icon="SAVE", on_click=mostrar_inicio)
        ], spacing=20))

    def mostrar_historial(e):
        # Usamos Column dentro de una Card para que se vea estructurado
        cambiar_vista(ft.Column([
            ft.IconButton(icon="ARROW_BACK", on_click=mostrar_inicio),
            ft.Text("Historial", size=24, weight="bold"),
            ft.Card(content=ft.Container(content=ft.Text("Registro #1: 8 horas - Gamiz"), padding=20)),
            ft.Card(content=ft.Container(content=ft.Text("Registro #2: 7 horas - Meco"), padding=20))
        ]))

    # Añadimos la vista principal a la página
    page.add(main_view)
    mostrar_inicio()

ft.app(target=main, view=ft.AppView.WEB_BROWSER, port=int(os.environ.get("PORT", 8080)))