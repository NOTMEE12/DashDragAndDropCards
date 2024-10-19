import dash_mantine_components as dmc
from dash import dcc

from .column import get_layout as get_column_layout
import data
from components.theme_toggle import get_layout as get_theme_toggle_layout


def get_layout():
    return dmc.MantineProvider(
        children=[
            dmc.Flex(
                [
                    dmc.NumberInput(
                        value=1,
                        id=data.ids.input,
                        label="Input",
                        description="Once changed should update the layout",
                        m="md",
                        size="md",
                        w="100%",
                    ),
                    get_theme_toggle_layout(),
                ],
                align="end",
                h="130px",
            ),
            dmc.ScrollArea(
                [
                    dmc.SimpleGrid(
                        # if I have get_columns_layout here it won't work because I have "dynamic" layouts
                        # that's why I have mirror, and it creates nice transition
                        get_columns_layout(is_mirror=True),
                        cols=data.column_amount,
                        miw=data.column_amount * 450,
                        spacing="sm",
                        m=10,
                        id=data.ids.grid,
                    ),
                    dmc.SimpleGrid(
                        children=get_columns_layout(is_mirror=True),
                        cols=data.column_amount,
                        miw=data.column_amount * 450,
                        spacing="sm",
                        mt=100,
                        m=10,
                        id=data.ids.mirror_container,
                    ),
                ],
                type="auto",
                offsetScrollbars=True,
                scrollbarSize=16,
                scrollbars="xy",
                m="sm",
                h="calc(100vh - 130px - 40px)",
            ),
            # data used for determining where the card was moved and from.
            dcc.Store(id=data.ids.output_store_card_id, storage_type="memory"),
            dcc.Store(id=data.ids.output_store_column_id, storage_type="memory"),
            dcc.Store(id=data.ids.output_store_old_column_id, storage_type="memory"),
            dcc.Store(id=data.ids.output_store_position_id, storage_type="memory"),
            dmc.NotificationProvider(position="bottom-left", limit=15, autoClose=5500),
            dmc.Container(id=data.ids.notifications),
            # dmc.Flex(id=data.ids.output_data, align="flex-start", opacity=0.7),
        ],
        id=data.ids.mantine_provider,
    )


def get_columns_layout(is_mirror=False):
    return [
        get_column_layout(
            col,
            sorted(
                filter(
                    lambda card: card[1]["column"] == col, data.card_positions.items()
                ),
                key=lambda card: card[1]["index"],
            ),
            is_mirror,
        )
        for col in range(data.column_amount)
    ]
