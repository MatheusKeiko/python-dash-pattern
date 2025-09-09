# [atual] layouts/main_layout.py
import dash_mantine_components as dmc
from dash_iconify import DashIconify
from dash import Input, Output, State, callback, clientside_callback
from config import Config
from layouts.map_layout import content_map

def _prefix() -> str:
    return Config.ROOT_PATH_PREFIX.rstrip("/")


def create_main_layout():
    buttons = [
        dmc.Button("Home", variant="subtle", color="gray"),
        dmc.Button("Informações", variant="subtle", color="gray"),
        dmc.Button("Sair", id="logout-button", variant="subtle", color="gray"),
        dmc.Switch(
            offLabel=DashIconify(icon="radix-icons:sun", width=15, color=dmc.DEFAULT_THEME["colors"]["yellow"][8]),
            onLabel=DashIconify(icon="radix-icons:moon", width=15, color=dmc.DEFAULT_THEME["colors"]["yellow"][6]),
            id="color-scheme-switch",
            persistence=True,
            color="grey",
            ml="md",
        ),
    ]

    return dmc.AppShell(
        [
            dmc.AppShellHeader(
                dmc.Group(
                    [
                        dmc.Group(
                            [
                                dmc.Burger(id="mobile-burger", size="sm", hiddenFrom="sm", opened=False),
                                dmc.Burger(id="desktop-burger", size="sm", visibleFrom="sm", opened=False),
                                # Light (preto) – visível no tema claro
                                dmc.Image(
                                    src=f"{_prefix()}/assets/src/images/navbar/Regua_NIT_IP_IB_Gov_uma_tinta.png",
                                    h=60,
                                    flex=0,
                                    className="theme-light-only",
                                ),
                                # Dark (branco) – visível no tema escuro
                                dmc.Image(
                                    src=f"{_prefix()}/assets/src/images/navbar/Regua_NIT_IP_IB_Gov_negativa.png",
                                    h=60,
                                    flex=0,
                                    className="theme-dark-only",
                                ),
                                dmc.Title("Projeções climáticas", size="md"),
                            ]
                        ),
                        dmc.Group(children=buttons, ml="xl", gap=0, visibleFrom="sm"),
                    ],
                    justify="space-between",
                    style={"flex": 1},
                    h="100%",
                    px="md",
                ),
            ),
            dmc.AppShellNavbar(
                id="navbar",
                children=[
                    "Colocar itens aqui",
                    *[dmc.Skeleton(height=28, mt="sm", animate=False) for _ in range(15)],
                ],
                py="md",
                px=4,
            ),
            dmc.AppShellMain(
                content_map(),
            ),
        ],
        header={"height": 60},
        navbar={"width": 300, "breakpoint": "sm", "collapsed": {"desktop": True, "mobile": True}},
        id="appshell",
        style={
            "overflow": "hidden",
            "position": "relative"
        },
    )

@callback(
    Output("appshell", "navbar"),
    Input("mobile-burger", "opened"),
    Input("desktop-burger", "opened"),
    State("appshell", "navbar"),
)
def toggle_navbar(mobile_opened, desktop_opened, navbar):
    navbar["collapsed"] = {
        "mobile": not mobile_opened,
        "desktop": not desktop_opened,
    }
    return navbar

clientside_callback(
    """
    (switchOn) => {
       document.documentElement.setAttribute('data-mantine-color-scheme', switchOn ? 'dark' : 'light');
       return window.dash_clientside.no_update
    }
    """,
    Output("color-scheme-switch", "id"),
    Input("color-scheme-switch", "checked"),
)



