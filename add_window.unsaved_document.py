#!/usr/local/bin/python3

import dearpygui.dearpygui as dpg

dpg.create_context()
dpg.create_viewport(title=f"Test - {dpg.get_dearpygui_version()}", width=700, height=700)

with dpg.window(label="Regular window", width=200):
    dpg.add_text("Lorem ipsum")

with dpg.window(label="Unsaved doc", pos=(220, 0), width=200, unsaved_document=True):
    dpg.add_text("dolor sit")

dpg.setup_dearpygui()
dpg.show_viewport()
dpg.start_dearpygui()
dpg.destroy_context()
