#!/usr/local/bin/python3

import dearpygui.dearpygui as dpg

dpg.create_context()
dpg.create_viewport(title=f"Test - {dpg.get_dearpygui_version()}", width=700, height=700)

with dpg.window() as wnd:
    dpg.set_primary_window(dpg.last_item(), True)

    dpg.add_combo(["one", "two", "three", "cincuenta", "seis"])
    dpg.add_combo(["one", "two", "three", "cincuenta", "seis"], fit_width=True)

dpg.setup_dearpygui()
dpg.show_viewport()
dpg.start_dearpygui()
dpg.destroy_context()
