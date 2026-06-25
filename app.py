import flet as ft
from supabase import create_client

# --- CONFIGURACIÓN ---
URL = "https://bggzywzlusinkwwkwzgj.supabase.co"
KEY = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6ImJnZ3p5d3psdXNpbmt3d2t3emdqIiwicm9sZSI6ImFub24iLCJpYXQiOjE3ODI0MDMxNjMsImV4cCI6MjA5Nzk3OTE2M30.GtEiVvBZXeAYKap7YOK-CxNmUBHIoxxkJjVV4QyJp4c"
supabase = create_client(URL, KEY)

def main(page: ft.Page):
    page.title = "Gestor de Partes"
    page.scroll = "adaptive"
    page.padding = 20

    # --- CAMPOS ---
    f_fecha = ft.TextField(label="Fecha", width=140)
    f_horas = ft.TextField(label="Horas", width=140)
    f_metros = ft.TextField(label="Metros", width=140)
    f_lugar = ft.TextField(label="Lugar")
    f_n_parte = ft.TextField(label="Nº Parte", width=140)
    f_constructora = ft.TextField(label="Constructora")
    f_companero = ft.TextField(label="Compañero")

    # --- TABLA ---
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
            tabla.rows.clear()
            for item in response.data:
                tabla.rows.append(ft.DataRow(cells=[
                    ft.DataCell(ft.Text(item.get("fecha", "-"))),
                    ft.DataCell(ft.Text(item.get("lugar", "-"))),
                    ft.DataCell(ft.Text(item.get("horas", "-"))),
                    ft.DataCell(ft.Text(item.get("metros", "-"))),
                ]))
            page.update()
        except Exception as e:
            print(f"Error: {e}")

    def guardar(e):
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
        for campo in [f_fecha, f_horas, f_metros, f_lugar, f_n_parte, f_constructora, f_companero]:
            campo.value = ""
        
        cargar_datos()

    # --- INTERFAZ ---
    page.add(
        ft.Text("NUEVO PARTE DE TRABAJO", size=22, weight="bold"),
        ft.Row([f_fecha, f_horas, f_metros]),
        f_lugar,
        ft.Row([f_n_parte, f_companero]),
        f_constructora,
        ft.ElevatedButton("GUARDAR PARTE", on_click=guardar, icon=ft.icons.SAVE),
        ft.Divider(),
        ft.Text("RESUMEN DE PARTES", size=18, weight="bold"),
        ft.Column([tabla], scroll="adaptive") # Esto permite que la tabla tenga scroll horizontal
    )
    
    cargar_datos()

ft.app(target=main, view=ft.AppView.WEB_BROWSER)