from nicegui import app, ui
from rabbit_display_emulator import Driver, root, Display

display = Display()

driver = Driver(initial_display=display)
app.on_startup(driver.start)
app.on_shutdown(driver.stop)

if __name__ in {"__main__", "__mp_main__"}:
    ui.run(lambda: root(driver.display), title="Display Emulator")