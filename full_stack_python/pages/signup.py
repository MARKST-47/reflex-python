import reflex as rx
from .base_page import base_page

def signup_page():
    """the sign up page."""
    return base_page(
        rx.center(
            rx.vstack(
                rx.heading("Sign up to our Website!"),
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
                        rx.input(
                            type="password",
                            placeholder="Confirm password",
                            size="3",
                        ),
                        rx.button(
                            "Sign up",
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
                    "Already have an account? ",
                    rx.link("Sign in here.", href="/login"),
                    color="gray",
                ),
                text_align="center",
                align="center",
                justify="center",
                min_height="85vh",
            ),
        ),
    )