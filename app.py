import flet as ft
from supabase import create_client

# --- CONFIGURACIÓN ---
URL = "https://bggzywzlusinkwwkwzgj.supabase.co"
KEY = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6ImJnZ3p5d3psdXNpbmt3d2t3emdqIiwicm9sZSI6ImFub24iLCJpYXQiOjE3ODI0MDMxNjMsImV4cCI6MjA5Nzk3OTE2M30.GtEiVvBZXeAYKap7YOK-CxNmUBHIoxxkJjVV4QyJp4c"
supabase = create_client(URL, KEY)




def main(page: ft.Page):
    page.title = "Registro de Trabajo"
    page.theme_mode = ft.ThemeMode.LIGHT
    
    # --- VISTA 1: MENÚ DE INICIO ---
    def ir_a_formulario(e):
        page.views.append(vista_formulario)
        page.update()

    vista_inicio = ft.View(
        "/",
        [
            ft.AppBar(title=ft.Text("Inicio"), bgcolor="blue", color="white"),
            ft.Container(
                content=ft.Column([
                    ft.Text("Bienvenido", size=24, weight="bold"),
                    # Usamos el nombre del icono como texto para evitar errores de módulo
                    ft.ElevatedButton("NUEVO PARTE", icon="add", on_click=ir_a_formulario),
                ], alignment=ft.MainAxisAlignment.CENTER, horizontal_alignment=ft.CrossAxisAlignment.CENTER),
                padding=20
            )
        ]
    )

    # --- VISTA 2: FORMULARIO ---
    def volver_al_inicio(e):
        page.views.pop()
        page.update()

    vista_formulario = ft.View(
        "/formulario",
        [
            ft.AppBar(title=ft.Text("Nuevo Parte"), bgcolor="blue", color="white", 
                      leading=ft.IconButton("arrow_back", on_click=volver_al_inicio)),
            ft.Container(
                content=ft.Column([
                    ft.TextField(label="Fecha", value="26/06/2026"),
                    ft.TextField(label="Horas trabajadas"),
                    ft.TextField(label="Metros instalados"),
                    ft.TextField(label="Lugar"),
                    ft.TextField(label="Nº Parte"),
                    ft.TextField(label="Constructora"),
                    ft.TextField(label="Compañero"),
                    ft.ElevatedButton("GUARDAR PARTE", icon="save")
                ]),
                padding=20
            )
        ]
    )

    page.views.append(vista_inicio)
    page.update()

ft.app(target=main, view=ft.AppView.WEB_BROWSER)