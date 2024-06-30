#!/usr/local/bin/python3

from math import sin
import dearpygui.dearpygui as dpg

dpg.create_context()
dpg.create_viewport(title=f"Test - {dpg.get_dearpygui_version()}", width=700, height=700)

with dpg.window() as wnd:
    dpg.set_primary_window(dpg.last_item(), True)

    x_data = [x/10 for x in range(0, 200)]
    y_data = [sin(x) for x in x_data]

    with dpg.plot(label="Regular plot", width=-1, height=-1, tag="plot"):
        dpg.add_plot_axis(dpg.mvXAxis)
        with dpg.plot_axis(dpg.mvYAxis, label="y"):
            dpg.add_line_series(x_data, y_data, label="Line series")

        dpg.add_drag_point(label="non-clamped", default_value=(5, 0.5), offset=(0, 20), clamped=False)
        dpg.add_drag_point(label="no_cursor", default_value=(15, 0.5), no_cursor=True)
        dpg.add_drag_point(label="no_inputs", default_value=(15, -0.5), no_inputs=True)

        dpg.add_drag_point(label="no_fit", default_value=(-2, -2), no_fit=True)
        dpg.add_drag_point(label="fit", default_value=(23, 2), no_fit=False)

dpg.setup_dearpygui()
dpg.show_viewport()
dpg.start_dearpygui()
dpg.destroy_context()
