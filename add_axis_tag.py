#!/usr/local/bin/python3

from math import sin
import dearpygui.dearpygui as dpg

dpg.create_context()
dpg.create_viewport(title=f"Test - {dpg.get_dearpygui_version()}", width=500, height=750)

with dpg.window() as wnd:
    dpg.set_primary_window(dpg.last_item(), True)

    x_data = [x/10 for x in range(0, 200)]
    y_data = [sin(x) for x in x_data]

    with dpg.plot(label="Regular plot", width=-1, height=-1, tag="plot"):
        dpg.add_plot_legend(tag="plot-legend")
        with dpg.plot_axis(dpg.mvXAxis, label="") as x_axis:
            dpg.add_axis_tag(default_value=5, color=(255, 0, 0, 255), label="Owned by X")
        with dpg.plot_axis(dpg.mvYAxis, label="y", no_label=True) as y_axis:
            dpg.add_axis_tag(default_value=0, color=(255, 0, 0, 255), label="Owned by Y")
            dpg.add_axis_tag(default_value=0.25, color=(255, 255, 0, 255))
            dpg.add_axis_tag(default_value=0.5, color=(0, 255, 255, 255), label="Tag: 42")
            dpg.add_axis_tag(default_value=-0.5, color=(0, 255, 0, 255), auto_rounding=True)
            dpg.add_shade_series(x_data, y_data, label="Line series")
        with dpg.plot_axis(dpg.mvYAxis2, label="y2", no_label=True) as y_axis:
            dpg.add_axis_tag(default_value=0, color=(255, 255, 0, 255), label="Owned by Y2")
            dpg.add_shade_series(x_data[:-10], y_data[10:])

dpg.setup_dearpygui()
dpg.show_viewport()
dpg.start_dearpygui()
dpg.destroy_context()
