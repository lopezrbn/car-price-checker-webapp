import reflex as rx
from .pages.index import index
from .pages.results import results


tab_title = "Car price checker"

app = rx.App()
app.add_page(index, title=tab_title)
app.add_page(results, title=tab_title)
