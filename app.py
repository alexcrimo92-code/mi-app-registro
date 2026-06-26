import flet as ft
from supabase import create_client

# --- CONFIGURACIÓN ---
URL = "https://bggzywzlusinkwwkwzgj.supabase.co"
KEY = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6ImJnZ3p5d3psdXNpbmt3d2t3emdqIiwicm9sZSI6ImFub24iLCJpYXQiOjE3ODI0MDMxNjMsImV4cCI6MjA5Nzk3OTE2M30.GtEiVvBZXeAYKap7YOK-CxNmUBHIoxxkJjVV4QyJp4c"
supabase = create_client(URL, KEY)


def main(page: ft.Page):
    page.title = "Registro de Trabajo"
    page.theme_mode = ft.ThemeMode.LIGHT
    page.padding = 0

    # --- FUNCIONES DE NAVEGACIÓN ---
    def ir_a_formulario(e):
        page.views.append(vista_formulario)
        page.update()

    def volver_al_inicio(e):
        page.views.pop()
        page.update()

    # --- VISTA 1: MENÚ DE INICIO ---
    vista_inicio = ft.View(
        "/",
        [
            ft.AppBar(title=ft.Text("Inicio"), bgcolor=ft.colors.BLUE_900, color="white"),
            ft.Container(
                content=ft.Column([
                    ft.Text("Bienvenido", size=24, weight="bold"),
                    ft.ElevatedButton("NUEVO PARTE", icon=ft.icons.ADD, on_click=ir_a_formulario),
                    ft.ElevatedButton("VER HISTORIAL", icon=ft.icons.LIST)
                ], alignment=ft.MainAxisAlignment.CENTER, horizontal_alignment=ft.CrossAxisAlignment.CENTER),
                padding=20
            )
        ]
    )

    # --- VISTA 2: FORMULARIO ---
    f_fecha = ft.TextField(label="Fecha", value="26/06/2026")
    f_horas = ft.TextField(label="Horas trabajadas")
    
    vista_formulario = ft.View(
        "/formulario",
        [
            ft.AppBar(title=ft.Text("Nuevo Parte"), bgcolor=ft.colors.BLUE_900, color="white", 
                      leading=ft.IconButton(ft.icons.ARROW_BACK, on_click=volver_al_inicio)),
            ft.Container(
                content=ft.Column([
                    f_fecha, f_horas,
                    ft.ElevatedButton("GUARDAR PARTE", on_click=lambda e: print("Guardado"))
                ]),
                padding=20
            )
        ]
    )

    page.views.append(vista_inicio)
    page.update()

# Para evitar el error, asegúrate de tener instalado flet actualizado: 
# pip install flet --upgrade
ft.app(target=main, view=ft.AppView.WEB_BROWSER)