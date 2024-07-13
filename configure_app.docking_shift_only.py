#!/usr/local/bin/python3

import dearpygui.dearpygui as dpg

dpg.create_context()
dpg.configure_app(docking=True, docking_shift_only=True)
dpg.create_viewport(title=f"Test - {dpg.get_dearpygui_version()}", width=700, height=900)


with dpg.window(label="Window 1"):
    # Changing this option dynamically doesn't really work. It must be set at the very start.

    # def on_option(sender, checked, opt_name):
    #     args = {opt_name: checked}
    #     dpg.configure_app(**args)

    # with dpg.group(horizontal=True):
    #     for opt in ("docking_shift_only", ):
    #         dpg.add_checkbox(label=opt, callback=on_option, user_data=opt, default_value=False)

    dpg.add_text("Lorem ipsum")

with dpg.window(label="Window 2", pos=(300, 0)):
    dpg.add_text("dolor sit")

dpg.setup_dearpygui()
dpg.show_viewport()
dpg.start_dearpygui()
dpg.destroy_context()
