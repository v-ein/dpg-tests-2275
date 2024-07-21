#!/usr/local/bin/python3

import dearpygui.dearpygui as dpg

dpg.create_context()
dpg.create_viewport(title=f"Test - {dpg.get_dearpygui_version()}", width=500, height=900)

with dpg.window():
    dpg.set_primary_window(dpg.last_item(), True)

    with dpg.group(horizontal=True):
        dpg.add_colormap_scale(label="Colormap Slider 1", mirror=False, reverse_dir=True)
        dpg.add_colormap_scale(label="Colormap Slider 2", mirror=True)

    dpg.add_colormap_scale(label="Level", format="%.3f m")

dpg.setup_dearpygui()
dpg.show_viewport()
# dpg.show_style_editor()
dpg.start_dearpygui()
dpg.destroy_context()
