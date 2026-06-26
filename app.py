import os
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

    # --- CAMPOS DEL FORMULARIO ---
    f_fecha = ft.TextField(label="Fecha", value="26/06/2026")
    f_horas = ft.TextField(label="Horas")
    f_metros = ft.TextField(label="Metros")
    f_lugar = ft.TextField(label="Lugar")
    f_n_parte = ft.TextField(label="Nº Parte")
    f_constructora = ft.TextField(label="Constructora")
    f_companero = ft.TextField(label="Compañero")

    # --- FUNCIONES DE NAVEGACIÓN ---

    def mostrar_inicio(e=None):
        page.clean()
        page.add(
            ft.Container(
                content=ft.Column([
                    ft.Text("Menú Principal", size=24, weight="bold"),
                    ft.ElevatedButton("NUEVO REGISTRO", icon="add", on_click=mostrar_formulario),
                    ft.ElevatedButton("VER HISTORIAL", icon="list", on_click=mostrar_historial)
                ], alignment=ft.MainAxisAlignment.CENTER, horizontal_alignment=ft.CrossAxisAlignment.CENTER),
                padding=50
            )
        )
        page.update()

    def mostrar_formulario(e):
        page.clean()
        page.add(
            ft.Container(
                content=ft.Column([
                    ft.AppBar(title=ft.Text("Nuevo Parte"), bgcolor="blue", color="white", 
                              leading=ft.IconButton("arrow_back", on_click=mostrar_inicio)),
                    f_fecha, f_horas, f_metros, f_lugar, f_n_parte, f_constructora, f_companero,
                    ft.ElevatedButton("GUARDAR PARTE", icon="save", on_click=guardar_y_volver),
                    ft.OutlinedButton("CANCELAR", icon="close", on_click=mostrar_inicio)
                ], scroll=ft.ScrollMode.AUTO),
                padding=20
            )
        )
        page.update()

    def guardar_y_volver(e):
        datos = {
            "fecha": f_fecha.value, "horas": f_horas.value, "metros": f_metros.value,
            "lugar": f_lugar.value, "n_parte": f_n_parte.value, 
            "constructora": f_constructora.value, "companero": f_companero.value
        }
        supabase.table("datos_app").insert(datos).execute()
        mostrar_inicio()

    def mostrar_historial(e):
        page.clean()
        try:
            response = supabase.table("datos_app").select("*").execute()
            tarjetas = []
            for item in response.data:
                tarjetas.append(
                    ft.Card(
                        content=ft.Container(
                            content=ft.Column([
                                ft.Text(f"PARTE Nº: {item.get('n_parte', 'N/A')}", size=20, weight="bold", color="blue"),
                                ft.Text(f"Fecha: {item.get('fecha', '')}", size=14, color="grey"),
                                ft.Divider(height=1, color="grey"),
                                ft.Column([
                                    ft.Text(f"🏢 {item.get('constructora', 'N/A')}", size=16),
                                    ft.Text(f"📍 {item.get('lugar', 'N/A')}", size=16),
                                    ft.Text(f"⏱ {item.get('horas', '0')} hrs | 📏 {item.get('metros', '0')} m", size=16, weight="w500"),
                                    ft.Text(f"👥 {item.get('companero', 'N/A')}", size=16),
                                ], spacing=8, horizontal_alignment=ft.CrossAxisAlignment.START),
                            ], spacing=10, horizontal_alignment=ft.CrossAxisAlignment.CENTER),
                            padding=20
                        )
                    )
                )
        except Exception as ex:
            tarjetas = [ft.Text(f"Error: {ex}")]

        page.add(
            ft.Container(
                content=ft.Column([
                    ft.AppBar(title=ft.Text("Historial de Partes"), bgcolor="blue", color="white", 
                              leading=ft.IconButton("arrow_back", on_click=mostrar_inicio)),
                    ft.ElevatedButton("VOLVER AL MENÚ", icon="home", on_click=mostrar_inicio),
                    ft.ListView(controls=tarjetas, expand=True, spacing=15)
                ], expand=True),
                padding=10,
                expand=True
            )
        )
        page.update()

    # Inicializar App
    mostrar_inicio()

# Lanza la aplicación
ft.app(target=main, view=ft.AppView.WEB_BROWSER, port=int(os.environ.get("PORT", 8080)))