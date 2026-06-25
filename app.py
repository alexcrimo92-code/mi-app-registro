import flet as ft
# Asegúrate de tener los imports de supabase aquí

def main(page: ft.Page):
    page.title = "App Taller"
    
    # Mensaje inicial para saber si la app arranca
    lista = ft.ListView()
    entrada = ft.TextField(hint_text="Escribe algo...")
    
    page.add(ft.Text("Iniciando aplicación..."), entrada, ft.ElevatedButton("Enviar", on_click=lambda e: enviar(e)), lista)

    def cargar_datos():
        try:
            # Quitamos el mensaje de iniciando
            lista.controls.clear()
            response = supabase.table("datos_app").select("contenido").execute()
            
            if not response.data:
                lista.controls.append(ft.Text("La tabla está vacía en Supabase"))
            else:
                for item in response.data:
                    lista.controls.append(ft.Text(f"• {item['contenido']}"))
            page.update()
        except Exception as e:
            lista.controls.append(ft.Text(f"ERROR CRÍTICO: {str(e)}", color="red"))
            page.update()

    def enviar(e):
        try:
            supabase.table("datos_app").insert({"contenido": entrada.value}).execute()
            entrada.value = ""
            cargar_datos()
        except Exception as e:
            lista.controls.append(ft.Text(f"ERROR AL GUARDAR: {str(e)}", color="red"))
            page.update()

    cargar_datos()

ft.app(target=main, view=ft.AppView.WEB_BROWSER)