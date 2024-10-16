import reflex as rx

def navbar_link(text: str, url: str) -> rx.Component:
    return rx.link(rx.text(text, size="4", weight="medium"), href=url)


def navbar() -> rx.Component:
    return rx.box(
        rx.desktop_only(
            rx.hstack(
                rx.hstack(
                    rx.image(
                        src="/logo.JPG",
                        loading="eager",
                        width="2.25em",
                        height="auto",
                        border_radius="25%",
                    ),
                    rx.heading("MarkT", size="7", weight="bold"),
                    align_items="center",
                ),
                rx.hstack(
                    navbar_link("Home", "/#"),
                    navbar_link("About", "/about"),
                    navbar_link("Pricing", "/pricing"),
                    navbar_link("Contact", "/contact"),
                    spacing="5",
                ),
                rx.hstack(
                    rx.button(
                        "Sign Up",
                        size="3",
                        variant="outline",
                        on_click=rx.redirect("/signup")
                    ),
                    rx.button(
                        "Log In",
                        size="3",
                        on_click=rx.redirect("/login")
                    ),
                    spacing="4",
                    justify="end",
                ),
                justify="between",
                align_items="center",
            ),
        ),
        rx.mobile_and_tablet(
            rx.hstack(
                rx.hstack(
                    rx.image(
                        src="/logo.JPG",
                        loading="eager",
                        width="2em",
                        height="auto",
                        border_radius="25%",
                    ),
                    rx.heading("MarkT", size="6", weight="bold"),
                    align_items="center",
                ),
                rx.menu.root(
                    rx.menu.trigger(rx.icon("menu", size=30)),
                    rx.menu.content(
                        rx.menu.item("Home", on_click=rx.redirect("/#")),
                        rx.menu.item("About", on_click=rx.redirect("/about")),
                        rx.menu.item("Pricing", on_click=rx.redirect("/pricing")),
                        rx.menu.item("Contact", on_click=rx.redirect("/contact")),
                        rx.menu.separator(),
                        rx.menu.item("Log in", on_click=rx.redirect("/login")),
                        rx.menu.item("Sign up", on_click=rx.redirect("/signup")),
                    ),
                    justify="end",
                ),
                justify="between",
                align_items="center",
            ),
        ),
        bg=rx.color("accent", 3),
        padding="1em",
        # position="fixed",
        # top="0px",
        # z_index="5",
        width="100%",
    )
