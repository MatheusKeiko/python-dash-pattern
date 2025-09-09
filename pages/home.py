# [atual] pages/home.py
"""Página principal após login."""
import dash
from layouts.home_layout import create_main_layout

dash.register_page(__name__, path="/home")

layout = create_main_layout()
