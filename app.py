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

    # --- CONTENEDOR PRINCIPAL ---
    contenedor_principal = ft.Container()

    # --- FUNCIÓN: IR AL FORMULARIO ---
    def mostrar_formulario(e):
        contenedor_principal.content = ft.Container(
            content=ft.Column([
                ft.AppBar(title=ft.Text("Nuevo Parte"), bgcolor="blue", color="white", 
                          leading=ft.IconButton("arrow_back", on_click=mostrar_inicio)),
                ft.TextField(label="Fecha", value="26/06/2026"),
                ft.TextField(label="Horas trabajadas"),
                ft.TextField(label="Metros"),
                ft.ElevatedButton("GUARDAR PARTE", icon="save")
            ]),
            padding=20 # El padding va aquí, en el contenedor
        )
        page.update()

    # --- FUNCIÓN: IR AL INICIO ---
    def mostrar_inicio(e):
        contenedor_principal.content = ft.Container(
            content=ft.Column([
                ft.Text("Menú Principal", size=24, weight="bold"),
                ft.ElevatedButton("NUEVO REGISTRO", icon="add", on_click=mostrar_formulario),
                ft.ElevatedButton("VER HISTORIAL", icon="list")
            ], alignment=ft.MainAxisAlignment.CENTER, horizontal_alignment=ft.CrossAxisAlignment.CENTER),
            padding=50 # El padding va aquí
        )
        page.update()

    # --- INICIO ---
    page.add(contenedor_principal)
    mostrar_inicio(None)

ft.app(target=main, view=ft.AppView.WEB_BROWSER)