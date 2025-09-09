# [atual] layouts/login_layout.py
"""Layout da página de login."""
from config import Config
from dash import html, dcc
import dash_mantine_components as dmc


def _icon(name: str, size: int = 18):
    # Usa Boxicons (carregado no external_stylesheets do app)
    return html.I(className=f"bx {name}", style={"fontSize": f"{size}px", "lineHeight": 1})

def create_login_layout() -> html.Main:
    """Cria o layout da página de login usando apenas Mantine, com ícones alinhados."""
    return html.Main(
        className="login-body",
        children=[
            dmc.Center(
                style={"width": "100%", "minHeight": "100vh"},
                children=[
                    dmc.Paper(
                        withBorder=False,
                        shadow="xl",
                        radius="lg",
                        p=26,
                        style={
                            "backgroundColor": "#3c3c3c",
                            "width": "100%",
                            "maxWidth": 360,
                            "animation": "fadeIn 0.5s ease-out",
                        },
                        children=[
                            # Logo principal
                            html.Img(
                                src=f"{Config.ROOT_PATH_PREFIX.rstrip('/')}/assets/src/images/login/colorido/itaipuparquetec_logotipo_branco.png",
                                style={"width": "300px", "display": "block", "margin": "0 auto 16px"},
                                alt="Itaipu Parquetec logo",
                            ),

                            # Inputs com ícones
                            dmc.Stack(
                                gap="sm",
                                children=[
                                    dmc.TextInput(
                                        id="username",
                                        placeholder="Usuário",
                                        size="md",
                                        radius="sm",
                                        required=True,
                                        leftSection=_icon("bx-user"),
                                        leftSectionWidth=36,  # reserva espaço p/ o ícone
                                        styles={
                                            "input": {
                                                "backgroundColor": "#4c4c4c",
                                                "color": "#f0f0f0",
                                                "borderColor": "#4c4c4c",
                                                "height": 45,
                                            },
                                            "leftSection": {"color": "#d9d9d9"},
                                            # evita que o clique no ícone roube o foco do input
                                            "section": {"pointerEvents": "none"},
                                        },
                                    ),
                                    dmc.PasswordInput(
                                        id="password",
                                        placeholder="Senha",
                                        size="md",
                                        radius="sm",
                                        required=True,
                                        # visibilityToggle=True,
                                        leftSection=_icon("bx-lock"),
                                        leftSectionWidth=36,
                                        styles={
                                            "input": {
                                                "backgroundColor": "#4c4c4c",
                                                "color": "#f0f0f0",
                                                "borderColor": "#4c4c4c",
                                                "height": 45,
                                            },
                                            "leftSection": {"color": "#d9d9d9"},
                                            # "section": {"pointerEvents": "none"},
                                        },
                                    ),
                                    # Mensagem de erro opcional
                                    dmc.Text(
                                        id="password-error",
                                        children="Por favor, insira sua senha",
                                        size="sm",
                                        style={"display": "none", "color": "#a0a0a0", "fontWeight": 500},
                                    ),
                                ],
                            ),

                            # Botão "Entrar"
                            dmc.Button(
                                "Entrar",
                                id="login-button",
                                size="md",
                                fullWidth=True,
                                mt=28,
                                radius="sm",
                                variant="filled",
                                color="gray",
                                styles={
                                    "root": {
                                        "background": "linear-gradient(135deg, #606060 0%, #808080 100%)",
                                        "color": "#ffffff",
                                        "border": "none",
                                        "textTransform": "uppercase",
                                        "fontWeight": 600,
                                        "padding": "13px 36px",
                                        "borderRadius": "5px",
                                        "letterSpacing": "1px",
                                        "cursor": "pointer",
                                        "transition": "all 0.3s ease",
                                        "boxShadow": "0 4px 6px rgba(0, 0, 0, 0.3)",
                                        "&:hover": {
                                            "background": "linear-gradient(135deg, #707070 0%, #909090 100%)",
                                            "transform": "translateY(-2px)",
                                            "boxShadow": "0 6px 8px rgba(0, 0, 0, 0.4)",
                                        },
                                        "&:active": {
                                            "transform": "translateY(0)",
                                        },
                                    }
                                },
                            ),

                            # Hidden submit (se você usa Enter/n_submit em algum lugar)
                            dcc.Input(id="hidden-submit", type="text", style={"display": "none"}, n_submit=0),

                            # Saída e erro
                            html.Div(id="login-output"),
                            dmc.Text(
                                id="error-message",
                                children="",
                                ta="center",
                                mt="sm",
                                style={"display": "none", "color": "#ff6b6b", "fontWeight": 600},
                            ),

                            dmc.Divider(my=16, size="sm", color="#606060"),
                            dmc.Text("APOIO:", ta="center", fw=600, c="dimmed"),

                            # Logos de apoio
                            dmc.Stack(
                                gap=6,
                                align="center",
                                mt=6,
                                children=[
                                    html.Img(
                                        src=f"{Config.ROOT_PATH_PREFIX.rstrip('/')}/assets/src/images/login/colorido/itaipu_gov_colorido_branco.png",
                                        style={"maxWidth": "100%", "height": "auto"},
                                        alt="Itaipu Binacional Logo",
                                    ),
                                    html.Img(
                                        src=f"{Config.ROOT_PATH_PREFIX.rstrip('/')}/assets/src/images/login/colorido/nit_branco_hq.png",
                                        style={"width": "135px", "height": "37px"},
                                        alt="Sanepar Logo",
                                    ),
                                ],
                            ),
                        ],
                    ),
                ],
            ),
        ],
    )

