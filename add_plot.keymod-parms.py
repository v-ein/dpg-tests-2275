#!/usr/local/bin/python3

import dearpygui.dearpygui as dpg

dpg.create_context()
dpg.create_viewport(title=f"Test - {dpg.get_dearpygui_version()}", width=700, height=700)

with dpg.window():
    dpg.set_primary_window(dpg.last_item(), True)

    values = [1, 1, 2, 3, 5]
    labels = ["A", "B", "C", "D", "E"]

    with dpg.plot(label="Regular plot", width=350, height=300, equal_aspects=True):
        dpg.add_plot_legend()
        dpg.add_plot_axis(dpg.mvXAxis, label="x")
        with dpg.plot_axis(dpg.mvYAxis, label="y"):
            dpg.add_pie_series(0.5, 0.5, 0.5, values, labels, normalize=True, format="%.0f")

    with dpg.plot(label="Shift disables input, Alt enables zoom", width=350, height=300, override_mod=dpg.mvKey_ModShift, zoom_mod=dpg.mvKey_ModAlt, zoom_rate=-0.02):
        dpg.add_plot_legend()
        x_axis = dpg.add_plot_axis(dpg.mvXAxis, label="x")
        with dpg.plot_axis(dpg.mvYAxis, label="y") as y_axis:
            dpg.add_pie_series(0.5, 0.5, 0.5, values, labels, normalize=True, format="%.0f")


dpg.setup_dearpygui()
dpg.show_viewport()
dpg.start_dearpygui()
dpg.destroy_context()
