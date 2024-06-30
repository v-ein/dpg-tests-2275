#!/usr/local/bin/python3

from math import sin
import random
import dearpygui.dearpygui as dpg

dpg.create_context()
dpg.create_viewport(title="Test", width=700, height=700)

with dpg.window() as wnd:
    dpg.set_primary_window(dpg.last_item(), True)

    x_data = [x/10 for x in range(0, 200)]
    y_data = [10*sin(x) for x in x_data]

    fit_args = {
        "no_initial_fit": True
    }
    fit_args = {}

    with dpg.plot(label="Regular plot", width=-1, height=-1, tag="plot"):
        dpg.add_plot_legend(tag="plot-legend")
        x_axis = dpg.add_plot_axis(dpg.mvXAxis, label="x", **fit_args)
        with dpg.plot_axis(dpg.mvYAxis, label="y", **fit_args) as y_axis:
            dpg.add_digital_series(x_data, y_data)

dpg.setup_dearpygui()
dpg.show_viewport()
# dpg.show_style_editor()
dpg.start_dearpygui()
dpg.destroy_context()
