import os
import flet as ft

from config import (
    PRIMARY,
    BACKGROUND,
    TRABAJADOR
)

# Vistas (las iremos creando)
from dashboard import DashboardView
from views.formulario import FormularioView
from views.historial import HistorialView
from views.estadisticas import EstadisticasView
from views.configuracion import ConfiguracionView


class App:

    def __init__(self, page: ft.Page):

        self.page = page

        self.page.title = "Partes de Trabajo PRO"

        self.page.window_width = 1400
        self.page.window_height = 850
        self.page.padding = 0
        self.page.spacing = 0

        self.page.theme_mode = ft.ThemeMode.LIGHT

        self.page.theme = ft.Theme(
            color_scheme_seed=PRIMARY,
            use_material3=True,
        )

        self.navigation = ft.NavigationRail(
            selected_index=0,
            label_type=ft.NavigationRailLabelType.ALL,
            min_width=80,
            min_extended_width=220,
            extended=True,
            group_alignment=-0.9,
            destinations=[
                ft.NavigationRailDestination(
                    icon=ft.Icons.HOME_OUTLINED,
                    selected_icon=ft.Icons.HOME,
                    label="Inicio",
                ),
                ft.NavigationRailDestination(
                    icon=ft.Icons.ADD_BOX_OUTLINED,
                    selected_icon=ft.Icons.ADD_BOX,
                    label="Nuevo Parte",
                ),
                ft.NavigationRailDestination(
                    icon=ft.Icons.HISTORY,
                    selected_icon=ft.Icons.HISTORY,
                    label="Historial",
                ),
                ft.NavigationRailDestination(
                    icon=ft.Icons.QUERY_STATS,
                    selected_icon=ft.Icons.QUERY_STATS,
                    label="Estadísticas",
                ),
                ft.NavigationRailDestination(
                    icon=ft.Icons.SETTINGS_OUTLINED,
                    selected_icon=ft.Icons.SETTINGS,
                    label="Configuración",
                ),
            ],
            on_change=self.cambiar_pantalla,
        )

        self.contenido = ft.Container(
            expand=True,
            bgcolor=BACKGROUND,
            padding=20,
        )

        self.page.add(
            ft.Row(
                [
                    self.navigation,
                    ft.VerticalDivider(width=1),
                    self.contenido,
                ],
                expand=True,
            )
        )

        self.cargar_dashboard()

    # -------------------------------------------------

    def cargar_dashboard(self):

        self.contenido.content = DashboardView(self.page)

        self.page.update()

    # -------------------------------------------------

    def cargar_formulario(self):

        self.contenido.content = FormularioView(self.page)

        self.page.update()

    # -------------------------------------------------

    def cargar_historial(self):

        self.contenido.content = HistorialView(self.page)

        self.page.update()

    # -------------------------------------------------

    def cargar_estadisticas(self):

        self.contenido.content = EstadisticasView(self.page)

        self.page.update()

    # -------------------------------------------------

    def cargar_configuracion(self):

        self.contenido.content = ConfiguracionView(self.page)

        self.page.update()

    # -------------------------------------------------

    def cambiar_pantalla(self, e):

        indice = e.control.selected_index

        if indice == 0:
            self.cargar_dashboard()

        elif indice == 1:
            self.cargar_formulario()

        elif indice == 2:
            self.cargar_historial()

        elif indice == 3:
            self.cargar_estadisticas()

        elif indice == 4:
            self.cargar_configuracion()


# =====================================================


def main(page: ft.Page):

    App(page)


if __name__ == "__main__":

    ft.app(
        target=main,
        assets_dir="assets",
        view=ft.AppView.WEB_BROWSER,
        port=int(os.environ.get("PORT", 8080)),
    )
