#!/usr/local/bin/python3

from math import sin
import dearpygui.dearpygui as dpg

dpg.create_context()
dpg.create_viewport(title=f"Test - {dpg.get_dearpygui_version()}", width=700, height=900)

with dpg.window():
    dpg.set_primary_window(dpg.last_item(), True)

    x_data = [x/10 for x in range(0, 64)]
    y_data = [sin(x) for x in x_data] 

    dpg.add_text("Move plots down so that only a half (or, better, a third) of the sine wave is visible.")
    dpg.add_text("Click Fit X and see if range_fit works.")

    with dpg.group(horizontal=True):
        dpg.add_button(label="Fit X", callback=lambda: (dpg.fit_axis_data("x-axis1"), dpg.fit_axis_data("x-axis2")))
        dpg.add_button(label="Fit Y", callback=lambda: (dpg.fit_axis_data("y-axis1"), dpg.fit_axis_data("y-axis2")))

    with dpg.plot(label="Regular plot", width=-1, height=300):
        dpg.add_plot_axis(dpg.mvXAxis, label="x", tag="x-axis1")
        with dpg.plot_axis(dpg.mvYAxis, label="y", tag="y-axis1"):
            dpg.add_line_series(x_data, y_data, label="Line series") 

    with dpg.plot(label="range_fit on X axis", width=-1, height=300):
        dpg.add_plot_axis(dpg.mvXAxis, label="x", tag="x-axis2", range_fit=True)
        with dpg.plot_axis(dpg.mvYAxis, label="y", tag="y-axis2"):
            dpg.add_line_series(x_data, y_data, label="Line series") 


dpg.setup_dearpygui()
dpg.show_viewport()
dpg.start_dearpygui()
dpg.destroy_context()
