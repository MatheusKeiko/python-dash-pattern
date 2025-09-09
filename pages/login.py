# [atual] pages/login.py
"""Página de login do aplicativo Dash."""
import dash
from layouts.login_layout import create_login_layout

dash.register_page(__name__, path="/login")

layout = create_login_layout()
