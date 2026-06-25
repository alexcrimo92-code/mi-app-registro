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

    # Campos de entrada
    f_fecha = ft.TextField(label="Fecha", border_radius=10)
    f_horas = ft.TextField(label="Horas", border_radius=10)
    f_metros = ft.TextField(label="Metros", border_radius=10)
    f_lugar = ft.TextField(label="Lugar", border_radius=10)
    f_n_parte = ft.TextField(label="Nº Parte", border_radius=10)
    f_constructora = ft.TextField(label="Constructora", border_radius=10)
    f_companero = ft.TextField(label="Compañero", border_radius=10)

    # Tabla
    tabla = ft.DataTable(
        columns=[
            ft.DataColumn(ft.Text("Fecha")),
            ft.DataColumn(ft.Text("Lugar")),
            ft.DataColumn(ft.Text("Horas")),
            ft.DataColumn(ft.Text("Metros")),
        ],
        rows=[]
    )

    def cargar_datos(e=None):
        try:
            response = supabase.table("datos_app").select("*").execute()
            tabla.rows = [
                ft.DataRow(cells=[
                    ft.DataCell(ft.Text(str(i.get("fecha", "")))),
                    ft.DataCell(ft.Text(str(i.get("lugar", "")))),
                    ft.DataCell(ft.Text(str(i.get("horas", "")))),
                    ft.DataCell(ft.Text(str(i.get("metros", "")))),
                ]) for i in response.data
            ]
            page.update()
        except:
            pass

    def guardar(e):
        datos = {
            "fecha": f_fecha.value, "horas": f_horas.value, "metros": f_metros.value,
            "lugar": f_lugar.value, "n_parte": f_n_parte.value, 
            "constructora": f_constructora.value, "companero": f_companero.value
        }
        supabase.table("datos_app").insert(datos).execute()
        for f in [f_fecha, f_horas, f_metros, f_lugar, f_n_parte, f_constructora, f_companero]:
            f.value = ""
        cargar_datos()

    # Layout usando texto simple para colores/iconos para evitar errores de atributos
    page.add(
        ft.Column([
            ft.Text("Registro de Trabajo", size=25, weight="bold"),
            f_fecha, f_horas, f_metros, f_lugar, f_n_parte, f_constructora, f_companero,
            ft.ElevatedButton("GUARDAR PARTE", icon="save", on_click=guardar)
        ]),
        ft.Divider(),
        ft.Text("Historial"),
        tabla
    )
    cargar_datos()

ft.app(target=main, view=ft.AppView.WEB_BROWSER)