import flet as ft
from supabase import create_client

# --- CONFIGURACIÓN ---
URL = "https://bggzywzlusinkwwkwzgj.supabase.co"
KEY = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6ImJnZ3p5d3psdXNpbmt3d2t3emdqIiwicm9sZSI6ImFub24iLCJpYXQiOjE3ODI0MDMxNjMsImV4cCI6MjA5Nzk3OTE2M30.GtEiVvBZXeAYKap7YOK-CxNmUBHIoxxkJjVV4QyJp4c"
supabase = create_client(URL, KEY)

def main(page: ft.Page):
    # Diseño simplificado que funciona en versiones antiguas y nuevas
    page.title = "Registro de Trabajo"
    
    # Usamos iconos como texto plano ('save', 'person', etc.) para evitar errores de módulos
    txt_fecha = ft.TextField(label="Fecha", value="26/06/2026", icon="date_range")
    txt_horas = ft.TextField(label="Horas trabajadas", icon="access_time")
    
    def guardar(e):
        # Aquí iría tu lógica de guardar en Supabase
        page.update()

    page.add(
        ft.Text("Registro de Trabajo", size=20, weight="bold"),
        txt_fecha,
        txt_horas,
        ft.ElevatedButton("GUARDAR PARTE", icon="save", on_click=guardar)
    )

if __name__ == "__main__":
    ft.app(target=main)
