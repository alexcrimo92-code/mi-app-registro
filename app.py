import os
import flet as ft
from supabase import create_client

# --- CONFIGURACIÓN ---
URL = "https://bggzywzlusinkwwkwzgj.supabase.co"
KEY = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6ImJnZ3p5d3psdXNpbmt3d2t3emdqIiwicm9sZSI6ImFub24iLCJpYXQiOjE3ODI0MDMxNjMsImV4cCI6MjA5Nzk3OTE2M30.GtEiVvBZXeAYKap7YOK-CxNmUBHIoxxkJjVV4QyJp4c"
supabase = create_client(URL, KEY)



def main(page: ft.Page):
    page.title = "App Registro"
    page.theme_mode = "light"
    page.padding = 0
    page.assets_dir = "assets"
    
    # Capa de contenido (La que limpiaremos)
    contenido = ft.Column(alignment="center", horizontal_alignment="center", expand=True)
    
    # Stack principal
    contenedor_principal = ft.Stack(expand=True)
    contenedor_principal.controls.append(ft.Image(src="fondo.jpeg", fit="cover", expand=True))
    contenedor_principal.controls.append(ft.Container(bgcolor=ft.colors.with_opacity(0.5, "black"), expand=True))
    contenedor_principal.controls.append(contenido)
    
    page.add(contenedor_principal)

    def mostrar_menu(e=None):
        contenido.controls.clear()
        contenido.controls.extend([
            ft.Text("MENÚ PRINCIPAL", size=30, weight="bold", color="white"),
            ft.ElevatedButton("➕ NUEVO REGISTRO", on_click=mostrar_formulario),
            ft.ElevatedButton("📋 VER HISTORIAL", on_click=mostrar_historial)
        ])
        page.update()

    def mostrar_formulario(e):
        contenido.controls.clear()
        # Campos básicos para asegurar que no fallen
        f_fecha = ft.TextField(label="Fecha", value="26/06/2026", color="white")
        f_horas = ft.TextField(label="Horas", color="white")
        # ... (puedes agregar los demás campos aquí)
        
        contenido.controls.extend([
            ft.Text("Nuevo Registro", color="white", size=20),
            f_fecha, f_horas,
            ft.ElevatedButton("GUARDAR", on_click=lambda _: mostrar_menu()),
            ft.ElevatedButton("VOLVER", on_click=mostrar_menu)
        ])
        page.update()

    def mostrar_historial(e):
        contenido.controls.clear()
        # Lista con scroll
        lista = ft.Column(scroll="auto", expand=True, horizontal_alignment="center")
        contenido.controls.append(lista)
        
        # Botón volver al final (alineado a la derecha como pediste)
        contenido.controls.append(ft.Row([ft.ElevatedButton("🔙 VOLVER", on_click=mostrar_menu)], alignment="end"))
        page.update()

    mostrar_menu()

if __name__ == "__main__":
    ft.app(target=main, port=int(os.environ.get("PORT", 8080)))