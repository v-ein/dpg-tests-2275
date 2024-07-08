#!/usr/local/bin/python3

from math import pi, sin
import dearpygui.dearpygui as dpg

dpg.create_context()
dpg.create_viewport(title=f"Test - {dpg.get_dearpygui_version()}", width=700, height=900)

with dpg.window():
    dpg.set_primary_window(dpg.last_item(), True)

    x_data = [x/2 - 2*pi for x in range(0, int(4*pi*2))]
    y_data = [3*sin(x) for x in x_data] 

    with dpg.plot(width=-1, height=300):
        dpg.add_plot_legend()
        dpg.add_plot_axis(dpg.mvXAxis, label="x")
        with dpg.plot_axis(dpg.mvYAxis, label="y"):
            dpg.add_stair_series(x_data, y_data, label="Regular") 
            dpg.add_stair_series(x_data, y_data, label="pre_step", pre_step=True) 

    with dpg.plot(width=-1, height=300):
        dpg.add_plot_legend()
        dpg.add_plot_axis(dpg.mvXAxis, label="x")
        with dpg.plot_axis(dpg.mvYAxis, label="y"):
            dpg.add_stair_series(x_data, y_data, label="shaded", shaded=True) 


dpg.setup_dearpygui()
dpg.show_viewport()
dpg.start_dearpygui()
dpg.destroy_context()
