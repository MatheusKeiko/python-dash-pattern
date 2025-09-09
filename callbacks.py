# [atual] callbacks.py
"""Registro centralizado de callbacks dinâmicos via import de módulos."""

from __future__ import annotations

import importlib
import logging
from typing import Final, Iterable

logger = logging.getLogger(__name__)

# Lista padrão de módulos que expõem a função `register_callbacks()`.
MODULES: Final[list[str]] = [
    "auth.auth",
    "components.map.map_alerts.callbacks",
    "components.map.map_dropdown.callbacks",
]


def _import_and_register(dotted_path: str) -> None:
    """Importa um módulo e executa sua `register_callbacks()` se existir.

    Args:
        dotted_path: Caminho pontilhado do módulo (ex.: "pkg.sub.mod").

    Raises:
        Exception: Propaga exceções de import ou execução para o chamador
            lidar com logging adequado.
    """
    module = importlib.import_module(dotted_path)
    fn = getattr(module, "register_callbacks", None)
    if callable(fn):
        fn()
        logger.info("Callbacks registrados: %s", dotted_path)
    else:
        logger.info("Somente importado (legado): %s", dotted_path)


def register(extra_modules: Iterable[str] | None = None) -> None:
    """Registra callbacks de todos os módulos padrão e extras.

    Faz o import dinâmico de cada módulo listado e chama sua função
    `register_callbacks()` quando disponível. Módulos sem essa função são
    apenas importados (para efeitos de side-effects/legado).

    Args:
        extra_modules: Coleção opcional de módulos adicionais para registrar.

    Notes:
        Qualquer falha em um módulo é logada, mas não interrompe o processo
        de registro dos demais.
    """
    modules = list(MODULES) + list(extra_modules or [])
    for dotted in modules:
        try:
            _import_and_register(dotted)
        except Exception as exc:  # não derruba o app por uma feature
            logger.exception("Falha ao registrar callbacks %s: %s", dotted, exc)


__all__ = ["register", "MODULES"]
