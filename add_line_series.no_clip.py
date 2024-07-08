#!/usr/local/bin/python3

from math import sin
import dearpygui.dearpygui as dpg

dpg.create_context()
dpg.create_viewport(title=f"Test - {dpg.get_dearpygui_version()}", width=700, height=700)

with dpg.window():
    dpg.set_primary_window(dpg.last_item(), True)

    x_data = [x/10 for x in range(0, 200)]
    x_data2 = [-x for x in x_data]
    y_data = [10*sin(x) for x in x_data]

    y_data2 = [-y for y in y_data]
    
    with dpg.theme() as marker_theme:
        with dpg.theme_component():
            dpg.add_theme_style(dpg.mvPlotStyleVar_Marker, dpg.mvPlotMarker_Diamond, category=dpg.mvThemeCat_Plots)

    with dpg.plot(width=-1, height=-1, tag="plot"):
        dpg.add_plot_legend(tag="plot-legend")
        x_axis = dpg.add_plot_axis(dpg.mvXAxis, label="x")
        with dpg.plot_axis(dpg.mvYAxis, label="y") as y_axis:
            dpg.add_line_series(x_data, y_data, label="regular")
            dpg.bind_item_theme(dpg.last_item(), marker_theme)
            dpg.add_line_series(x_data2, y_data2, label="no_clip", no_clip=True)
            dpg.bind_item_theme(dpg.last_item(), marker_theme)


dpg.setup_dearpygui()
dpg.show_viewport()
dpg.start_dearpygui()
dpg.destroy_context()
