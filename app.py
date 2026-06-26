import os
import flet as ft
from supabase import create_client

# --- CONFIGURACIÓN ---
URL = "https://bggzywzlusinkwwkwzgj.supabase.co"
KEY = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6ImJnZ3p5d3psdXNpbmt3d2t3emdqIiwicm9sZSI6ImFub24iLCJpYXQiOjE3ODI0MDMxNjMsImV4cCI6MjA5Nzk3OTE2M30.GtEiVvBZXeAYKap7YOK-CxNmUBHIoxxkJjVV4QyJp4c"
supabase = create_client(URL, KEY)



def main(page: ft.Page):
    page.assets_dir = "assets"
    page.title = "App Registro"
    page.theme_mode = "light"
    page.padding = 0

    # Usamos un Stack como contenedor principal
    contenedor_pantalla = ft.Stack(expand=True)
    page.add(contenedor_pantalla)

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
        contenedor_pantalla.controls.clear()
        h, m = obtener_totales()
        
        # 1. Capa de imagen (fondo)
        fondo = ft.Image(src="fondo.jpg", fit="cover", width=page.width, height=page.height)
        
        # 2. Capa de contenido (menú)
        contenido = ft.Column([
            ft.Container(content=ft.Column([
                ft.Text("MENÚ PRINCIPAL", size=24, weight="bold"),
                ft.Text(f"Total Horas ⏱: {h}"),
                ft.Text(f"Total Metros 📏: {m}"),
            ]), bgcolor="white", padding=20, border_radius=10),
            ft.ElevatedButton("NUEVO REGISTRO", on_click=mostrar_formulario),
            ft.ElevatedButton("VER HISTORIAL", on_click=mostrar_historial)
        ], alignment="center", horizontal_alignment="center")

        contenedor_pantalla.controls.extend([fondo, contenido])
        page.update()

    # --- CAMPOS (Igual que antes) ---
    f_fecha = ft.TextField(label="Fecha", value="26/06/2026")
    f_horas = ft.TextField(label="Horas")
    f_metros = ft.TextField(label="Metros")
    f_material = ft.TextField(label="Material instalado")
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
        contenedor_pantalla.controls.clear()
        formulario = ft.Column([
            ft.Text("Nuevo Registro"), f_fecha, f_horas, f_metros, f_material, 
            f_lugar, f_parte, f_constr, f_comp, 
            ft.ElevatedButton("GUARDAR", on_click=guardar_registro), 
            ft.ElevatedButton("VOLVER", on_click=mostrar_menu)
        ], scroll="auto")
        contenedor_pantalla.controls.append(formulario)
        page.update()

    def mostrar_historial(e):
        contenedor_pantalla.controls.clear()
        lista = ft.Column(scroll="auto")
        lista.controls.append(ft.ElevatedButton("VOLVER", on_click=mostrar_menu))
        
        try:
            res = supabase.table("datos_app").select("*").execute()
            for item in res.data:
                tarjeta = ft.Container(
                    content=ft.Column([
                        ft.Text(f"📅 {item.get('fecha')} | Parte: {item.get('n_parte', 'N/A')}", weight="bold"),
                        ft.Text(f"🏢 {item.get('constructora')} | 📍 {item.get('lugar')}"),
                        ft.Text(f"⏱ {item.get('horas')}h | 📏 {item.get('metros')}m | 🛠 {item.get('material instalado', 'N/A')}"),
                        ft.Text(f"👥 {item.get('companero')}")
                    ]),
                    border=ft.border.all(1, "grey"),
                    padding=10
                )
                lista.controls.append(tarjeta)
        except:
            lista.controls.append(ft.Text("Error al cargar"))
            
        contenedor_pantalla.controls.append(lista)
        page.update()

    mostrar_menu()

if __name__ == "__main__":
    ft.app(target=main, port=int(os.environ.get("PORT", 8080)))