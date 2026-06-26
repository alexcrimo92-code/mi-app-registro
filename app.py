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
    # Centrado global básico
    page.horizontal_alignment = "center" 
    
    contenedor_pantalla = ft.Column(alignment="center", horizontal_alignment="center")
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
        
        # Menú centrado
        contenedor_pantalla.controls.extend([
            ft.Text("MENÚ PRINCIPAL", size=24, weight="bold"),
            ft.Text(f"Total Horas ⏱: {h}"),
            ft.Text(f"Total Metros 📏: {m}"),
            ft.ElevatedButton("➕ NUEVO REGISTRO", on_click=mostrar_formulario),
            ft.ElevatedButton("📋 VER HISTORIAL", on_click=mostrar_historial)
        ])
        page.update()

    def mostrar_historial(e):
        contenedor_pantalla.controls.clear()
        contenedor_pantalla.controls.append(ft.ElevatedButton("🔙 VOLVER", on_click=mostrar_menu))
        
        try:
            res = supabase.table("datos_app").select("*").execute()
            for item in res.data:
                # ESTRUCTURA DE TARJETA: Título = Fecha + Parte
                tarjeta = ft.Container(
                    content=ft.Column([
                        ft.Text(f"📅 {item.get('fecha', 'N/A')} - Parte Nº: {item.get('n_parte', 'N/A')}", 
                                weight="bold", size=16),
                        ft.Divider(),
                        ft.Text(f"🏢 Constructora: {item.get('constructora', 'N/A')}"),
                        ft.Text(f"📍 Lugar: {item.get('lugar', 'N/A')}"),
                        ft.Text(f"🛠 Material: {item.get('material instalado', 'N/A')}"),
                        ft.Text(f"⏱ {item.get('horas')}h | 📏 {item.get('metros')}m | 👥 {item.get('companero')}")
                    ]),
                    padding=15,
                    border=ft.border.all(1, "grey"),
                    border_radius=10,
                    margin=10
                )
                contenedor_pantalla.controls.append(tarjeta)
        except Exception as err:
            contenedor_pantalla.controls.append(ft.Text(f"Error: {err}"))
        page.update()

    # (Funciones de formulario permanecen iguales)
    # ... (mostrar_formulario y guardar_registro)

    mostrar_menu()

if __name__ == "__main__":
    ft.app(target=main, port=int(os.environ.get("PORT", 8080)))