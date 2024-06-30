#!/usr/local/bin/python3

from math import sin
import dearpygui.dearpygui as dpg

dpg.create_context()
dpg.create_viewport(title=f"Test - {dpg.get_dearpygui_version()}", width=700, height=700)

if not hasattr(dpg, "add_hline_series"):
    def add_hline_series(points):
        dpg.add_inf_line_series(points, horizontal=True)
    dpg.add_hline_series = add_hline_series
    
    def add_vline_series(points):
        dpg.add_inf_line_series(points, horizontal=False)
    dpg.add_vline_series = add_vline_series

with dpg.window() as wnd:
    dpg.set_primary_window(dpg.last_item(), True)

    x_data = [x/10 for x in range(0, 200)]
    y_data = [sin(x) for x in x_data]

    for i in range(10):
        y_data[len(y_data) * i // 10] = float("nan")

    with dpg.plot(label="Regular plot", width=-1, height=-1, tag="plot"):
        dpg.add_plot_legend(tag="plot-legend")
        x_axis = dpg.add_plot_axis(dpg.mvXAxis, label="x")
        with dpg.plot_axis(dpg.mvYAxis, label="y") as y_axis:
            dpg.add_line_series(x_data, y_data, label="Line series", skip_nan=True)
            # dpg.add_shade_series(x_data, y_data, label="Line series")
            # dpg.add_hline_series([0.3, 0.7])
            # dpg.add_vline_series([3, 7])


dpg.setup_dearpygui()
dpg.show_viewport()
# dpg.show_style_editor()
dpg.start_dearpygui()
dpg.destroy_context()
