import os
import flet as ft
from supabase import create_client

# --- CONFIGURACIÓN ---
URL = "https://bggzywzlusinkwwkwzgj.supabase.co"
KEY = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6ImJnZ3p5d3psdXNpbmt3d2t3emdqIiwicm9sZSI6ImFub24iLCJpYXQiOjE3ODI0MDMxNjMsImV4cCI6MjA5Nzk3OTE2M30.GtEiVvBZXeAYKap7YOK-CxNmUBHIoxxkJjVV4QyJp4c"
supabase = create_client(URL, KEY)


def main(page: ft.Page):
    page.title = "Registro"
    page.theme_mode = ft.ThemeMode.LIGHT
    page.bgcolor = "#F8F9FA"

    # Contenedor central
    view_container = ft.Container(expand=True, padding=10)

    def mostrar_menu():
        view_container.content = ft.Column([
            ft.Text("Menú Principal", size=24, weight="bold"),
            ft.ElevatedButton("NUEVO REGISTRO", icon="ADD", on_click=lambda e: mostrar_formulario()),
            ft.ElevatedButton("VER HISTORIAL", icon="LIST", on_click=lambda e: mostrar_historial())
        ], alignment=ft.MainAxisAlignment.CENTER, horizontal_alignment=ft.CrossAxisAlignment.CENTER)
        page.update()

    def mostrar_formulario():
        view_container.content = ft.Column([
            ft.IconButton(icon="ARROW_BACK", icon_color="blue", on_click=lambda e: mostrar_menu()),
            ft.Text("Nuevo Registro", size=20, weight="bold"),
            ft.TextField(label="Fecha", value="26/06/2026"),
            ft.TextField(label="Horas"),
            ft.TextField(label="Lugar"),
            ft.ElevatedButton("GUARDAR", icon="SAVE", on_click=lambda e: mostrar_menu())
        ])
        page.update()

    def mostrar_historial():
        # Simulamos carga de datos para asegurar estructura
        cards = [
            ft.Card(content=ft.Container(content=ft.Text("PARTE: 861 | Gamiz", weight="bold"), padding=15)),
            ft.Card(content=ft.Container(content=ft.Text("PARTE: 862 | Meco", weight="bold"), padding=15))
        ]
        
        view_container.content = ft.Column([
            ft.IconButton(icon="ARROW_BACK", icon_color="blue", on_click=lambda e: mostrar_menu()),
            ft.Text("Historial de Partes", size=20, weight="bold"),
            ft.ListView(controls=cards, expand=True, spacing=10)
        ], expand=True)
        page.update()

    page.add(view_container)
    mostrar_menu()

ft.app(target=main, view=ft.AppView.WEB_BROWSER, port=int(os.environ.get("PORT", 8080)))