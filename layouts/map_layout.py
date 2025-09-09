# [atual] layouts/map_layout.py
import dash_leaflet as dl
from dash import html
from components.map.map_alerts.ui import successful_access_alert
from components.map.map_layers.ui import layers_camadas_component
from components.map.map_buttons.ui import map_buttons_teste
from components.map.map_dropdown.ui import map_dropdown_teste
import dash_mantine_components as dmc

def tabs_ui():
 return dmc.Tabs(
    activateTabWithKeyboard=False,
    radius="xs",
    # variant="variant",
    color="teal",
    children=[
        dmc.TabsList(
            [
                dmc.TabsTab("Foz do Iguaçu", value="gallery", color="teal"),
                dmc.TabsTab("Usina Hidrelétrica de Itaipu", value="messages", disabled=False),
                dmc.TabsTab("Sequenciamento", value="settings"),
            ]
        ),
        content_map(),
    ],    
)
def content_map():
    """Layout do mapa ocupando todo o espaço do AppShellMain."""
    return html.Div(
        id="map-stage",
        style={"position": "relative"},  # ANCORAGEM DO ABSOLUTE
        children=[
            dl.Map(
                style={"height": "calc(100vh - 60px)"},
                zoomControl=False,
                center=[-21, -55],
                zoom=6,
                attributionControl=False,
                children=[
                    dl.AttributionControl(position="topright"),
                    successful_access_alert(),
                    layers_camadas_component(),
                    map_buttons_teste(),
                    map_dropdown_teste(),
                ],
            ),
        ],
    )

def tabs_ui_test():
    return dmc.Tabs(
        id="main-tabs",
        value="gallery",          # aba inicial (a do mapa)
        keepMounted=False,        # monta/desmonta conteúdo por aba (bom pro Leaflet)
        activateTabWithKeyboard=False,
        variant="outline",
        radius="sm",
        # color="teal",
        children=[
            dmc.TabsList([
                dmc.TabsTab("Foz do Iguaçu", value="gallery"),
                dmc.TabsTab("Usina Hidrelétrica de Itaipu", value="messages"),
                dmc.TabsTab("Sequenciamento", value="settings"),
            ]),
            # --- CONTEÚDO DAS ABAS ---
            dmc.TabsPanel(content_map(), value="gallery"),
            dmc.TabsPanel(html.Div("Conteúdo da usina (em breve)."), value="messages"),
            dmc.TabsPanel(html.Div("Sequenciamento (em breve)."), value="settings"),
        ],
    )

def content_map_test():
    """Layout do mapa ocupando o painel da aba."""
    return html.Div(
        id="map-stage",
        # Dê altura explícita ao contêiner do mapa dentro do painel da aba:
        style={
            "position": "relative",
            # ajuste este cálculo conforme o topo/headers do seu layout
            "height": "calc(100vh - 160px)",
            "width": "100%",
        },
        children=[
            dl.Map(
                id="main-map",
                style={"height": "100%", "width": "100%"},
                zoomControl=False,
                center=[-21, -55],
                zoom=6,
                attributionControl=False,
                children=[
                    dl.AttributionControl(position="topright"),
                    successful_access_alert(),
                    layers_camadas_component(),
                    map_buttons_teste(),

                ],
            ),
        ],
    )
