import flet as ft
from supabase import create_client
from datetime import datetime


# --- CONFIGURACIÓN ---
URL = "https://bggzywzlusinkwwkwzgj.supabase.co"
KEY = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6ImJnZ3p5d3psdXNpbmt3d2t3emdqIiwicm9sZSI6ImFub24iLCJpYXQiOjE3ODI0MDMxNjMsImV4cCI6MjA5Nzk3OTE2M30.GtEiVvBZXeAYKap7YOK-CxNmUBHIoxxkJjVV4QyJp4c"
supabase = create_client(URL, KEY)


def main(page: ft.Page):
    page.title = "Registro de Trabajo"
    page.theme_mode = ft.ThemeMode.LIGHT
    page.bgcolor = "#F8F9FA"

    # --- CAMPOS (Iconos universales) ---
    f_fecha = ft.TextField(label="Fecha", value="26/06/2026", icon=ft.icons.CALENDAR_TODAY)
    f_horas = ft.TextField(label="Horas trabajadas", icon=ft.icons.ACCESS_TIME, expand=True)
    f_metros = ft.TextField(label="Metros instalados", icon=ft.icons.LINEAR_SCALE, expand=True)
    f_lugar = ft.TextField(label="Lugar", icon=ft.icons.LOCATION_ON)
    f_n_parte = ft.TextField(label="Nº Parte", icon=ft.icons.TAG, expand=True)
    f_constructora = ft.TextField(label="Constructora", icon=ft.icons.BUSINESS, expand=True)
    f_companero = ft.TextField(label="Compañero", icon=ft.icons.PERSON)

    # --- TABLA ---
    tabla = ft.DataTable(
        columns=[
            ft.DataColumn(ft.Text("Lugar")), 
            ft.DataColumn(ft.Text("Horas")), 
            ft.DataColumn(ft.Text("Metros"))
        ],
        rows=[]
    )

    def cargar_datos(e=None):
        try:
            response = supabase.table("datos_app").select("*").execute()
            tabla.rows.clear()
            for i in response.data:
                tabla.rows.append(ft.DataRow(cells=[
                    ft.DataCell(ft.Text(i.get("lugar", ""))),
                    ft.DataCell(ft.Text(f"{i.get('horas', '')} horas")),
                    ft.DataCell(ft.Text(i.get("metros", ""))),
                ]))
            page.update()
        except Exception as e:
            print(f"Error cargando: {e}")

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
            # Limpiar campos después de guardar
            for f in [f_horas, f_metros, f_lugar, f_n_parte, f_constructora, f_companero]:
                f.value = ""
            cargar_datos()
        except Exception as e:
            print(f"Error guardando: {e}")

    # --- ESTRUCTURA VISUAL ---
    page.add(
        ft.Container(
            content=ft.Text("Registro de Trabajo", size=24, weight="bold", color="white"),
            bgcolor="#003366", padding=20, border_radius=ft.border_radius.only(bottom_left=20, bottom_right=20)
        ),
        ft.Container(
            content=ft.Column([
                f_fecha,
                ft.Row([f_horas, f_metros]),
                f_lugar,
                ft.Row([f_n_parte, f_constructora]),
                f_companero,
                ft.ElevatedButton("GUARDAR PARTE", icon=ft.icons.SAVE, on_click=guardar, 
                                 style=ft.ButtonStyle(bgcolor="#0D47A1", color="white"))
            ]),
            padding=20, bgcolor="white", border_radius=15
        ),
        ft.Container(
            content=ft.Column([
                ft.Text("Partes registrados", size=18, weight="bold"),
                ft.SingleChildScrollView(content=tabla)
            ]),
            padding=20, bgcolor="white", border_radius=15, margin=ft.margin.only(top=10)
        )
    )
    cargar_datos()

# Esta es la forma más estable de lanzar Flet
if __name__ == "__main__":
    ft.app(target=main)