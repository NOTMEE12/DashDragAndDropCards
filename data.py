from typing import Literal

column_amount: int = 4
"""Amount of columns per table"""
card_amount_inside_columns: int = 1
"""Amount of cards per column"""
theme: Literal["light", "dark"] = "light"
"""Default theme"""

table_dimensions: int = 10
"""How many tables of cards. Not to confuse with columns."""

card_positions: dict[int, dict[int, dict[str, int]]] = {
    table: {
        (col * card_amount_inside_columns + card_id): {"column": col, "index": card_id}
        for card_id in range(card_amount_inside_columns)
        for col in range(column_amount)
    }
    for table in range(table_dimensions)
}


class ids:
    get_container_id = lambda arg: {"type": "drag-container", "index": arg}
    get_card_id = lambda arg: {"type": "card", "index": arg}

    output_store_card_id = "output-store-card-id"
    output_store_column_id = "output-store-column-id"
    output_store_old_column_id = "output-store-old-column-id"
    output_store_position_id = "output-store-position-id"

    notifications = "notifications"
    mirror_container = "mirror"
    input = "input"
    grid = "grid"

    mantine_provider = "mantine-provider"

    light_theme_toggle = "light-theme-toggle"
    dark_theme_toggle = "dark-theme-toggle"
