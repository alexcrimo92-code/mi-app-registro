import flet as ft
from supabase import create_client

# --- CONFIGURACIÓN ---
URL = "https://bggzywzlusinkwwkwzgj.supabase.co"
KEY = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6ImJnZ3p5d3psdXNpbmt3d2t3emdqIiwicm9sZSI6ImFub24iLCJpYXQiOjE3ODI0MDMxNjMsImV4cCI6MjA5Nzk3OTE2M30.GtEiVvBZXeAYKap7YOK-CxNmUBHIoxxkJjVV4QyJp4c"
supabase = create_client(URL, KEY)

def main(page: ft.Page):
    page.title = "Registro de Partes"
    page.scroll = "adaptive"

    # Campos de entrada
    f_fecha = ft.TextField(label="Fecha")
    f_horas = ft.TextField(label="Horas")
    f_metros = ft.TextField(label="Metros")
    f_lugar = ft.TextField(label="Lugar")
    f_n_parte = ft.TextField(label="Nº Parte")
    f_constructora = ft.TextField(label="Constructora")
    f_companero = ft.TextField(label="Compañero")

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
            # Seleccionamos * para traer todas las columnas nuevas
            response = supabase.table("datos_app").select("*").execute()
            tabla.rows.clear()
            for item in response.data:
                tabla.rows.append(ft.DataRow(cells=[
                    ft.DataCell(ft.Text(str(item.get("fecha", "-")))),
                    ft.DataCell(ft.Text(str(item.get("lugar", "-")))),
                    ft.DataCell(ft.Text(str(item.get("horas", "-")))),
                    ft.DataCell(ft.Text(str(item.get("metros", "-")))),
                ]))
            page.update()
        except Exception as e:
            print(f"Error: {e}")

    def guardar(e):
        try:
            datos = {
                "fecha": f_fecha.value,
                "horas": f_horas.value,
                "metros": f_metros.value,
                "lugar": f_lugar.value,
                "n_parte": f_n_parte.value,
                "constructora": f_constructora.value,
                "companero": f_companero.value
            }
            supabase.table("datos_app").insert(datos).execute()
            # Limpiar campos
            f_fecha.value = f_horas.value = f_metros.value = ""
            f_lugar.value = f_n_parte.value = f_constructora.value = f_companero.value = ""
            cargar_datos()
        except Exception as e:
            print(f"Error al guardar: {e}")

    page.add(
        ft.Text("NUEVO PARTE", size=20, weight="bold"),
        f_fecha, f_horas, f_metros, f_lugar, f_n_parte, f_constructora, f_companero,
        ft.ElevatedButton("GUARDAR PARTE", on_click=guardar),
        ft.Divider(),
        tabla
    )
    cargar_datos()

ft.app(target=main, view=ft.AppView.WEB_BROWSER)