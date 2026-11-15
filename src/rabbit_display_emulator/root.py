from nicegui import ui

from rabbit_display_emulator.display import Display, Shared, Side

SMALL_TEXT_SIZE = "75px"

def root(display: Display):

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

    def render_pips(side: Side):
        with ui.grid(columns=3).classes("gap-4"):
            for i in range(3):
                with ui.element('div').classes("relative w-14 h-14"):
                    ui.html("", tag="div", sanitize=False).classes(
                        "absolute inset-0 rounded-full bg-gray-900")
                    ui.html("", tag="div", sanitize=False).classes(
                        "absolute inset-0 rounded-full bg-red").bind_visibility_from(
                        side, 'pips', backward=lambda n, i=i: i < n)

    def render_side(side: Side):
        with ui.column().classes("flex-col justify-center items-center"):
            ui.label().classes("flex justify-center content-center").bind_text_from(side, "text")
            ui.label().classes("flex justify-center content-center").bind_text_from(side, "large")
            ui.label().classes(f"flex justify-center content-center text-[{SMALL_TEXT_SIZE}]").bind_text_from(side, "small")
            render_pips(side)

    def render_shared(shared: Shared):
        with ui.column().classes("flex-col justify-center items-center"):
            ui.label().classes("flex justify-center content-center").bind_text_from(shared, "time")
            ui.label().classes(f"flex justify-center content-center text-[{SMALL_TEXT_SIZE}]").bind_text_from(shared, "small")

    with ui.grid(columns=3).classes("w-full h-full flex-row justify-between bg-gray-700 text-red"):
        render_side(display.left)
        render_shared(display.shared)
        render_side(display.right)

