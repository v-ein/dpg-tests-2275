#!/usr/local/bin/python3

from math import pi, sin
import dearpygui.dearpygui as dpg

dpg.create_context()
dpg.create_viewport(title=f"Test - {dpg.get_dearpygui_version()}", width=700, height=700)

with dpg.window():
    dpg.set_primary_window(dpg.last_item(), True)

    x_data = [x/10 - 2*pi for x in range(0, int(4*pi*10))]
    y_data = [3*sin(x) for x in x_data] 

    with dpg.group(horizontal=True):
        with dpg.plot(label="Regular plot", width=300, height=300):
            dpg.add_plot_legend()
            dpg.add_plot_axis(dpg.mvXAxis, label="x")
            with dpg.plot_axis(dpg.mvYAxis, label="y"):
                dpg.add_shade_series(x_data, y_data, label="Shade series") 
            with dpg.plot_axis(dpg.mvYAxis2, label="y2"):
                dpg.add_line_series(y_data, x_data, label="Line series") 

        with dpg.plot(label="no_buttons + sort", width=300, height=300):
            dpg.add_plot_legend(no_buttons=True, sort=True)
            dpg.add_plot_axis(dpg.mvXAxis, label="x")
            with dpg.plot_axis(dpg.mvYAxis, label="y"):
                dpg.add_shade_series(x_data, y_data, label="Shade series") 
            with dpg.plot_axis(dpg.mvYAxis2, label="y2"):
                dpg.add_line_series(y_data, x_data, label="Line series") 

    with dpg.group(horizontal=True):
        with dpg.plot(label="no_highlight_axis + no_menus", width=300, height=300):
            dpg.add_plot_legend(no_highlight_axis=True, no_menus=True)
            dpg.add_plot_axis(dpg.mvXAxis, label="x")
            with dpg.plot_axis(dpg.mvYAxis, label="y"):
                dpg.add_shade_series(x_data, y_data, label="Shade series") 
            with dpg.plot_axis(dpg.mvYAxis2, label="y2"):
                dpg.add_line_series(y_data, x_data, label="Line series") 

        with dpg.plot(label="no_highlight_item", width=300, height=300):
            dpg.add_plot_legend(no_highlight_item=True)
            dpg.add_plot_axis(dpg.mvXAxis, label="x")
            with dpg.plot_axis(dpg.mvYAxis, label="y"):
                dpg.add_shade_series(x_data, y_data, label="Shade series") 
            with dpg.plot_axis(dpg.mvYAxis2, label="y2"):
                dpg.add_line_series(y_data, x_data, label="Line series") 


dpg.setup_dearpygui()
dpg.show_viewport()
dpg.start_dearpygui()
dpg.destroy_context()
