#!/usr/local/bin/python3

from math import sin
import dearpygui.dearpygui as dpg

dpg.create_context()
dpg.create_viewport(title=f"Test - {dpg.get_dearpygui_version()}", width=700, height=900)

with dpg.window():
    dpg.set_primary_window(dpg.last_item(), True)

    x_data = [x/10 for x in range(0, 64)]
    y_data = [sin(x) for x in x_data] 

    with dpg.plot(label="Regular plot", width=-1, height=300):
        dpg.add_plot_axis(dpg.mvXAxis, label="x", tag="x-axis1")
        with dpg.plot_axis(dpg.mvYAxis, label="y", tag="y-axis1"):
            dpg.add_line_series(x_data, y_data, label="Line series") 

    with dpg.plot(label="pan_stretch on X axis", width=-1, height=300):
        dpg.add_plot_axis(dpg.mvXAxis, label="x", tag="x-axis2", pan_stretch=True)
        with dpg.plot_axis(dpg.mvYAxis, label="y", tag="y-axis2"):
            dpg.add_line_series(x_data, y_data, label="Line series") 
        dpg.set_axis_limits_constraints("x-axis1", -2, 5)
        dpg.set_axis_limits_constraints("x-axis2", -2, 5)


dpg.setup_dearpygui()
dpg.show_viewport()
dpg.start_dearpygui()
dpg.destroy_context()
