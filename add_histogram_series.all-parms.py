#!/usr/local/bin/python3

from math import atan
import dearpygui.dearpygui as dpg

dpg.create_context()
dpg.create_viewport(title=f"Test - {dpg.get_dearpygui_version()}", width=700, height=700)

with dpg.window():
    dpg.set_primary_window(dpg.last_item(), True)

    count = 20000
    x_dist = [ (atan(x/count*4-2)) for x in range(0, count)]

    def create_plot(label: str, cumulative: bool = False, horizontal: bool = False) -> None:
        with dpg.plot(width=300, height=300):
            dpg.add_plot_legend()
            dpg.add_plot_axis(dpg.mvXAxis)
            with dpg.plot_axis(dpg.mvYAxis):
                dpg.add_histogram_series(x_dist, label=label, bins=20, cumulative=cumulative, horizontal=horizontal)

    with dpg.group(horizontal=True):
        create_plot("regular")
        create_plot("horizontal", horizontal=True)

    with dpg.group(horizontal=True):
        create_plot("cumulative", cumulative=True)
        create_plot("cumulative horizontal", cumulative=True, horizontal=True)

dpg.setup_dearpygui()
dpg.show_viewport()
dpg.start_dearpygui()
dpg.destroy_context()
