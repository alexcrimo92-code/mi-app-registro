import flet as ft
from supabase import create_client

# --- CONFIGURACIÓN ---
URL = "https://bggzywzlusinkwwkwzgj.supabase.co"
KEY = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6ImJnZ3p5d3psdXNpbmt3d2t3emdqIiwicm9sZSI6ImFub24iLCJpYXQiOjE3ODI0MDMxNjMsImV4cCI6MjA5Nzk3OTE2M30.GtEiVvBZXeAYKap7YOK-CxNmUBHIoxxkJjVV4QyJp4c"
supabase = create_client(URL, KEY)



def main(page: ft.Page):
    page.title = "PARTES DE TRABAJO"
    page.theme_mode = ft.ThemeMode.LIGHT
    page.bgcolor = "#E3F2FD" 
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER

    # Usamos iconos como string (ej: "save") en lugar de ft.icons.SAVE
    f_fecha = ft.TextField(label="Fecha", value="26/06/2026", icon="date_range", width=300)
    
    # Menú desplegable para horas
    f_horas = ft.Dropdown(
        label="Horas trabajadas",
        options=[ft.dropdown.Option(str(i)) for i in range(1, 13)],
        width=300
    )

    f_metros = ft.TextField(label="Metros instalados", icon="reorder", width=300)
    f_lugar = ft.TextField(label="Lugar", icon="location_on", width=300)
    f_n_parte = ft.TextField(label="Nº Parte", icon="tag", width=300)
    f_constructora = ft.TextField(label="Constructora", icon="business", width=300)
    f_companero = ft.TextField(label="Compañero", icon="person", width=300)

    tabla = ft.DataTable(
        columns=[
            ft.DataColumn(ft.Text("Parte")),
            ft.DataColumn(ft.Text("Lugar")),
            ft.DataColumn(ft.Text("Horas")),
        ],
        rows=[]
    )

    def cargar_datos(e=None):
        try:
            response = supabase.table("datos_app").select("*").execute()
            tabla.rows.clear()
            for i in response.data:
                tabla.rows.append(ft.DataRow(cells=[
                    ft.DataCell(ft.Text(str(i.get("n_parte", "")))),
                    ft.DataCell(ft.Text(i.get("lugar", ""))),
                    ft.DataCell(ft.Text(str(i.get("horas", "")))),
                ]))
            page.update()
        except:
            pass

    def guardar(e):
        try:
            supabase.table("datos_app").insert({
                "fecha": f_fecha.value, "horas": f_horas.value, "metros": f_metros.value,
                "lugar": f_lugar.value, "n_parte": f_n_parte.value, 
                "constructora": f_constructora.value, "companero": f_companero.value
            }).execute()
            cargar_datos()
        except:
            pass

    # Diseño usando contenedores simples
    page.add(
        ft.Container(
            content=ft.Column([
                ft.Text("PARTES DE TRABAJO", size=30, weight="bold", color="#0D47A1"),
                f_fecha, f_horas, f_metros, f_lugar, f_n_parte, f_constructora, f_companero,
                ft.ElevatedButton("GUARDAR PARTE", icon="save", on_click=guardar, bgcolor="#1976D2", color="white")
            ], horizontal_alignment=ft.CrossAxisAlignment.CENTER),
            bgcolor="white", padding=30, border_radius=20, width=400
        ),
        ft.Container(
            content=ft.Column([
                ft.Text("Partes registrados", size=20, weight="bold"),
                # ScrollView simple que sí existe en todas las versiones
                ft.ListView(content=tabla, height=200) 
            ]),
            bgcolor="white", padding=20, border_radius=20, margin=ft.margin.only(top=20)
        )
    )
    cargar_datos()

if __name__ == "__main__":
    ft.app(target=main)
