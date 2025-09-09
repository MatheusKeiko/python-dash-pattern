# [atual] pages/index.py
"""
Módulo que define a página inicial de redirecionamento do aplicativo Dash.

Inclui:
- Registro da página como a raiz do aplicativo.
- Redirecionamento automático para a página de login ao acessar a raiz.
"""

import dash
from dash import dcc
from config import Config

dash.register_page(__name__, path="/")
layout = dcc.Location(
    id="redirect",
    href=f"{Config.ROOT_PATH_PREFIX.rstrip('/')}/login",
    refresh=True,
)
