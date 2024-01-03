import reflex as rx
import socket

config = rx.Config(
    app_name="car_prices_checker",
    api_url=("http://152.228.134.180" if socket.gethostname() == "vps-955fe093" else "http://localhost:8001"),
    frontend_port=3001,
    backend_port=8001,
)