#!/usr/local/bin/python3

import dearpygui.dearpygui as dpg

dpg.create_context()
dpg.create_viewport(title=f"Test - {dpg.get_dearpygui_version()}", width=700, height=700)

with dpg.window():
    dpg.set_primary_window(dpg.last_item(), True)

    values = [1, 1, 2, 3, 5]
    labels = ["Click", "on legend", "items", "...", "...."]

    with dpg.plot(label="Regular pie", width=-1, height=300, equal_aspects=True):
        dpg.add_plot_legend()
        dpg.add_plot_axis(dpg.mvXAxis, label="x")
        with dpg.plot_axis(dpg.mvYAxis, label="y"):
            dpg.add_pie_series(0.5, 0.5, 0.5, values, labels, normalize=True, format="%.0f")

    with dpg.plot(label="ignore_hidden", width=-1, height=300, equal_aspects=True):
        dpg.add_plot_legend()
        x_axis = dpg.add_plot_axis(dpg.mvXAxis, label="x")
        with dpg.plot_axis(dpg.mvYAxis, label="y") as y_axis:
            dpg.add_pie_series(0.5, 0.5, 0.5, values, labels, normalize=True, format="%.0f", ignore_hidden=True)


dpg.setup_dearpygui()
dpg.show_viewport()
dpg.start_dearpygui()
dpg.destroy_context()
