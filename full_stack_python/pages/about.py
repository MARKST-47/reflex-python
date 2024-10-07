import reflex as rx
from .base_page import base_page

def about_page() -> rx.Component:
    return base_page(
        rx.vstack(
            rx.heading("About Us", size="9"),
            rx.text(
                "Something. Everything. Nothing.",
                size="5",
            ),
            spacing="5",
            justify="center",
            text_align="center",
            align="center",
            min_height="85vh",
        ),
    )
