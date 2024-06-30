#!/usr/local/bin/python3

from math import sin
import dearpygui.dearpygui as dpg

dpg.create_context()
dpg.create_viewport(title=f"Test - {dpg.get_dearpygui_version()}", width=700, height=700)

x_data = [x/10 for x in range(0, 200)]
y_data = [sin(x) for x in x_data]

def create_plot(no_fit=False):
    with dpg.plot(label="y=f(x)", height=300, width=-1) as plot:
        dpg.add_plot_legend()
        dpg.add_plot_axis(dpg.mvXAxis, label="x")
        with dpg.plot_axis(dpg.mvYAxis, label="y"):
            dpg.add_line_series(x_data, y_data, label="Line series")
            with dpg.custom_series([-10, 30], [-3, 3], 2, label="Custom Series", no_fit=no_fit):
                pass


with dpg.window():
    dpg.set_primary_window(dpg.last_item(), True)
    create_plot(no_fit=False)
    create_plot(no_fit=True)

dpg.setup_dearpygui()
dpg.show_viewport()
dpg.start_dearpygui()
dpg.destroy_context()
