from dash import (
    ALL,
    Dash,
    no_update,
    Input,
    Output,
    ClientsideFunction,
    clientside_callback,
    State,
    set_props,
)
from dash._dash_renderer import _set_react_version

_set_react_version("18.2.0")

import dash_mantine_components as dmc
import data
from layouts import get_layout, get_columns_layout


app = Dash(
    __name__,
    external_scripts=[
        "https://cdnjs.cloudflare.com/ajax/libs/dragula/3.7.2/dragula.min.js"
    ],
    external_stylesheets=dmc.styles.ALL,
)

clientside_callback(
    ClientsideFunction(namespace="draggable", function_name="make_draggable"),
    Output(data.ids.get_container_id(ALL), "data-drag"),
    [
        Input(data.ids.get_container_id(ALL), "id"),
        Input(data.ids.output_store_card_id, "id"),
        Input(data.ids.output_store_column_id, "id"),
        Input(data.ids.output_store_old_column_id, "id"),
        Input(data.ids.output_store_position_id, "id"),
    ],
)


@app.callback(
    Output(data.ids.grid, "children"),
    Output(data.ids.mirror_container, "children"),
    Input(data.ids.input, "value"),
)
def show_data(table: str):
    set_props(data.ids.grid, {"children": []})
    return get_columns_layout(int(table)), get_columns_layout(
        int(table), is_mirror=True
    )


@app.callback(
    Output(data.ids.notifications, "children"),
    Output(data.ids.mirror_container, "children", allow_duplicate=True),
    Input(data.ids.output_store_card_id, "data"),
    Input(data.ids.output_store_column_id, "data"),
    Input(data.ids.output_store_old_column_id, "data"),
    Input(data.ids.output_store_position_id, "data"),
    State(data.ids.input, "value"),
    prevent_initial_call=True,
)
def show_changes(card_id, column_id, old_column_id, position_id, table: str):
    table = int(table)
    if (
        card_id is None
        or column_id is None
        or old_column_id is None
        or position_id is None
    ):
        return no_update, get_columns_layout(table, is_mirror=True)

    column = int(column_id)
    old_col = int(old_column_id)

    old_card_positions = data.card_positions[table].copy()

    data.card_positions[table][card_id]["column"] = column

    def filter_every_card_down_from_old_pos(card):
        _, card_pos = card
        return (
            card_pos["column"] == old_col
            and card_pos["index"] >= data.card_positions[table][card_id]["index"] + 1
        )

    for card_id_, card_data_ in filter(
        filter_every_card_down_from_old_pos, data.card_positions[table].items()
    ):
        data.card_positions[table][card_id_]["index"] -= 1

    if int(position_id) != -1:

        def filter_every_card_down_from_new_pos(card):
            _, card_pos = card
            return card_pos["column"] == column and card_pos["index"] >= new_position

        new_position = old_card_positions[int(position_id)]["index"]
        for card_id_, card_data in filter(
            filter_every_card_down_from_new_pos, data.card_positions[table].items()
        ):
            data.card_positions[table][card_id_]["index"] += 1

        data.card_positions[table][card_id]["index"] = new_position
    else:
        data.card_positions[table][card_id]["index"] = (
            len(
                tuple(
                    filter(
                        lambda card: card[1]["column"] == column,
                        old_card_positions.items(),
                    )
                )
            )
            - 1
        )

    return (
        dmc.Notification(
            title=f"Moved card {card_id} from column {old_column_id} to column {column_id} on position "
            f"{'Last' if position_id == -1 else 'Higher than card ' + str(position_id)}",
            message="",
            action="show",
            withBorder=True,
        ),
        get_columns_layout(table, is_mirror=True),
    )


if __name__ == "__main__":
    app.layout = get_layout
    app.run(debug=True)
