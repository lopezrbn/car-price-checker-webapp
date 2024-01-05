import reflex as rx
import socket

config = rx.Config(
    app_name="car_prices_checker",
    api_url=("http://152.228.134.180:8000" if socket.gethostname() == "vps-955fe093" else "http://localhost:8000"),
    frontend_port=3000,
    backend_port=8000,
)