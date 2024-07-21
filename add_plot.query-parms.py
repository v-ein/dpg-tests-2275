#!/usr/local/bin/python3

from math import sin
import dearpygui.dearpygui as dpg

dpg.create_context()
dpg.create_viewport(title=f"Test - {dpg.get_dearpygui_version()}", width=700, height=700)

with dpg.window():
    dpg.set_primary_window(dpg.last_item(), True)

    x_data = [x/10 for x in range(0, 200)]
    y_data = [sin(x) for x in x_data]

    with dpg.group(horizontal=True):
        with dpg.plot(label="Regular plot", width=330, height=300):
            dpg.add_plot_axis(dpg.mvXAxis, no_tick_labels=True)
            with dpg.plot_axis(dpg.mvYAxis, no_tick_labels=True):
                dpg.add_line_series(x_data, y_data)

        with dpg.plot(label="query=True", width=330, height=300, query=True):
            dpg.add_plot_axis(dpg.mvXAxis, no_tick_labels=True)
            with dpg.plot_axis(dpg.mvYAxis, no_tick_labels=True):
                dpg.add_line_series(x_data, y_data)

    with dpg.group(horizontal=True):
        with dpg.plot(label="min_query_rects=2, query_color=red", width=330, height=300, query=True, min_query_rects=2, max_query_rects=9999, query_color=(255, 0, 0, 255)):
            dpg.add_plot_axis(dpg.mvXAxis, no_tick_labels=True)
            with dpg.plot_axis(dpg.mvYAxis, no_tick_labels=True):
                dpg.add_line_series(x_data, y_data)

        with dpg.plot(label="max_query_rects=3", width=330, height=300, query=True, min_query_rects=0, max_query_rects=3):
            dpg.add_plot_axis(dpg.mvXAxis, no_tick_labels=True)
            with dpg.plot_axis(dpg.mvYAxis, no_tick_labels=True):
                dpg.add_line_series(x_data, y_data)


dpg.setup_dearpygui()
dpg.show_viewport()
dpg.start_dearpygui()
dpg.destroy_context()
