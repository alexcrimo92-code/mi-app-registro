import os
import flet as ft
from supabase import create_client

# --- CONFIGURACIÓN ---
URL = "https://bggzywzlusinkwwkwzgj.supabase.co"
KEY = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6ImJnZ3p5d3psdXNpbmt3d2t3emdqIiwicm9sZSI6ImFub24iLCJpYXQiOjE3ODI0MDMxNjMsImV4cCI6MjA5Nzk3OTE2M30.GtEiVvBZXeAYKap7YOK-CxNmUBHIoxxkJjVV4QyJp4c"
supabase = create_client(URL, KEY)



def main(page: ft.Page):
    page.title = "App Registro"
    page.theme_mode = "light"
    page.padding = 0
    page.assets_dir = "assets"
    
    # 1. Creamos un Stack para superponer la imagen y el contenido
    contenedor_principal = ft.Stack(expand=True)
    page.add(contenedor_principal)
    
    # 2. Capa de fondo: Imagen
    fondo = ft.Image(src="fondo.jpeg", fit="cover", width=page.width, height=page.height)
    
    # 3. Capa de contenido: Columna centrada
    contenido = ft.Column(alignment="center", horizontal_alignment="center")
    
    contenedor_principal.controls.append(fondo)
    contenedor_principal.controls.append(contenido)

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
        contenido.controls.clear()
        h, m = obtener_totales()
        contenido.controls.extend([
            ft.Text("MENÚ PRINCIPAL", size=24, weight="bold", color="white"),
            ft.Text(f"Total Horas ⏱: {h}", color="white"),
            ft.Text(f"Total Metros 📏: {m}", color="white"),
            ft.ElevatedButton("➕ NUEVO REGISTRO", on_click=mostrar_formulario),
            ft.ElevatedButton("📋 VER HISTORIAL", on_click=mostrar_historial)
        ])
        page.update()

    def mostrar_historial(e):
        contenido.controls.clear()
        contenido.controls.append(ft.ElevatedButton("🔙 VOLVER", on_click=mostrar_menu))
        try:
            res = supabase.table("datos_app").select("*").execute()
            for item in res.data:
                tarjeta = ft.Column([
                    ft.Text(f"📅 {item.get('fecha', 'N/A')} | 🆔 {item.get('n_parte', 'N/A')}", weight="bold", color="white"),
                    ft.Text(f"🏢 {item.get('constructora', 'N/A')} | 🛠 {item.get('material instalado', 'N/A')}", color="white"),
                    ft.Text("------------------------------------", color="white")
                ], horizontal_alignment="center")
                contenido.controls.append(tarjeta)
        except:
            contenido.controls.append(ft.Text("Error al cargar", color="white"))
        page.update()

    def mostrar_formulario(e):
        # ... (Mantén tu código anterior de formulario aquí)
        pass

    mostrar_menu()

if __name__ == "__main__":
    ft.app(target=main, port=int(os.environ.get("PORT", 8080)))