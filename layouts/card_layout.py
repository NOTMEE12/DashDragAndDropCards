from typing import Optional, Sequence

import dash_mantine_components as dmc

from data import ids


def get_layout(
    card_data: tuple[int, dict[str, int]], is_mirror: Optional[bool] = False
):
    card_id = card_data[0]
    card_column = card_data[1]["column"]
    card_index = card_data[1]["index"]
    return dmc.Paper(
        [
            dmc.Badge(
                "Badge",
                variant="light",
                color=("blue", "yellow", "green", "red")[card_data[0] % 4],
            ),
            dmc.Title(f"#{card_id}", fs="italic"),
            dmc.Text(
                "Content"
                if not is_mirror
                else f"Column: {card_column} | Index: {card_index}"
            ),
        ],
        withBorder=True,
        shadow="sm",
        p="sm",
        **({"id": ids.get_card_id(card_id)} if not is_mirror else {}),
    )
