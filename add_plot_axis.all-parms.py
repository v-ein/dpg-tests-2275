#!/usr/local/bin/python3

from math import sin
import dearpygui.dearpygui as dpg

dpg.create_context()
dpg.create_viewport(title=f"Test - {dpg.get_dearpygui_version()}", width=700, height=900)

with dpg.window():
    dpg.set_primary_window(dpg.last_item(), True)

    x_data = [x/10 - 8 for x in range(0, 200)]
    y_data = [sin(x) for x in x_data] 

    with dpg.plot(width=-1, height=280):
        dpg.add_plot_axis(dpg.mvXAxis, label="This is a regular plot")
        with dpg.plot_axis(dpg.mvYAxis, label="y"):
            dpg.add_shade_series(x_data, y_data, label="Line series") 

    with dpg.plot(width=-1, height=280):
        dpg.add_plot_axis(dpg.mvXAxis, label="invert + no_highlight", invert=True, no_highlight=True)
        with dpg.plot_axis(dpg.mvYAxis, label="foreground_grid + no_initial_fit", foreground_grid=True, no_initial_fit=True):
            dpg.add_shade_series(x_data, y_data, label="Line series") 

    with dpg.plot(width=-1, height=280):
        dpg.add_plot_axis(dpg.mvXAxis, label="no_menus + opposite + scale=log", no_menus=True, opposite=True, scale=dpg.mvPlotScale_SymLog)
        with dpg.plot_axis(dpg.mvYAxis, label="no_side_switch + tick_format", no_side_switch=True, tick_format="%.2f"):
            dpg.add_shade_series(x_data, y_data, label="Line series") 


dpg.setup_dearpygui()
dpg.show_viewport()
dpg.start_dearpygui()
dpg.destroy_context()
