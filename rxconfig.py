import reflex as rx
import socket

front_port = 3002
back_port = 8002

config = rx.Config(
    app_name="car_prices_checker",
    api_url=("http://152.228.134.180" if socket.gethostname() == "vps-955fe093" else f"http://localhost:{back_port}"),
    frontend_port=front_port,
    backend_port=back_port,
)