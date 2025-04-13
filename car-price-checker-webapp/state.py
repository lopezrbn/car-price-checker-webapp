import reflex as rx
import pandas as pd
import requests
from typing import Dict, List
from datetime import date
# from .pipeline import make_prediction

from .data.cars_manuf_and_models import cars


def make_prediction(data):
    api_url = "http://api.lopezrbn.com/predict"
    response = requests.post(api_url, json=data)
    return response.status_code, response.json()


class State(rx.State):

    # Base vars
    current_year: int = date.today().year
    manufacturers_list: List[str] = list(cars.keys())
    models_list: List[str] = []
    years_list: List[str] = list(range(current_year, 2009, -1))
    months_list: List[str] = list(range(1, 13))
    fuels_list: List[str] = ["Diesel", "Gasoline", "Electric", "Hybrid", "Gasoline hybrid", "Diesel hybrid"]
    transmissions_list: List[str] = ["Manual", "Automatic"]
    cars: Dict[str, List] = cars
    selected_manufacturer: str = ""
    selected_model: str = ""
    selected_year: str = ""
    selected_month: str = ""
    selected_fuel: str = ""
    selected_transmission: str = ""
    selected_power: int = 0
    selected_kms: int = 0
    selected_doors: int = 0
    predicted_value: int = 0
    api_response_status = 0

    def reset_selected_vars(self):
        self.selected_manufacturer = ""
        self.selected_model = ""
        self.selected_year = ""
        self.selected_month = ""
        self.selected_fuel = ""
        self.selected_transmission = ""
        self.selected_power = 0
        self.selected_kms = 0
        self.selected_doors = 0
        self.predicted_value = 0
        self.api_response_status = 0

    # Event handlers
    def set_selected_manufacturer(self, value):
        self.selected_manufacturer = value
        self.models_list = self.cars[value]
        self.selected_model = ""

    def _format_fuel(self, value):
        fuel_formatted = {
            "Diesel": "d",
            "Gasoline": "g",
            "Electric": "e",
            "Hybrid": "h",
            "Gasoline hybrid": "hg",
            "Diesel hybrid": "hd"
        }
        return fuel_formatted[value]


    def search_handler(self):
        car_to_predict: Dict = {
            "manufacturer": self.selected_manufacturer,
            "model": self.selected_model,
            "month": int(self.selected_month) if self.selected_month != "" else 0,
            "year": int(self.selected_year) if self.selected_year != "" else 0,
            "kms": int(self.selected_kms) if self.selected_kms != "" else 0,
            "fuel": self._format_fuel(self.selected_fuel),
            "transmission": self.selected_transmission.lower()[0],
            "power_hp": int(self.selected_power) if self.selected_power != "" else 0,
            # "no_doors": 5,
            # "age": self.current_year - (int(self.selected_year) if self.selected_year != "" else 0) - 1,
        }
        # X_pred = pd.DataFrame([car_to_predict, ], index=[0])
        # print(X_pred)
        print(f"Predicting for {car_to_predict}")
        # self.predicted_value = make_prediction(self.selected_manufacturer, self.selected_model, X_pred)
        self.api_response_status, self.predicted_value = make_prediction(car_to_predict)
        self.predicted_value = self.predicted_value["Predicted price"]
        if self.api_response_status != 200:
            self.predicted_value = "API error: " + str(self.api_response_status)
        else:
            if self.predicted_value < 0:
                self.predicted_value = "Not enough data to predict the value of this car"
            else:
                self.predicted_value = int(self.predicted_value)
        print(f"Predicted value: {self.predicted_value}")
        return rx.redirect("/results")
    

    def back_handler(self):
        self.reset_selected_vars()
        return rx.redirect("/")


    # Computed vars
    @rx.var
    def predicted_value_formatted(self):
        if isinstance(self.predicted_value, int):
            predicted_value_formatted = ""
            for i, digit in enumerate(str(self.predicted_value)[::-1]):
                if i % 3 != 0:
                    predicted_value_formatted += digit
                else:
                    predicted_value_formatted += "." + digit
            predicted_value_formatted = predicted_value_formatted[-1:0:-1]
            predicted_value_formatted += " €"
            return predicted_value_formatted
        else:
            return self.predicted_value