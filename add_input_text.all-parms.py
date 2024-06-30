#!/usr/local/bin/python3

from math import atan
import dearpygui.dearpygui as dpg

dpg.create_context()
dpg.create_viewport(title=f"Test - {dpg.get_dearpygui_version()}", width=700, height=700)

with dpg.window():
    dpg.set_primary_window(dpg.last_item(), True)

    dpg.add_input_text(default_value="Lorem ipsum", label="regular")
    dpg.add_input_text(default_value="Lorem ipsum", label="always_overwrite", always_overwrite=True)
    dpg.add_input_text(default_value="Lorem ipsum", label="auto_select_all", auto_select_all=True)
    dpg.add_input_text(default_value="Lorem ipsum", label="ctrl_enter_for_new_line", ctrl_enter_for_new_line=True, multiline=True)
    dpg.add_input_text(default_value="Lorem ipsum", label="escape_clears_all", escape_clears_all=True)
    dpg.add_input_text(default_value="Lorem ipsum", label="no_horizontal_scroll", no_horizontal_scroll=True)
    dpg.add_input_text(default_value="Lorem ipsum", label="no_undo_redo", no_undo_redo=True)

dpg.setup_dearpygui()
dpg.show_viewport()
dpg.start_dearpygui()
dpg.destroy_context()
