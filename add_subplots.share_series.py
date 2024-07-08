#!/usr/local/bin/python3

from math import pi, sin
import dearpygui.dearpygui as dpg

dpg.create_context()
dpg.create_viewport(title=f"Test - {dpg.get_dearpygui_version()}", width=700, height=700)

with dpg.window():
    dpg.set_primary_window(dpg.last_item(), True)

    x_data = [x/2 for x in range(0, int(4*pi*2))]
    y_data = [3*sin(x) for x in x_data] 

    with dpg.subplots(2, 2, label="Non-shared", width=-1, height=300):
        for i in range(4):
            with dpg.plot(no_title=True):
                dpg.add_plot_legend()
                dpg.add_plot_axis(dpg.mvXAxis, label="", no_tick_labels=True)
                with dpg.plot_axis(dpg.mvYAxis, label="", no_tick_labels=True):
                    dpg.add_line_series(x_data, y_data, label=f"Line {i}")
                    dpg.add_stem_series(x_data, y_data, label=f"Stems {i}")

    with dpg.subplots(2, 2, label="Shared", width=-1, height=300, share_series=True):
        for i in range(4):
            with dpg.plot(no_title=True):
                dpg.add_plot_legend()
                dpg.add_plot_axis(dpg.mvXAxis, label="", no_tick_labels=True)
                with dpg.plot_axis(dpg.mvYAxis, label="", no_tick_labels=True):
                    dpg.add_line_series(x_data, y_data, label=f"Line {i}")
                    dpg.add_stem_series(x_data, y_data, label=f"Stems {i}")


dpg.setup_dearpygui()
dpg.show_viewport()
dpg.start_dearpygui()
dpg.destroy_context()
