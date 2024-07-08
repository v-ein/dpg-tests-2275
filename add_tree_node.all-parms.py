#!/usr/local/bin/python3

import dearpygui.dearpygui as dpg

dpg.create_context()
dpg.create_viewport(title=f"Test - {dpg.get_dearpygui_version()}", width=700, height=700)

with dpg.window():
    dpg.set_primary_window(dpg.last_item(), True)

    dpg.add_text("Hover sub-items to see how span properies affect the hit box.")

    with dpg.tree_node(label="Regular root", default_open=True):
        with dpg.tree_node(label="Regular sub-item", default_open=True):
            dpg.add_tree_node(label="Regular leaf", leaf=True)

    with dpg.tree_node(label="Regular root", default_open=True):
        with dpg.tree_node(label="span_full_width", span_full_width=True, default_open=True):
            dpg.add_tree_node(label="Regular leaf", leaf=True)

    with dpg.tree_node(label="Regular root", default_open=True):
        with dpg.tree_node(label="span_text_width", span_text_width=True, default_open=True):
            dpg.add_tree_node(label="Regular leaf", leaf=True)


dpg.setup_dearpygui()
dpg.show_viewport()
dpg.start_dearpygui()
dpg.destroy_context()
