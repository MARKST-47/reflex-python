import reflex as rx
from full_stack_python.components.navbar import navbar

def base_page(child: rx.Component, *args, **kwargs) -> rx.Component:
    return rx.fragment(
        navbar(),
        rx.box(
            child,
            # bg=rx.color("black", 3),
            padding="1em",
            width="100%",
        ),
        rx.color_mode.button(position="bottom-right"),
        rx.logo(),
    )