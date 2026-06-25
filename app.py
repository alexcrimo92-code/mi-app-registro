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
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER

    # Fecha actual por defecto
    fecha_hoy = datetime.now().strftime("%d/%m/%Y")

    def input_field(label, valor_defecto=""):
        return ft.TextField(label=label, value=valor_defecto, width=300, border_radius=10, bgcolor="blue-grey-50")

    f_fecha = input_field("Fecha", valor_defecto=fecha_hoy)
    f_horas = input_field("Horas")
    f_metros = input_field("Metros")
    f_lugar = input_field("Lugar")
    f_n_parte = input_field("Nº Parte")
    f_constructora = input_field("Constructora")
    f_companero = input_field("Compañero")

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
        except: pass

    def guardar(e):
        supabase.table("datos_app").insert({
            "fecha": f_fecha.value, "horas": f_horas.value, "metros": f_metros.value,
            "lugar": f_lugar.value, "n_parte": f_n_parte.value, 
            "constructora": f_constructora.value, "companero": f_companero.value
        }).execute()
        # Opcional: limpiar campos menos la fecha
        for f in [f_horas, f_metros, f_lugar, f_n_parte, f_constructora, f_companero]:
            f.value = ""
        cargar_datos()

    page.add(
        ft.Column([
            ft.Text("Registro de Trabajo", size=25, weight="bold", color="blue-900"),
            f_fecha, f_horas, f_metros, f_lugar, f_n_parte, f_constructora, f_companero,
            ft.ElevatedButton("GUARDAR PARTE", icon="save", on_click=guardar, bgcolor="blue-700", color="white")
        ], alignment=ft.MainAxisAlignment.CENTER, horizontal_alignment=ft.CrossAxisAlignment.CENTER),
        ft.Divider(),
        ft.Row([tabla], scroll="always")
    )
    cargar_datos()

ft.app(target=main, view=ft.AppView.WEB_BROWSER)