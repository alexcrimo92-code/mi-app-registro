import flet as ft
from supabase import create_client, Client
import os

# --- CONFIGURACIÓN ---
URL = "https://bggzywzlusinkwwkwzgj.supabase.co"
KEY = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6ImJnZ3p5d3psdXNpbmt3d2t3emdqIiwicm9sZSI6ImFub24iLCJpYXQiOjE3ODI0MDMxNjMsImV4cCI6MjA5Nzk3OTE2M30.GtEiVvBZXeAYKap7YOK-CxNmUBHIoxxkJjVV4QyJp4c"

# Inicializar Supabase aquí, fuera de las funciones
supabase: Client = create_client(URL, KEY)

def main(page: ft.Page):
    page.title = "App Taller"
    page.padding = 20

    # Componentes de la interfaz
    lista = ft.ListView(expand=True, spacing=10)
    entrada = ft.TextField(hint_text="Escribe algo...")

    def cargar_datos(e=None):
        try:
            # Traer los datos de la nube
            response = supabase.table("datos_app").select("contenido").execute()
            
            lista.controls.clear()
            
            if not response.data:
                lista.controls.append(ft.Text("La tabla está vacía."))
            else:
                for item in response.data:
                    lista.controls.append(ft.Text(f"• {item['contenido']}"))
            
            page.update()
        except Exception as e:
            lista.controls.append(ft.Text(f"Error al cargar: {str(e)}", color="red"))
            page.update()

    def enviar(e):
        try:
            if entrada.value:
                # Guardar en la nube
                supabase.table("datos_app").insert({"contenido": entrada.value}).execute()
                entrada.value = ""
                # Actualizar la lista inmediatamente después de guardar
                cargar_datos()
        except Exception as e:
            lista.controls.append(ft.Text(f"Error al guardar: {str(e)}", color="red"))
            page.update()

    # Botón y estructura
    boton_enviar = ft.ElevatedButton("Enviar", on_click=enviar)
    
    page.add(
        ft.Text("Registro de datos", size=20, weight="bold"),
        entrada,
        boton_enviar,
        ft.Divider(),
        lista
    )

    # Cargar datos al iniciar
    cargar_datos()

# Iniciar la aplicación
ft.app(target=main, view=ft.AppView.WEB_BROWSER)