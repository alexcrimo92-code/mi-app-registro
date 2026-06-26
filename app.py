import flet as ft
from supabase import create_client

# --- CONFIGURACIÓN ---
URL = "https://bggzywzlusinkwwkwzgj.supabase.co"
KEY = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6ImJnZ3p5d3psdXNpbmt3d2t3emdqIiwicm9sZSI6ImFub24iLCJpYXQiOjE3ODI0MDMxNjMsImV4cCI6MjA5Nzk3OTE2M30.GtEiVvBZXeAYKap7YOK-CxNmUBHIoxxkJjVV4QyJp4c"
supabase = create_client(URL, KEY)

def main(page: ft.Page):
    page.title = "PARTES DE TRABAJO"
    page.theme_mode = ft.ThemeMode.LIGHT
    page.bgcolor = "#F8F9FA"

    # Campos de texto con iconos estándar (strings) para evitar errores de versión
    f_fecha = ft.TextField(label="Fecha", value="26/06/2026", icon="date_range")
    f_horas = ft.TextField(label="Horas trabajadas", icon="access_time")
    f_metros = ft.TextField(label="Metros instalados", icon="reorder")
    f_lugar = ft.TextField(label="Lugar", icon="location_on")
    f_n_parte = ft.TextField(label="Nº Parte", icon="tag")
    f_constructora = ft.TextField(label="Constructora", icon="business")
    f_companero = ft.TextField(label="Compañero", icon="person")

    # Tabla para mostrar registros
    tabla = ft.DataTable(
        columns=[
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
            for i in response.data:
                tabla.rows.append(ft.DataRow(cells=[
                    ft.DataCell(ft.Text(i.get("lugar", ""))),
                    ft.DataCell(ft.Text(str(i.get("horas", "")))),
                    ft.DataCell(ft.Text(str(i.get("metros", "")))),
                ]))
            page.update()
        except:
            pass

    def guardar(e):
        try:
            supabase.table("datos_app").insert({
                "fecha": f_fecha.value,
                "horas": f_horas.value,
                "metros": f_metros.value,
                "lugar": f_lugar.value,
                "n_parte": f_n_parte.value,
                "constructora": f_constructora.value,
                "companero": f_companero.value
            }).execute()
            # Limpiar campos
            for campo in [f_horas, f_metros, f_lugar, f_n_parte, f_constructora, f_companero]:
                campo.value = ""
            cargar_datos()
        except Exception as err:
            print(f"Error al guardar: {err}")

    # Estructura visual con componentes básicos (compatibles con todo)
    page.add(
        ft.Container(
            content=ft.Text("PARTES DE TRABAJO", size=20, color="white", weight="bold"),
            bgcolor="#003366", padding=20, border_radius=10
        ),
        ft.Container(
            content=ft.Column([
                f_fecha, f_horas, f_metros, f_lugar, f_n_parte, f_constructora, f_companero,
                ft.ElevatedButton("GUARDAR PARTE", icon="save", on_click=guardar)
            ]),
            padding=10, bgcolor="white", border_radius=10
        ),
        ft.Container(
            content=ft.Column([ft.Text("Partes registrados", weight="bold"), tabla]),
            padding=10, bgcolor="white", border_radius=10
        )
    )
    cargar_datos()

if __name__ == "__main__":
    ft.app(target=main)
