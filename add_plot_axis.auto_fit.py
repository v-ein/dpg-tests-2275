#!/usr/local/bin/python3

from math import sin
import dearpygui.dearpygui as dpg

dpg.create_context()
dpg.create_viewport(title=f"Test - {dpg.get_dearpygui_version()}", width=700, height=700)

x_data = [x/10 - 10 for x in range(0, 200)]
y_data = [sin(x) for x in x_data] 

def update_data():
    time = dpg.get_frame_count() / 60
    coeff = sin(time) * 0.1
    cur_y_data = [y + x*coeff for x, y in zip(x_data, y_data)]
    dpg.configure_item("series1", y=cur_y_data)
    dpg.configure_item("series2", y=cur_y_data)

with dpg.item_handler_registry() as handlers:
    dpg.add_item_visible_handler(callback=update_data)

with dpg.window():
    dpg.set_primary_window(dpg.last_item(), True)
    dpg.bind_item_handler_registry(dpg.last_item(), handlers)


    with dpg.plot(label="Regular plot", width=-1, height=300):
        dpg.add_plot_legend()
        dpg.add_plot_axis(dpg.mvXAxis, label="x")
        with dpg.plot_axis(dpg.mvYAxis, label="y"):
            dpg.add_line_series(x_data, y_data, label="Line series", tag="series1") 

    with dpg.plot(label="auto_fit", width=-1, height=300):
        dpg.add_plot_legend()
        dpg.add_plot_axis(dpg.mvXAxis, label="x")
        with dpg.plot_axis(dpg.mvYAxis, label="y", auto_fit=True):
            dpg.add_line_series(x_data, y_data, label="Line series", tag="series2") 


dpg.setup_dearpygui()
dpg.show_viewport()
dpg.start_dearpygui()
dpg.destroy_context()
