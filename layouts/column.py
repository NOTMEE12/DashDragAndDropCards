from typing import Optional, Sequence

import dash_mantine_components as dmc
from dash_iconify import DashIconify as Icon

from .card_layout import get_layout as get_card_layout
from data import ids


def get_layout(
    column_id: int,
    card_positions: Sequence[tuple[int, dict[str, int]]],
    is_mirror: Optional[bool] = False,
):
    def get_header():
        return dmc.Flex(
            [
                dmc.Title(f"Column {column_id}", order=3),
                dmc.ActionIcon(
                    Icon(icon="tabler:pencil"),
                    variant="light",
                    color="gray",
                    disabled=is_mirror,
                ),
            ],
            justify="space-between",
        )

    def get_content():
        return dmc.Stack(
            [
                get_card_layout(card_pos, is_mirror=is_mirror)
                for card_pos in card_positions
            ],
            **({"id": ids.get_container_id(column_id)} if not is_mirror else {}),
            p="sm",
            pb="lg",
            variant="filled",
            bg="light-dark(var(--mantine-color-dark-light), var(--mantine-color-dark-filled))",
            style={"borderRadius": "1rem"},
        )

    return dmc.Paper(
        [get_header(), dmc.Space(h="sm"), get_content()],
        withBorder=True,
        p="sm",
        shadow="sm",
        h="fit-content",
        opacity=0.5 if is_mirror else 1.0,
    )
