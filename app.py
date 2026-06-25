import flet as ft
from supabase import create_client

# --- CONFIGURACIÓN ---
URL = "https://bggzywzlusinkwwkwzgj.supabase.co"
KEY = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6ImJnZ3p5d3psdXNpbmt3d2t3emdqIiwicm9sZSI6ImFub24iLCJpYXQiOjE3ODI0MDMxNjMsImV4cCI6MjA5Nzk3OTE2M30.GtEiVvBZXeAYKap7YOK-CxNmUBHIoxxkJjVV4QyJp4c"
supabase = create_client(URL, KEY)

def main(page: ft.Page):
    page.title = "Sistema de Partes"
    page.theme_mode = ft.ThemeMode.LIGHT
    page.padding = 20
    page.scroll = "adaptive"

    # Campos con estilo
    def input_field(label):
        return ft.TextField(label=label, border_radius=10, bgcolor=ft.colors.BLUE_GREY_50)

    f_fecha = input_field("Fecha")
    f_horas = input_field("Horas")
    f_metros = input_field("Metros")
    f_lugar = input_field("Lugar")
    f_n_parte = input_field("Nº Parte")
    f_constructora = input_field("Constructora")
    f_companero = input_field("Compañero")

    tabla = ft.DataTable(
        columns=[
            ft.DataColumn(ft.Text("Fecha", weight="bold")),
            ft.DataColumn(ft.Text("Lugar", weight="bold")),
            ft.DataColumn(ft.Text("Horas", weight="bold")),
            ft.DataColumn(ft.Text("Metros", weight="bold")),
        ],
        rows=[]
    )

    def guardar(e):
        datos = {
            "fecha": f_fecha.value, "horas": f_horas.value, "metros": f_metros.value,
            "lugar": f_lugar.value, "n_parte": f_n_parte.value, 
            "constructora": f_constructora.value, "companero": f_companero.value
        }
        supabase.table("datos_app").insert(datos).execute()
        # Limpiar
        for f in [f_fecha, f_horas, f_metros, f_lugar, f_n_parte, f_constructora, f_companero]:
            f.value = ""
        cargar_datos()

    def cargar_datos(e=None):
        response = supabase.table("datos_app").select("*").execute()
        tabla.rows = [
            ft.DataRow(cells=[
                ft.DataCell(ft.Text(i.get("fecha"))),
                ft.DataCell(ft.Text(i.get("lugar"))),
                ft.DataCell(ft.Text(i.get("horas"))),
                ft.DataCell(ft.Text(i.get("metros"))),
            ]) for i in response.data
        ]
        page.update()

    # Layout Profesional
    page.add(
        ft.Container(
            content=ft.Column([
                ft.Text("Registro de Trabajo", size=28, weight="w900", color=ft.colors.BLUE_900),
                ft.Row([f_fecha, f_horas, f_metros]),
                f_lugar,
                ft.Row([f_n_parte, f_constructora, f_companero]),
                ft.ElevatedButton("GUARDAR PARTE", icon=ft.icons.SAVE_ALT, on_click=guardar, bgcolor=ft.colors.BLUE_700, color="white"),
            ]),
            padding=20,
            border=ft.border.all(1, ft.colors.BLUE_100),
            border_radius=15
        ),
        ft.Divider(height=40),
        ft.Text("Historial de Partes", size=20, weight="bold"),
        ft.Container(content=tabla, border=ft.border.all(1, ft.colors.GREY_300), border_radius=10)
    )
    cargar_datos()

ft.app(target=main, view=ft.AppView.WEB_BROWSER)