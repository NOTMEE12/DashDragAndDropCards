import dash_mantine_components as dmc
from dash_iconify import DashIconify as Icon
from dash import callback, Input, Output
from data import ids


# toggle theme to dark
@callback(
    Output(ids.mantine_provider, "forceColorScheme", allow_duplicate=True),
    Input(ids.light_theme_toggle, "n_clicks"),
    prevent_initial_call=True,
)
def change_theme_to_dark(_):
    return "dark"


# toggle theme to light
@callback(
    Output(ids.mantine_provider, "forceColorScheme", allow_duplicate=True),
    Input(ids.dark_theme_toggle, "n_clicks"),
    prevent_initial_call=True,
)
def change_theme_to_light(_):
    return "light"


def get_layout():
    light_icon = dmc.ActionIcon(
        Icon(icon="tabler:moon"),
        darkHidden=True,
        id=ids.light_theme_toggle,
        color="gray",
        variant="light",
        radius="sm",
        size="xl",
    )
    dark_icon = dmc.ActionIcon(
        Icon(icon="tabler:sun"),
        lightHidden=True,
        id=ids.dark_theme_toggle,
        color="gray",
        variant="light",
        radius="sm",
        size="xl",
    )
    return dmc.Container([light_icon, dark_icon], m="md", ml=0)
