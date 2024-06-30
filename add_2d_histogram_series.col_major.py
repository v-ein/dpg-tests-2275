#!/usr/local/bin/python3

from math import sin
import random
import dearpygui.dearpygui as dpg

dpg.create_context()
dpg.create_viewport(title=f"Test - {dpg.get_dearpygui_version()}", width=500, height=750)
 
with dpg.window() as wnd:
    dpg.set_primary_window(dpg.last_item(), True)

    x_data = [x/10 for x in range(0, 200)]
    y_data = [sin(x) for x in x_data]

    count_2d_histogram = 50000
    xybin_2d_histogram = [100, 100]

    x_dist = [random.gauss(1, 2) for _ in range(count_2d_histogram)]
    y_dist = [random.uniform(1, 2) for _ in range(count_2d_histogram)]

    fit_args = {
        "no_initial_fit": True
    }
    fit_args = {}

    with dpg.plot(label="Regular plot", width=-1, height=350, tag="plot"):
        x_axis = dpg.add_plot_axis(dpg.mvXAxis, label="x", **fit_args)
        with dpg.plot_axis(dpg.mvYAxis, label="y", **fit_args) as y_axis:
            dpg.add_2d_histogram_series(x_dist, y_dist, tag="histogram_2d_series",
                                        label="histogram", xbins=xybin_2d_histogram[0], ybins=xybin_2d_histogram[1],
                                        xmax_range=6, xmin_range=-6, ymin_range=0, ymax_range=0
            )

    with dpg.plot(label="Regular plot", width=-1, height=350, tag="plot2"):
        x_axis = dpg.add_plot_axis(dpg.mvXAxis, label="x", **fit_args)
        with dpg.plot_axis(dpg.mvYAxis, label="y", **fit_args) as y_axis:
            dpg.add_2d_histogram_series(x_dist, y_dist, tag="histogram_2d_series2", col_major=True,
                                        label="histogram", xbins=xybin_2d_histogram[0], ybins=xybin_2d_histogram[1],
                                        xmax_range=6, xmin_range=-6, ymin_range=0, ymax_range=0
            )

dpg.setup_dearpygui()
dpg.show_viewport()
# dpg.show_style_editor()
dpg.start_dearpygui()
dpg.destroy_context()
