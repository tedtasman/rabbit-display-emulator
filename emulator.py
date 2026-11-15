from nicegui import ui
from rabbit_display_emulator import root

display = {
    "left": {
        "text": "ABC",
        "large": "123",
        "small": "123",
        "pips": 1
    },
    "shared": {
        "time": "12:34",
        "small": "12",
    },
    "right": {
        "text": "DEF",
        "large": "456",
        "small": "456",
        "pips": 2
    },
}


ui.run(lambda: root(display), title="Display Emulator")