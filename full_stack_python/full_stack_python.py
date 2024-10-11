import reflex as rx
from . import pages
from .pages.base_page import base_page
from rxconfig import config


class State(rx.State):
    """The app state."""

    count: int = 0
    label: str = "Welcome to Reflex!"
    color: str = "green"

    def handle_title_change(self, val):
        self.label = val

    def change_color(self):
        self.color = "blue"

    def reset_color(self):
        self.color = "green"


def index() -> rx.Component:
    # Welcome Page (Index)
    return base_page(
        rx.vstack(
            rx.heading(State.label, size="9"),
            rx.text(
                "Get started by editing.",
                rx.code(f"{config.app_name}/{config.app_name}.py"),
                size="5",
            ),
            rx.input(
                default_value=State.label,
                on_change=State.handle_title_change,
            ),
            rx.button(
                "COLOR",
                style={"background-color": State.color},
                on_mouse_over=State.change_color,
                on_mouse_out=State.reset_color,
            ),
            spacing="5",
            justify="center",
            text_align="center",
            align="center",
            min_height="85vh",
        ),
    )


app = rx.App()

app.add_page(index)
app.add_page(pages.about_page, route="/about")
app.add_page(pages.pricing_page, route="/pricing")
app.add_page(pages.contact_page, route="/contact")
app.add_page(pages.todo_page, route="/todo")