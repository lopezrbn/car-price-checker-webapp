import reflex as rx
from ..state import State


def results():
    return rx.center(
        rx.vstack(
            rx.text(f"Your {State.selected_year} {State.selected_manufacturer} {State.selected_model}, {State.selected_fuel} fuel, {State.selected_transmission} transmission, {State.selected_horsepower} HP and {State.selected_kms} Kms is worth:"),
            rx.spacer(),
            rx.heading(f"{State.predicted_value_formatted} €"),
            rx.spacer(),
            rx.button(
                "Back",
                on_click=State.back_handler,
            ),
        ),
        height="90vh",
    )