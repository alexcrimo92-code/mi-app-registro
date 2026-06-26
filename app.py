import os
import flet as ft
from supabase import create_client

# --- CONFIGURACIÓN ---
URL = "https://bggzywzlusinkwwkwzgj.supabase.co"
KEY = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6ImJnZ3p5d3psdXNpbmt3d2t3emdqIiwicm9sZSI6ImFub24iLCJpYXQiOjE3ODI0MDMxNjMsImV4cCI6MjA5Nzk3OTE2M30.GtEiVvBZXeAYKap7YOK-CxNmUBHIoxxkJjVV4QyJp4c"
supabase = create_client(URL, KEY)


def main(page: ft.Page):
    page.title = "App Registro"
    page.theme_mode = ft.ThemeMode.LIGHT
    page.bgcolor = "#FFFFFF" # Fondo blanco limpio

    # Contenedor que hará de "pantalla"
    contenedor_pantalla = ft.Container(padding=20)
    
    def mostrar_menu():
        contenedor_pantalla.content = ft.Column([
            ft.Text("Menú Principal", size=24, weight="bold"),
            ft.ElevatedButton("NUEVO REGISTRO", on_click=lambda _: mostrar_formulario()),
            ft.ElevatedButton("VER HISTORIAL", on_click=lambda _: mostrar_historial())
        ], horizontal_alignment=ft.CrossAxisAlignment.CENTER)
        page.update()

    def mostrar_formulario():
        contenedor_pantalla.content = ft.Column([
            # Usamos un botón con texto en lugar de solo icono para evitar el error rojo
            ft.TextButton("← Volver", on_click=lambda _: mostrar_menu()),
            ft.Text("Nuevo Registro", size=20, weight="bold"),
            ft.TextField(label="Fecha", value="26/06/2026"),
            ft.TextField(label="Horas"),
            ft.TextField(label="Lugar"),
            ft.ElevatedButton("GUARDAR", on_click=lambda _: mostrar_menu())
        ])
        page.update()

    def mostrar_historial():
        # Simulamos datos para probar que la lista no se rompa
        items = ["Parte 861 - Gamiz", "Parte 862 - Meco"]
        controles = [ft.Card(content=ft.Container(content=ft.Text(i), padding=20)) for i in items]
        
        contenedor_pantalla.content = ft.Column([
            ft.TextButton("← Volver", on_click=lambda _: mostrar_menu()),
            ft.Text("Historial", size=20, weight="bold"),
            ft.Column(controls=controles)
        ])
        page.update()

    page.add(contenedor_pantalla)
    mostrar_menu()

ft.app(target=main, view=ft.AppView.WEB_BROWSER, port=int(os.environ.get("PORT", 8080)))80)))