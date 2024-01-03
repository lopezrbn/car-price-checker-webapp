import reflex as rx
from .pages.index import index
from .pages.results import results
from .state import State


# Add state and page to the app.
app = rx.App(
    state=State
)
app.add_page(index)
app.add_page(results)
app.compile()
