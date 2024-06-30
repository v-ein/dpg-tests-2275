#!/usr/local/bin/python3

import dearpygui.dearpygui as dpg

dpg.create_context()
dpg.create_viewport(title=f"Test - {dpg.get_dearpygui_version()}", width=500, height=750)
 
with dpg.window() as wnd:
    dpg.set_primary_window(dpg.last_item(), True)
    dpg.add_button(label="Regular", callback=lambda: print("Click!"))
    dpg.add_button(label="Auto-repeat", repeat=True, callback=lambda: print("Click!"))

dpg.setup_dearpygui()
dpg.show_viewport()
dpg.start_dearpygui()
dpg.destroy_context()
