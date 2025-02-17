#!/usr/local/bin/python3

from math import sin
import time
import warnings
import dearpygui.dearpygui as dpg

warnings.simplefilter('always', DeprecationWarning) 

dpg.create_context()
dpg.create_viewport(title=f"Test - {dpg.get_dearpygui_version()}", width=700, height=700)

with dpg.window(id="window") as wnd:
    dpg.set_primary_window(dpg.last_item(), True)

    now = time.time()

    x_data = [now + x/10 for x in range(0, 200)]
    y_data = [1 + sin(x) for x in x_data]

    with dpg.plot(label="Regular plot", width=-1, height=300):
        dpg.add_plot_axis(dpg.mvXAxis)
        with dpg.plot_axis(dpg.mvYAxis):
            dpg.add_line_series(x_data, y_data, label="Line series")

    with dpg.plot(label="Deprecated", width=-1, height=-1, tag="plot"):
        dpg.add_plot_axis(dpg.mvXAxis, label="time scale", time=True)
        with dpg.plot_axis(dpg.mvYAxis, label="log scale", log_scale=True):
            dpg.add_line_series(x_data, y_data, label="Line series")

dpg.setup_dearpygui()
dpg.show_viewport()
# dpg.show_style_editor()
dpg.start_dearpygui()
dpg.destroy_context()
