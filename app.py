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
                                ft.ListTile(
                                    leading=ft.Icon("work"),
                                    title=ft.Text(f"Nº Parte: {item.get('n_parte', 'N/A')}", text_align="center"),
                                    subtitle=ft.Text(f"Fecha: {item.get('fecha', '')}", text_align="center"),
                                ),
                                ft.Container(
                                    content=ft.Column([
                                        ft.Text(f"Constructora: {item.get('constructora', '')}", text_align="center"),
                                        ft.Text(f"Lugar: {item.get('lugar', '')}", text_align="center"),
                                        ft.Text(f"Horas: {item.get('horas', '')} | Metros: {item.get('metros', '')}", text_align="center"),
                                        ft.Text(f"Compañero: {item.get('companero', '')}", text_align="center"),
                                    ], 
                                    alignment=ft.MainAxisAlignment.CENTER, 
                                    horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                                    spacing=5),
                                    padding=10
                                )
                            ], alignment=ft.MainAxisAlignment.CENTER, horizontal_alignment=ft.CrossAxisAlignment.CENTER),
                            padding=10
                        )
                    )
                )
        except Exception as ex:
            tarjetas = [ft.Text(f"Error al cargar datos: {ex}")]

        page.add(
            ft.Container(
                content=ft.Column([
                    ft.AppBar(title=ft.Text("Historial"), bgcolor="blue", color="white", 
                              leading=ft.IconButton("arrow_back", on_click=mostrar_inicio)),
                    ft.ElevatedButton("VOLVER AL MENÚ", icon="home", on_click=mostrar_inicio),
                    ft.ListView(controls=tarjetas, expand=True, spacing=10)
                ], expand=True),
                padding=20,
                expand=True
            )
        )
        page.update()

    # Inicializar App
    mostrar_inicio()

# Lanza la aplicación
ft.app(target=main, view=ft.AppView.WEB_BROWSER, port=int(os.environ.get("PORT", 8080)))