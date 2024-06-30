#!/usr/local/bin/python3

from math import sin
import dearpygui.dearpygui as dpg

dpg.create_context()
dpg.create_viewport(title=f"Test - {dpg.get_dearpygui_version()}", width=700, height=700)

with dpg.window() as wnd:
    dpg.set_primary_window(dpg.last_item(), True)

    x_data = [x/10 for x in range(0, 200)]
    y_data = [sin(x) for x in x_data]

    # Note: it's not clear how to test `delayed`, and therefore we do not test this parm.

    with dpg.plot(label="Regular plot", width=-1, height=-1, tag="plot"):
        dpg.add_plot_axis(dpg.mvXAxis)
        with dpg.plot_axis(dpg.mvYAxis, label="y"):
            dpg.add_line_series(x_data, y_data, label="Line series")
        dpg.add_drag_line(default_value=5, vertical=True)
        dpg.add_drag_line(label="no_cursor", default_value=0.5, vertical=False, no_cursor=True)
        dpg.add_drag_line(label="no_inputs", default_value=-0.5, vertical=False, no_inputs=True)

        dpg.add_drag_line(label="fit", default_value=2, vertical=False)
        dpg.add_drag_line(label="no_fit", default_value=-2, vertical=False, no_fit=True)

        dpg.add_drag_line(label="fit", default_value=-2, vertical=True)
        dpg.add_drag_line(label="no_fit", default_value=22, vertical=True, no_fit=True)

dpg.setup_dearpygui()
dpg.show_viewport()
dpg.start_dearpygui()
dpg.destroy_context()
