import reflex as rx
import pandas as pd
import locale
from typing import Dict, List
from datetime import date
from .pipeline import make_prediction

from .data.cars_manuf_and_models import cars


locale.setlocale(locale.LC_ALL, "es_ES")


class State(rx.State):

    # Base vars
    current_year: int = date.today().year
    manufacturers_list: List[str] = list(cars.keys())
    models_list: List[str] = []
    years_list: List[str] = list(range(current_year, 1989, -1))
    fuels_list: List[str] = ["Diesel", "Gasolina", "Eléctrico"]
    transmissions_list: List[str] = ["Manual", "Automática"]
    selected_manufacturer: str = ""
    selected_model: str = ""
    selected_year: str = ""
    selected_fuel: str = ""
    selected_transmission: str = ""
    selected_horsepower: int = 0
    selected_kms: int = 0
    selected_doors: int = 0
    cars: Dict[str, List] = cars
    predicted_value: int = 0

    # Event handlers
    def set_selected_manufacturer(self, value):
        self.selected_manufacturer = value
        self.models_list = self.cars[value]
        self.selected_model = ""

    
    def search_handler(self):
        car_to_predict: Dict = {
            "year": int(self.selected_year) if self.selected_year != "" else 0,
            "month": 6,
            "km": int(self.selected_kms) if self.selected_kms != "" else 0,
            "power_hp": int(self.selected_horsepower) if self.selected_horsepower != "" else 0,
            "no_doors": 5,
            "age": self.current_year - (int(self.selected_year) if self.selected_year != "" else 0),
            "fuel": self.selected_fuel,
            "transmission": self.selected_transmission.lower(),
        }
        X_pred = pd.DataFrame([car_to_predict, ], index=[0])
        print(X_pred)
        self.predicted_value = make_prediction(self.selected_manufacturer, self.selected_model, X_pred)
        self.predicted_value = int(self.predicted_value)
        print(f"Predicted value: {self.predicted_value} €")
        return rx.redirect("/results")
    

    def back_handler(self):
        return rx.redirect("/")


    # Computed vars
    @rx.var
    def predicted_value_formatted(self):
        return locale.format_string("%d", self.predicted_value, grouping=True)