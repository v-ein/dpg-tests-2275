#!/usr/local/bin/python3

from math import pi, sin
import dearpygui.dearpygui as dpg

dpg.create_context()
dpg.create_viewport(title=f"Test - {dpg.get_dearpygui_version()}", width=500, height=750)
 
with dpg.window() as wnd:
    dpg.set_primary_window(dpg.last_item(), True)

    rows = 5
    cols = 10
    data = [ 0.5*x/cols + sin(y/(rows-1)*pi) for y in range(rows) for x in range(cols) ]

    with dpg.plot(label="Regular plot", width=-1, height=350, tag="plot"):
        x_axis = dpg.add_plot_axis(dpg.mvXAxis, label="x")
        with dpg.plot_axis(dpg.mvYAxis, label="y") as y_axis:
            dpg.add_heat_series(data, rows, cols)

    with dpg.plot(label="Regular plot", width=-1, height=350, tag="plot2"):
        x_axis = dpg.add_plot_axis(dpg.mvXAxis, label="x")
        with dpg.plot_axis(dpg.mvYAxis, label="y") as y_axis:
            dpg.add_heat_series(data, rows, cols, col_major=True)

dpg.setup_dearpygui()
dpg.show_viewport()
dpg.start_dearpygui()
dpg.destroy_context()
