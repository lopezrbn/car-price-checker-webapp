import reflex as rx
from ..state import State


def results():
    return rx.vstack(
        rx.hstack(
            rx.text("Manufacturer:"),
            rx.text(State.selected_manufacturer),
        ),
        rx.hstack(
            rx.text("Model:"),
            rx.text(State.selected_model),
        ),
        rx.hstack(
            rx.text("Year:"),
            rx.text(State.selected_year),
        ),
        rx.hstack(
            rx.text("Fuel:"),
            rx.text(State.selected_fuel),
        ),
        rx.hstack(
            rx.text("Transmission:"),
            rx.text(State.selected_transmission),
        ),
        rx.hstack(
            rx.text("Horsepower:"),
            rx.text(State.selected_horsepower),
        ),
        rx.hstack(
            rx.text("Kms:"),
            rx.text(State.selected_kms),
        ),
        rx.hstack(
            rx.text("Predicted value:"),
            rx.text(State.predicted_value),
        ),
        rx.button(
                "Back",
                on_click=State.back_handler,
            ),
    )