import reflex as rx
from ..state import State


def index():
    return rx.center(
        rx.vstack(
            rx.hstack(
                rx.text("Manufacturer:"),
                rx.select(
                    State.manufacturers_list,
                    value=State.selected_manufacturer,
                    placeholder="Select manufacturer",
                    on_change=State.set_selected_manufacturer,
                ),
            ),
            rx.cond(
                State.selected_manufacturer != "",
                rx.hstack(
                    rx.text("Model:"),
                    rx.select(
                        State.models_list,
                        value=State.selected_model,
                        placeholder="Select model",
                        on_change=State.set_selected_model,
                    ),
                ),
            ),
            rx.cond(
                State.selected_model != "",
                rx.hstack(
                    rx.text("Year:"),
                    rx.select(
                        State.years_list,
                        value=State.selected_year,
                        placeholder="Select year",
                        on_change=State.set_selected_year,
                    ),
                ),
            ),
            rx.cond(
                State.selected_year != "",
                rx.hstack(
                    rx.text("Fuel:"),
                    rx.select(
                        State.fuels_list,
                        value=State.selected_fuel,
                        placeholder="Select fuel",
                        on_change=State.set_selected_fuel,
                    ),
                ),
            ),
            rx.cond(
                State.selected_fuel != "",
                rx.hstack(
                    rx.text("Transmission:"),
                    rx.select(
                        State.transmissions_list,
                        value=State.selected_transmission,
                        placeholder="Select transmission",
                        on_change=State.set_selected_transmission,
                    ),
                ),
            ),
            rx.cond(
                State.selected_transmission != "",
                rx.hstack(
                    rx.text("Horsepower:"),
                    rx.number_input(
                        value=State.selected_horsepower,
                        placeholder="Enter horsepower",
                        on_change=State.set_selected_horsepower,
                    ),
                ),
            ),
            rx.cond(
                State.selected_horsepower != 0,
                rx.hstack(
                    rx.text("Kms:"),
                    rx.number_input(
                        value=State.selected_kms,
                        placeholder="Enter kms",
                        on_change=State.set_selected_kms,
                    ),
                ),
            ),
            rx.button(
                "Search",
                on_click=State.search_handler,
            ),
        ),
    )