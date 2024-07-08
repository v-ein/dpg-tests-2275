#!/usr/local/bin/python3

from math import pi, sin
import dearpygui.dearpygui as dpg

dpg.create_context()
dpg.create_viewport(title=f"Test - {dpg.get_dearpygui_version()}", width=700, height=900)

with dpg.window():
    dpg.set_primary_window(dpg.last_item(), True)

    x_data = [x/2 for x in range(6, int(4*pi*2))]
    y_data = [3*sin(x) for x in x_data] 

    with dpg.plot(width=-1, height=300):
        dpg.add_plot_legend()
        dpg.add_plot_axis(dpg.mvXAxis, label="x")
        with dpg.plot_axis(dpg.mvYAxis, label="y"):
            dpg.add_scatter_series(x_data, y_data, label="Regular") 
            # It's important to use floating-point numbers even if they are actually integer
            # dpg.add_text_point(1.0, 2.0, label="Lorem ipsum", offset=(50, 50))
            # dpg.add_text_point(x_data[0], y_data[0], label="Offset from the very first point", offset=(20, 20))
            dpg.add_text_point(x_data[0], y_data[0], label="No offset")
            dpg.add_text_point(x_data[0], y_data[0], label="Offset", offset=(20, 20))


dpg.setup_dearpygui()
dpg.show_viewport()
dpg.start_dearpygui()
dpg.destroy_context()
