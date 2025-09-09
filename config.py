# [atual] /config.py
"""Configurações da aplicação."""
import os
from dotenv import load_dotenv

load_dotenv()

class Config:
    FLASK_SECRET_KEY: str = os.getenv('FLASK_SECRET_KEY', '')
    ROOT_PATH_PREFIX: str = os.getenv('ROOT_PATH_PREFIX', '/')
    KEYCLOAK_SERVER_URL: str = os.getenv('KEYCLOAK_SERVER_URL', '')
    KEYCLOAK_CLIENT_ID: str = os.getenv('KEYCLOAK_CLIENT_ID', '')
    KEYCLOAK_REALM_NAME: str = os.getenv('KEYCLOAK_REALM_NAME', '')
    KEYCLOAK_CLIENT_SECRET_KEY: str = os.getenv('KEYCLOAK_CLIENT_SECRET_KEY', '')
    NIT_DATABASE_HOST: str = os.getenv('NIT_DATABASE_HOST', '')
    NIT_DATABASE_NAME: str = os.getenv('NIT_DATABASE_NAME', '')
    NIT_DATABASE_PASSWORD: str = os.getenv('NIT_DATABASE_PASSWORD', '') 
    NIT_DATABASE_PORT: str = os.getenv('NIT_DATABASE_PORT', '') 
    NIT_DATABASE_USERNAME: str = os.getenv('NIT_DATABASE_USERNAME', '') 