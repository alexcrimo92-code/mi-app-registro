import os
import flet as ft
from supabase import create_client

# --- CONFIGURACIÓN ---
URL = "https://bggzywzlusinkwwkwzgj.supabase.co"
KEY = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6ImJnZ3p5d3psdXNpbmt3d2t3emdqIiwicm9sZSI6ImFub24iLCJpYXQiOjE3ODI0MDMxNjMsImV4cCI6MjA5Nzk3OTE2M30.GtEiVvBZXeAYKap7YOK-CxNmUBHIoxxkJjVV4QyJp4c"
supabase = create_client(URL, KEY)

def main(page: ft.Page):
    page.title = "Registro de Partes de Trabajo"
    page.padding = 0

    # Contenedor principal para cambiar de pantalla
    contenedor_pantalla = ft.Container(expand=True)

    def mostrar_menu(e=None):
        menu_content = ft.Column(
            [
                ft.Text("Menú Principal", size=33, weight="bold", color="white"),
                ft.Container(height=20),
                ft.Row([ft.ElevatedButton("NUEVO PARTE", on_click=mostrar_formulario)], alignment=ft.MainAxisAlignment.CENTER),
                ft.Row([ft.ElevatedButton("HISTORIAL", on_click=mostrar_historial)], alignment=ft.MainAxisAlignment.CENTER),
                ft.Row([ft.ElevatedButton("CONFIGURAR")], alignment=ft.MainAxisAlignment.CENTER),
            ],
            alignment=ft.MainAxisAlignment.CENTER,
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            tight=True
        )
        
        contenedor_pantalla.content = ft.Stack([
            ft.Image(src="fondo.jpg", fit="cover", width=page.width, height=page.height),
            ft.Container(content=menu_content, alignment=ft.alignment.Alignment(0, 0), expand=True)
        ])
        page.update()

    def mostrar_formulario(e):
        # 1. Configuración del DatePicker
        fecha_input = ft.TextField(label="Fecha", read_only=True, icon=ft.icons.CALENDAR_MONTH)
        
        def on_date_change(e):
            fecha_input.value = e.control.value.strftime("%d/%m/%Y")
            page.update()

        date_picker = ft.DatePicker(on_change=on_date_change)
        page.overlay.append(date_picker)

        # Hacer que el campo abra el calendario al hacer clic
        fecha_input.on_click = lambda _: date_picker.pick_date()

        # 2. Función auxiliar para crear inputs con estilo de tarjeta
        def crear_input_estilizado(label, icon=None):
            return ft.Container(
                content=ft.TextField(label=label, border=ft.InputBorder.NONE),
                padding=10,
                bgcolor=ft.colors.WHITE70,
                border_radius=10,
                shadow=ft.BoxShadow(spread_radius=1, blur_radius=3, color=ft.colors.BLACK12)
            )

        # Construcción del formulario
        contenedor_pantalla.content = ft.Container(
            content=ft.Column([
                ft.Text("Nuevo Registro", size=24, weight="bold"),
                # Campo de fecha especial
                ft.Container(content=fecha_input, padding=10, bgcolor=ft.colors.WHITE70, border_radius=10),
                crear_input_estilizado("Nº Parte"),
                crear_input_estilizado("Horas"),
                crear_input_estilizado("Metros"),
                crear_input_estilizado("Material Instalado"),
                crear_input_estilizado("Direccion"), 
                crear_input_estilizado("Constructora"),
                crear_input_estilizado("Compañero"),
                ft.ElevatedButton("GUARDAR", icon="SAVE", on_click=mostrar_menu),
                ft.Divider(),
                ft.ElevatedButton("← MENÚ", icon="HOME", on_click=mostrar_menu)
            ], scroll=ft.ScrollMode.AUTO, spacing=15),
            padding=20
        )
        page.update()   
        def mostrar_historial(e):
        try:
            response = supabase.table("datos_app").select("*").execute()
            tarjetas = []
            for item in response.data:
                tarjetas.append(
                    ft.Card(
                        content=ft.Container(
                            content=ft.Column([
                                ft.Text(f"PARTE: {item.get('n_parte', 'N/A')}", weight="bold", color="blue"),
                                ft.Text(f"Fecha: {item.get('fecha', '')}"),
                                ft.Divider(),
                                ft.Text(f"🏢 {item.get('constructora', 'N/A')}"),
                                ft.Text(f"📍 {item.get('lugar', 'N/A')}"),
                                ft.Text(f"⏱ {item.get('horas', '0')} hrs"),
                                ft.Row([
                                    ft.Text(f"📏 {item.get('metros', '0')} m"),
                                    ft.Text("|"),
                                    ft.Text(f"🛠 {item.get('material _instalado', 'N/A')}") 
                                ])
                            ], spacing=5),
                            padding=15
                        )
                    )
                )
        except Exception as ex:
            tarjetas = [ft.Text(f"Error: {ex}")]

        # Envolvemos todo en un Container para poder usar padding
        contenedor_pantalla.content = ft.Container(
            content=ft.Column([
                ft.Text("Historial", size=24, weight="bold"),
                ft.ListView(controls=tarjetas, expand=True, spacing=10),
                ft.Divider(),
                ft.ElevatedButton("← VOLVER AL MENÚ", icon="HOME", on_click=mostrar_menu)
            ], expand=True),
            padding=20
        )
        page.update()

    # Inicialización
    page.add(contenedor_pantalla)
    mostrar_menu()

# Aseguramos el puerto para Render
if __name__ == "__main__":
    ft.app(target=main, assets_dir="assets", view=ft.AppView.WEB_BROWSER, port=int(os.environ.get("PORT", 8080)))
