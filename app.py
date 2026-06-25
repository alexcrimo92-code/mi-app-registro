import flet as ft
import os
from supabase import create_client, Client

# --- CONFIGURACIÓN ---
# Reemplaza estas líneas con tus datos reales de Supabase
URL = "https://bggzywzlusinkwwkwzgj.supabase.co"
KEY = "sb_publishable_OltrpYbszHHSWy6gyzRR2A_2sGx6Sxx"
supabase: Client = create_client(URL, KEY)

def main(page: ft.Page):
    page.title = "App de Registro en la Nube"
    
    # Campo de texto y lista
    entrada = ft.TextField(label="¿Qué quieres registrar?", width=300)
    lista = ft.Column()

    def cargar_datos():
    try:
            # Intentamos traer los datos
            response = supabase.table("datos_app").select("contenido").execute()
            
            lista.controls.clear()
            
            # Verificamos si response.data tiene contenido
            if not response.data:
                lista.controls.append(ft.Text("La tabla está vacía."))
            else:
                for item in response.data:
                    lista.controls.append(ft.Text(f"• {item['contenido']}"))
            
            page.update()
            
        except Exception as e:
            # Esto mostrará el error en tu app móvil/PC si algo falla
            lista.controls.append(ft.Text(f"Error técnico: {str(e)}", color="red"))
            page.update()


def enviar(e):
        if entrada.value:
            try:
                # Intentamos guardar
                supabase.table("datos_app").insert({"contenido": entrada.value}).execute()
                entrada.value = ""
                cargar_datos()
                page.update()
            except Exception as e:
                # Si falla, mostraremos el error en la pantalla
                lista.controls.append(ft.Text(f"Error: {e}", color="red"))
                page.update()

    # Cargar datos al iniciar
    cargar_datos()

    page.add(
        ft.Row([entrada, ft.ElevatedButton("Guardar", on_click=enviar)], alignment=ft.MainAxisAlignment.CENTER),
        lista
    )

# Configuración para que funcione en Render
port = int(os.environ.get("PORT", 8000))
ft.app(target=main, port=port, view=ft.AppView.WEB_BROWSER)