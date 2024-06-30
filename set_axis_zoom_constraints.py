#!/usr/local/bin/python3

from math import sin
import math
import warnings
import dearpygui.dearpygui as dpg

print(dpg.__file__)
warnings.simplefilter('always', DeprecationWarning)

dpg.create_context()
dpg.create_viewport(title="Test", width=700, height=750)

with dpg.window() as wnd:
    dpg.set_primary_window(dpg.last_item(), True)

    x_data = [x/10 for x in range(0, 200)]
    y_data = [1 + sin(x) for x in x_data]

    with dpg.plot(label="Regular plot", width=-1, height=-1, tag="plot"):
        dpg.add_plot_legend(tag="plot-legend")
        x_axis = dpg.add_plot_axis(dpg.mvXAxis, label="")
        with dpg.plot_axis(dpg.mvYAxis, label="y") as y_axis:
            dpg.add_line_series(x_data, y_data, label="Line series")
        # dpg.set_axis_limits_constraints(y_axis, -1, 5)
        # dpg.set_axis_limits_constraints(x_axis, -1, 5)
        # dpg.set_axis_limits_constraints(x_axis, -1, math.inf)
        dpg.set_axis_zoom_constraints(y_axis, 1, 5)
        dpg.set_axis_zoom_constraints(x_axis, 3, 10)

dpg.setup_dearpygui()
dpg.show_viewport()
# dpg.show_style_editor()
dpg.start_dearpygui()
dpg.destroy_context()
