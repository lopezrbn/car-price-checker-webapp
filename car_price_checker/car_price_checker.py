import reflex as rx
from .pages.index import index
from .pages.results import results


app = rx.App()
app.add_page(index)
app.add_page(results)
