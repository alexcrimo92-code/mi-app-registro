import flet as ft
from supabase import create_client

# --- CONFIGURACIÓN ---
URL = "https://bggzywzlusinkwwkwzgj.supabase.co"
KEY = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6ImJnZ3p5d3psdXNpbmt3d2t3emdqIiwicm9sZSI6ImFub24iLCJpYXQiOjE3ODI0MDMxNjMsImV4cCI6MjA5Nzk3OTE2M30.GtEiVvBZXeAYKap7YOK-CxNmUBHIoxxkJjVV4QyJp4c"
supabase = create_client(URL, KEY)



def main(page: ft.Page):
    page.title = "Registro de Trabajo"
    page.theme_mode = ft.ThemeMode.LIGHT
    page.vertical_alignment = ft.MainAxisAlignment.START
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.bgcolor = "#F8F9FA" # Color de fondo gris claro

    # --- ELEMENTOS DEL MENÚ ---
    titulo = ft.Text("Menú Principal", size=24, weight="bold", color="#003366")
    
    # Botón grande para ir al formulario
    btn_nuevo = ft.ElevatedButton(
        "NUEVO REGISTRO", 
        icon="add", 
        width=250, 
        height=50,
        style=ft.ButtonStyle(bgcolor="#003366", color="white")
    )
    
    btn_historial = ft.ElevatedButton(
        "VER HISTORIAL", 
        icon="list", 
        width=250, 
        height=50
    )

    # Añadimos todo a la página
    page.add(
        ft.Container(height=20), # Espacio superior
        titulo,
        ft.Container(height=20),
        btn_nuevo,
        ft.Container(height=10),
        btn_historial
    )
    
    page.update()

ft.app(target=main, view=ft.AppView.WEB_BROWSER)