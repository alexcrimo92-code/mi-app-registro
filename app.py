import flet as ft
from supabase import create_client

# --- CONFIGURACIÓN ---
URL = "https://bggzywzlusinkwwkwzgj.supabase.co"
KEY = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6ImJnZ3p5d3psdXNpbmt3d2t3emdqIiwicm9sZSI6ImFub24iLCJpYXQiOjE3ODI0MDMxNjMsImV4cCI6MjA5Nzk3OTE2M30.GtEiVvBZXeAYKap7YOK-CxNmUBHIoxxkJjVV4QyJp4c"
supabase = create_client(URL, KEY)





def main(page: ft.Page):
    page.title = "Registro de Trabajo"
    page.theme_mode = ft.ThemeMode.LIGHT
    
    # --- MENÚ DE INICIO ---
    btn_nuevo = ft.ElevatedButton("NUEVO PARTE", icon="add")
    
    # Creamos un contenedor simple para ver si renderiza
    layout = ft.Container(
        content=ft.Column([
            ft.Text("BIENVENIDO", size=30, weight="bold"),
            btn_nuevo
        ]),
        padding=50
    )

    # En lugar de usar page.views, usaremos page.add para descartar problemas de vistas
    page.add(layout)
    page.update()

# Ejecutar la app
ft.app(target=main, view=ft.AppView.WEB_BROWSER)