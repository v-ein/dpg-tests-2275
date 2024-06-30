#!/usr/local/bin/python3

import warnings
import dearpygui.dearpygui as dpg

print(dpg.__file__)
warnings.simplefilter('always', DeprecationWarning)

dpg.create_context()
dpg.create_viewport(title="Test", width=700, height=750)

with dpg.window(width=300, height=300) as wnd:
    dpg.add_text("Lorem")
    with dpg.child_window(
            auto_resize_x=True, auto_resize_y=True,
            resizable_x=True, resizable_y=True, frame_style=True):

        dpg.add_button(label="Autosized child")
        dpg.add_text("dolor sit")

    with dpg.child_window(
            width=200, height=200,
            auto_resize_x=not True, auto_resize_y=not True,
            resizable_x=True, resizable_y=True, frame_style=True):

        dpg.add_button(label="ipsum")
        dpg.add_text("dolor sit")

dpg.setup_dearpygui()
dpg.show_viewport()
# dpg.show_style_editor()
dpg.start_dearpygui()
dpg.destroy_context()
