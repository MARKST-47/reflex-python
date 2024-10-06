import reflex as rx
from rxconfig import config


class State(rx.State):
    """The app state."""
    count: int = 0

    def increment(self):
        self.count += 1
    
    def decrement(self):
        self.count -= 1


def index() -> rx.Component:
    # Welcome Page (Index)
    return rx.container(
        rx.color_mode.button(position="top-right"),
        rx.vstack(
            rx.heading("Welcome to Reflex!", size="9"),
            rx.text(
                "Get started by editing ",
                rx.code(f"{config.app_name}/{config.app_name}.py"),
                size="5",
            ),
            spacing="5",
            justify="center",
            min_height="85vh",
        ),
        rx.hstack(
            rx.button(
                'Decrement',
                color_scheme='red',
                on_click=State.decrement,
            ),
            rx.heading(State.count, font_size="2em"),
            rx.button(
                "Increment",
                color_scheme="green",
                on_click=State.increment,
            ),
            spacing="4",
        ),
        rx.logo(),
    )

app = rx.App()

app.add_page(index)
