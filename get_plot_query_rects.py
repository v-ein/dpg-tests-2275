#!/usr/local/bin/python3

from math import sin
import dearpygui.dearpygui as dpg

dpg.create_context()
dpg.create_viewport(title="Test", width=700, height=700)

with dpg.window() as wnd:
    dpg.set_primary_window(dpg.last_item(), True)

    x_data = [x/10 for x in range(0, 200)]
    y_data = [sin(x) for x in x_data]

    dpg.add_button(label="Print query rects", callback=lambda: print(dpg.get_plot_query_rects("plot")))

    with dpg.plot(label="Regular plot", tag="plot", width=-1, height=-1):

        dpg.add_plot_legend(tag="plot-legend")
        x_axis = dpg.add_plot_axis(dpg.mvXAxis, label="x")
        with dpg.plot_axis(dpg.mvYAxis, label="y") as y_axis:
            dpg.add_line_series(x_data, y_data, label="Line series")

dpg.setup_dearpygui()
dpg.show_viewport()
dpg.start_dearpygui()
dpg.destroy_context()
