import reflex as rx
from .base_page import base_page

def login_page():
    return base_page(
        rx.center(
            rx.vstack(
                rx.heading("Login to our Website!"),
                rx.box(
                    rx.vstack(
                        rx.input(
                            placeholder="Username",
                            size="3",
                        ),
                        rx.input(
                            type="password",
                            placeholder="Password",
                            size="3",
                        ),
                        rx.button(
                            "Log in",
                            size="3",
                            width="6em",
                        ),
                        align="center",
                        spacing="4",
                    ),
                    border="1px solid #191970",
                    padding="16px",
                    width="400px",
                    border_radius="8px",
                ),
                rx.text(
                    "Don't have an account yet? ",
                    rx.link("Sign up here.", href="/signup"),
                    color="gray",
                ),
                text_align="center",
                align="center",
                justify="center",
                min_height="85vh",
            ),
        ),
    )