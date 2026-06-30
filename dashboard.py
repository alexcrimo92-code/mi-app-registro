import flet as ft

from config import PRIMARY


class DashboardView(ft.Container):

    def __init__(self, page: ft.Page):
        super().__init__()

        self.page = page

        self.expand = True
        self.padding = 10

        self.content = self.build_ui()

    # -------------------------------------------------

    def build_card(self, title: str, value: str, icon: str):

        return ft.Container(
            width=260,
            height=140,
            padding=20,
            border_radius=15,
            bgcolor="white",
            shadow=ft.BoxShadow(
                spread_radius=1,
                blur_radius=12,
                color=ft.Colors.BLACK12,
                offset=ft.Offset(0, 4),
            ),
            content=ft.Column(
                [
                    ft.Row(
                        [
                            ft.Icon(icon, color=PRIMARY, size=28),
                            ft.Text(title, size=16, weight="bold"),
                        ],
                        alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
                    ),
                    ft.Divider(height=10, color="transparent"),
                    ft.Text(
                        value,
                        size=28,
                        weight="bold",
                        color=PRIMARY,
                    ),
                ]
            ),
        )

    # -------------------------------------------------

    def build_ui(self):

        return ft.Column(
            expand=True,
            spacing=20,
            controls=[

                ft.Text(
                    "Dashboard",
                    size=30,
                    weight="bold",
                ),

                ft.Text(
                    "Resumen general de actividad",
                    size=14,
                    color="grey",
                ),

                ft.Row(
                    wrap=True,
                    spacing=20,
                    controls=[

                        self.build_card("Horas del mes", "0 h", ft.Icons.TIMER),

                        self.build_card("Metros", "0 m", ft.Icons.STRAIGHTEN),

                        self.build_card("Partes", "0", ft.Icons.FORMAT_LIST_NUMBERED),

                        self.build_card("Constructoras", "0", ft.Icons.BUILD),

                    ],
                ),

                ft.Container(height=20),

                ft.Container(
                    padding=20,
                    border_radius=15,
                    bgcolor="white",
                    content=ft.Column(
                        [
                            ft.Text(
                                "Últimos partes",
                                size=18,
                                weight="bold",
                            ),
                            ft.Divider(),
                            ft.Text(
                                "Aún no hay datos",
                                color="grey",
                            ),
                        ]
                    ),
                ),

            ],
        )
