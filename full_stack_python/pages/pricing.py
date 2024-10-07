import reflex as rx
from .base_page import base_page

def pricing_page() -> rx.Component:
    return base_page(
        rx.vstack(
            rx.heading("Pricing", size="9", style={"text-decoration": "underline"}),
            rx.table.root(
                rx.table.header(
                    rx.table.row(
                        rx.table.column_header_cell("Differences"),
                        rx.table.column_header_cell("Basic"),
                        rx.table.column_header_cell("Professional"),
                        rx.table.column_header_cell("Enterprise"),
                    ),
                ),
                rx.table.body(
                    rx.table.row(
                        rx.table.row_header_cell("Space available"),
                        rx.table.cell("5GB"),
                        rx.table.cell("15GB"),
                        rx.table.cell("50GB"),
                    ),
                    rx.table.row(
                        rx.table.row_header_cell("Cloud facility"),
                        rx.table.cell("No"),
                        rx.table.cell("Yes"),
                        rx.table.cell("Yes"),
                    ),
                    rx.table.row(
                        rx.table.row_header_cell("24/7 Support"),
                        rx.table.cell("No"),
                        rx.table.cell("Yes"),
                        rx.table.cell("Yes"),
                    ),
                ),
                align="center",
                variant="surface",
                size="3",
            ),
            spacing="5",
            justify="center",
            text_align="center",
            align="center",
            min_height="85vh",
        ),
    )
