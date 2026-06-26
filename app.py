import os
import flet as ft
from supabase import create_client

# --- CONFIGURACIÓN ---
URL = "https://bggzywzlusinkwwkwzgj.supabase.co"
KEY = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6ImJnZ3p5d3psdXNpbmt3d2t3emdqIiwicm9sZSI6ImFub24iLCJpYXQiOjE3ODI0MDMxNjMsImV4cCI6MjA5Nzk3OTE2M30.GtEiVvBZXeAYKap7YOK-CxNmUBHIoxxkJjVV4QyJp4c"
supabase = create_client(URL, KEY)

import flet as ft
import os
from supabase import create_client

# Configuración
URL = os.environ.get("URL")
KEY = os.environ.get("KEY")
supabase = create_client(URL, KEY)

def main(page: ft.Page):
    page.title = "App Registro"
    page.theme_mode = "light"
    # Alineación centrada para que el menú luzca profesional
    page.vertical_alignment = "center"
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
        
        contenedor_pantalla.controls.extend([
            ft.Text("MENÚ PRINCIPAL", size=24, weight="bold"),
            ft.Text(f"⏱ Total Horas: {h}"),
            ft.Text(f"📏 Total Metros: {m}"),
            ft.ElevatedButton("➕ NUEVO REGISTRO", on_click=mostrar_formulario),
            ft.ElevatedButton("📋 VER HISTORIAL", on_click=mostrar_historial)
        ])
        page.update()

    # Campos definidos globalmente para evitar errores
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
        contenedor_pantalla.controls.extend([
            ft.Text("Nuevo Registro", size=20),
            f_fecha, f_horas, f_metros, f_material, f_lugar, f_parte, f_constr, f_comp,
            ft.ElevatedButton("💾 GUARDAR", on_click=guardar_registro),
            ft.ElevatedButton("🔙 VOLVER", on_click=mostrar_menu)
        ])
        page.update()

    def mostrar_historial(e):
        contenedor_pantalla.controls.clear()
        # Botón volver al inicio
        contenedor_pantalla.controls.append(ft.ElevatedButton("🔙 VOLVER", on_click=mostrar_menu))
        
        try:
            res = supabase.table("datos_app").select("*").execute()
            for item in res.data:
                # TARJETA PROFESIONAL: Usando el estilo celeste que solicitaste
                tarjeta = ft.Container(
                    content=ft.Column([
                        ft.Text(f"📅 {item.get('fecha', 'N/A')} | 🆔 {item.get('n_parte', 'N/A')}", weight="bold"),
                        ft.Text(f"🏢 {item.get('constructora', 'N/A')} | 📍 {item.get('lugar', 'N/A')}"),
                        ft.Text(f"🛠 {item.get('material instalado', 'N/A')}"),
                        ft.Text(f"⏱ {item.get('horas')}h | 📏 {item.get('metros')}m | 👥 {item.get('companero', 'N/A')}")
                    ]),
                    padding=15,
                    border=ft.border.all(1, "grey"),
                    border_radius=15,
                    bgcolor="#e3f2fd", # Color celeste profesional
                    margin=10
                )
                contenedor_pantalla.controls.append(tarjeta)
        except Exception as err:
            contenedor_pantalla.controls.append(ft.Text(f"Error: {err}"))
        page.update()

    mostrar_menu()

if __name__ == "__main__":
    ft.app(target=main, port=int(os.environ.get("PORT", 8080)))
    




