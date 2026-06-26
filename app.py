import os
import flet as ft
from supabase import create_client

# --- CONFIGURACIÓN ---
URL = "https://bggzywzlusinkwwkwzgj.supabase.co"
KEY = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6ImJnZ3p5d3psdXNpbmt3d2t3emdqIiwicm9sZSI6ImFub24iLCJpYXQiOjE3ODI0MDMxNjMsImV4cCI6MjA5Nzk3OTE2M30.GtEiVvBZXeAYKap7YOK-CxNmUBHIoxxkJjVV4QyJp4c"
supabase = create_client(URL, KEY)


def main(page: ft.Page):
    page.title = "Registro de Trabajo"
    page.theme_mode = ft.ThemeMode.LIGHT
    page.bgcolor = "#F8F9FA"

    # Campos
    f_fecha = ft.TextField(label="Fecha", value="26/06/2026")
    f_horas = ft.TextField(label="Horas")
    f_metros = ft.TextField(label="Metros")
    f_lugar = ft.TextField(label="Lugar")
    f_n_parte = ft.TextField(label="Nº Parte")
    f_constructora = ft.TextField(label="Constructora")
    f_companero = ft.TextField(label="Compañero")

    contenedor_principal = ft.Container()

    def mostrar_inicio(e=None):
        contenedor_principal.content = ft.Container(
            content=ft.Column([
                ft.Text("Menú Principal", size=24, weight="bold"),
                ft.ElevatedButton("NUEVO REGISTRO", icon="add", on_click=mostrar_formulario),
                ft.ElevatedButton("VER HISTORIAL", icon="list", on_click=mostrar_historial)
            ], alignment=ft.MainAxisAlignment.CENTER, horizontal_alignment=ft.CrossAxisAlignment.CENTER),
            padding=50
        )
        page.update()

    def mostrar_formulario(e):
        contenedor_principal.content = ft.Container(
            content=ft.Column([
                ft.AppBar(title=ft.Text("Nuevo Parte"), bgcolor="blue", color="white", 
                          leading=ft.IconButton("arrow_back", on_click=mostrar_inicio)),
                f_fecha, f_horas, f_metros, f_lugar, f_n_parte, f_constructora, f_companero,
                ft.ElevatedButton("GUARDAR PARTE", icon="save", on_click=guardar_y_volver),
                ft.OutlinedButton("CANCELAR", icon="close", on_click=mostrar_inicio)
            ], scroll=ft.ScrollMode.AUTO),
            padding=20
        )
        page.update()

    def guardar_y_volver(e):
        datos = {
            "fecha": f_fecha.value, "horas": f_horas.value, "metros": f_metros.value,
            "lugar": f_lugar.value, "n_parte": f_n_parte.value, 
            "constructora": f_constructora.value, "companero": f_companero.value
        }
        supabase.table("datos_app").insert(datos).execute()
        mostrar_inicio()

    def mostrar_historial(e):
      def mostrar_historial(e):
        response = supabase.table("datos_app").select("*").execute()
        tarjetas = []
        for item in response.data:
            tarjetas.append(
                ft.Card(
                    # El Card se ajustará automáticamente al ancho del padre
                    content=ft.Container(
                        content=ft.Column([
                            ft.ListTile(
                                leading=ft.Icon("work"),
                                title=ft.Text(f"Nº Parte: {item.get('n_parte', 'N/A')}"),
                                subtitle=ft.Text(f"Fecha: {item.get('fecha', '')}"),
                            ),
                            ft.Container(
                                content=ft.Column([
                                    ft.Text(f"Constructora: {item.get('constructora', '')}"),
                                    ft.Text(f"Lugar: {item.get('lugar', '')}"),
                                    ft.Text(f"Horas: {item.get('horas', '')} | Metros: {item.get('metros', '')}"),
                                    ft.Text(f"Compañero: {item.get('companero', '')}"),
                                ], spacing=5),
                                padding=10
                            )
                        ]),
                        padding=10
                    )
                )
            )

        contenedor_principal.content = ft.Container(
            # Configuramos el contenedor para que ocupe todo el ancho
            content=ft.Column([
                ft.AppBar(title=ft.Text("Historial"), bgcolor="blue", color="white", 
                          leading=ft.IconButton("arrow_back", on_click=mostrar_inicio)),
                ft.Container(
                    content=ft.ElevatedButton("VOLVER AL MENÚ", icon="home", on_click=mostrar_inicio),
                    padding=ft.padding.only(left=20, right=20)
                ),
                ft.Divider(),
                # Expanded hace que la lista ocupe el resto de la pantalla y no se comprima
                ft.Container(
                    content=ft.ListView(controls=tarjetas, spacing=10),
                    padding=20,
                    expand=True 
                )
            ], expand=True), # El Column también debe expandirse
            expand=True
        )
        page.update()

    page.add(contenedor_principal)
    mostrar_inicio()

ft.app(target=main, view=ft.AppView.WEB_BROWSER, port=int(os.environ.get("PORT", 8080)))