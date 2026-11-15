from nicegui import ui

SMALL_TEXT_SIZE = "75px"


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



def root():

    ui.add_css('''
        @import url('https://fonts.googleapis.com/css2?family=Bitcount+Grid+Single:wght@100..900&family=Special+Gothic:wght@400..700&display=swap');
        :root {
            --nicegui-default-padding: 0rem;
            --nicegui-default-gap: 0rem;
        }
        .nicegui-content {
            height: 100vh;
            width: 100vw;
        }
    ''')
    ui.add_head_html('''
    <style type="text/tailwindcss">
        body {
            font-family: "Bitcount Grid Single";
            font-size: 150px;
            text-align: center;
        }
    </style>
    ''')

    def pips(number):
        with ui.grid(columns=3).classes("gap-4"):
            for i in range(3):
                if i < number:
                    ui.html("", tag="div", sanitize=False).classes("w-14 h-14 bg-red rounded-full")
                else:
                    ui.html("", tag="div", sanitize=False).classes("w-14 h-14 bg-gray-900 rounded-full")

    with ui.grid(columns=len(display.keys())).classes("w-full h-full flex-row justify-between bg-gray-700 text-red"):
        for section, content in display.items():
            with ui.column().classes("flex-col justify-center items-center"):
                for element, value in content.items():
                    if element == "small":
                        ui.label().classes(f"flex justify-center content-center text-[{SMALL_TEXT_SIZE}]").bind_text(display, (section, element))
                    elif element == "pips":
                        pips(value)
                    else:
                        ui.label().classes("flex justify-center content-center").bind_text(display, (section, element))

ui.run(root, title="Display Emulator")