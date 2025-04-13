import reflex as rx
from ..state import State


def create_select_line(text_label, options_param, value_param, placeholder_param, on_change_param):
    return rx.hstack(
        rx.box(
            rx.text(
                text_label,
            ),
            width="10em",
        ),
        rx.box(
            rx.select(
                options_param,
                value=value_param,
                placeholder=placeholder_param,
                on_change=on_change_param,
            ),
            width="15em",
        ),
        width="25em",
        justify="between",
    )


def create_number_input_line(text_label, value_param, placeholder_param, on_change_param):
    return rx.hstack(
        rx.box(
            rx.text(
                text_label,
            ),
            width="10em",
        ),
        rx.box(
            rx.input(
                type="number",
                value=value_param,
                placeholder=placeholder_param,
                on_change=on_change_param,
            ),
            width="15em",
        ),
        width="25em",
        justify="between"
    )


def index():
    return rx.center(
        
        rx.vstack(
            rx.heading("How much is your car worth?"),
            rx.spacer(),
            rx.text("Please, enter the following information:"),
            rx.spacer(),
            create_select_line("Manufacturer:", State.manufacturers_list, State.selected_manufacturer, "Select manufacturer", State.set_selected_manufacturer,),
            rx.cond(
                State.selected_manufacturer != "",
                create_select_line("Model:", State.models_list, State.selected_model, "Select model", State.set_selected_model,),
            ),
            rx.cond(
                State.selected_model != "",
                create_select_line("Year:", State.years_list, State.selected_year, "Select year", State.set_selected_year,),
            ),
            rx.cond(
                State.selected_year != "",
                create_select_line("Month:", State.months_list, State.selected_month, "Select month", State.set_selected_month,),
            ),
            rx.cond(
                State.selected_month != "",
                create_select_line("Fuel:", State.fuels_list, State.selected_fuel, "Select fuel", State.set_selected_fuel,),
            ),
            rx.cond(
                State.selected_fuel != "",
                create_select_line("Transmission:", State.transmissions_list, State.selected_transmission, "Select transmission", State.set_selected_transmission,),
            ),
            rx.cond(
                State.selected_transmission != "",
                create_number_input_line("Power (hp):", State.selected_power, "Enter kms", State.set_selected_power,),
            ),
            rx.cond(
                State.selected_power != 0,
                create_number_input_line("Kms:", State.selected_kms, "Enter kms", State.set_selected_kms,),
            ),
            rx.button(
                "Search",
                on_click=State.search_handler,
            ),
        ),
        height="90vh",
    )