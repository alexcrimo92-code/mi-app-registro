import os
import flet as ft
from supabase import create_client

# --- CONFIGURACIÓN ---
URL = "https://bggzywzlusinkwwkwzgj.supabase.co"
KEY = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6ImJnZ3p5d3psdXNpbmt3d2t3emdqIiwicm9sZSI6ImFub24iLCJpYXQiOjE3ODI0MDMxNjMsImV4cCI6MjA5Nzk3OTE2M30.GtEiVvBZXeAYKap7YOK-CxNmUBHIoxxkJjVV4QyJp4c"
supabase = create_client(URL, KEY)



def main(page: ft.Page):
    # Definimos la carpeta de archivos estáticos
    page.assets_dir = "assets"
    page.title = "App Registro"
    page.theme_mode = "light"
    page.padding = 0

    contenedor_pantalla = ft.Container(expand=True)

    def obtener_totales():
        try:
            response = supabase.table("datos_app").select("horas, metros").execute()
            data = response.data
            t_h = sum(float(i.get('horas', 0) or 0) for i in data)
            t_m = sum(float(i.get('metros', 0) or 0) for i in data)
            return t_h, t_m
        except:
            return 0, 0

    def mostrar_menu(e=None):
        h, m = obtener_totales()
        
        # Menú principal con fondo y cálculos
        contenedor_pantalla.content = ft.Container(
            image_src="fondo.jpg",
            image_fit="cover",
            padding=20,
            content=ft.Column([
                ft.Text("CONTROL DE OBRA", size=26, weight="bold", color="white"),
                ft.Container(
                    bgcolor="white", padding=20, border_radius=15,
                    content=ft.Row([
                        ft.Column([ft.Text("Total Horas ⏱"), ft.Text(str(h), size=20, weight="bold")]),
                        ft.VerticalDivider(),
                        ft.Column([ft.Text("Total Metros 📏"), ft.Text(str(m), size=20, weight="bold")])
                    ], alignment="center")
                ),
                ft.ElevatedButton("NUEVO REGISTRO", icon="add", on_click=mostrar_formulario),
                ft.ElevatedButton("VER HISTORIAL", icon="list", on_click=mostrar_historial)
            ], alignment="center", horizontal_alignment="center")
        )
        page.update()

    # --- FORMULARIO ---
    f_fecha = ft.TextField(label="Fecha", value="26/06/2026")
    f_horas = ft.TextField(label="Horas")
    f_metros = ft.TextField(label="Metros")
    f_material = ft.TextField(label="Material Instalado")
    f_lugar = ft.TextField(label="Lugar")
    f_parte = ft.TextField(label="Nº Parte")
    f_constr = ft.TextField(label="Constructora")
    f_comp = ft.TextField(label="Compañero")

    def guardar_registro(e):
        datos = {
            "fecha": f_fecha.value, "horas": f_horas.value, "metros": f_metros.value, 
            "material instalado": f_material.value, "lugar": f_lugar.value, 
            "n_parte": f_parte.value, "constructora": f_constr.value, "companero": f_comp.value
        }
        supabase.table("datos_app").insert(datos).execute()
        mostrar_menu()

    def mostrar_formulario(e):
        contenedor_pantalla.content = ft.Column([
            ft.Text("Nuevo Registro", size=20, weight="bold"),
            f_fecha, f_horas, f_metros, f_material, f_lugar, f_parte, f_constr, f_comp,
            ft.ElevatedButton("GUARDAR", icon="save", on_click=guardar_registro),
            ft.ElevatedButton("← VOLVER", icon="arrow_back", on_click=mostrar_menu)
        ], scroll="auto", padding=20)
        page.update()

    def mostrar_historial(e):
        try:
            response = supabase.table("datos_app").select("*").execute()
            tarjetas = []
            for item in response.data:
                tarjeta = ft.Card(content=ft.Container(padding=15, content=ft.Column([
                    ft.Row([
                        ft.Text(f"📅 {item.get('fecha', 'N/A')}"),
                        ft.Text(f"Parte: {item.get('n_parte', 'N/A')}", weight="bold")
                    ], alignment="spaceBetween"),
                    ft.Divider(),
                    ft.Text(f"🏢 {item.get('constructora', 'N/A')}"),
                    ft.Text(f"📍 {item.get('lugar', 'N/A')}"),
                    ft.Row([
                        ft.Text(f"⏱ {item.get('horas', '0')} h"),
                        ft.Text(f"📏 {item.get('metros', '0')} m"),
                        ft.Text(f"🛠 {item.get('material instalado', 'N/A')}")
                    ]),
                    ft.Text(f"👥 {item.get('companero', 'N/A')}")
                ])))
                tarjetas.append(tarjeta)
        except:
            tarjetas = [ft.Text("Error al cargar")]

        contenedor_pantalla.content = ft.Column([
            ft.Text("Historial", size=20, weight="bold"),
            ft.ListView(controls=tarjetas, expand=True, spacing=10),
            ft.ElevatedButton("← VOLVER", icon="arrow_back", on_click=mostrar_menu)
        ], expand=True, padding=20)
        page.update()

    page.add(contenedor_pantalla)
    mostrar_menu()

if __name__ == "__main__":
    ft.app(target=main, port=int(os.environ.get("PORT", 8080)))