#!/usr/local/bin/python3

import dearpygui.dearpygui as dpg

dpg.create_context()
dpg.create_viewport(title=f"Test - {dpg.get_dearpygui_version()}", width=700, height=700)

with dpg.window():
    dpg.set_primary_window(dpg.last_item(), True)

    with dpg.table(
        no_keep_columns_visible=True,
        hideable=True,
        policy=dpg.mvTable_SizingFixedFit) as table:

        dpg.add_table_column(label="no_header_label", no_header_label=True)
        dpg.add_table_column(label="angled_header", angled_header=True)
        dpg.add_table_column(label="Hidden column", show=False)
        dpg.add_table_column(label="Regular column")
        with dpg.table_row():
            dpg.add_button(label="Lorem")
            dpg.add_button(label="ipsum")
            dpg.add_button(label="dolor")
            dpg.add_button(label="sit")


dpg.setup_dearpygui()
dpg.show_viewport()
dpg.start_dearpygui()
dpg.destroy_context()
