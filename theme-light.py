#!/usr/local/bin/python3

from math import sin
import dearpygui.dearpygui as dpg
from dearpygui_ext.themes import create_theme_imgui_light, create_theme_imgui_dark
import dearpygui_ext.themes

dpg.create_context()
dpg.create_viewport(title=f"Test - {dpg.get_dearpygui_version()}", width=700, height=900)

print(f"dearpygui_ext path: {dearpygui_ext.themes.__file__}")

dpg.bind_theme(create_theme_imgui_light())

with dpg.window():
    dpg.set_primary_window(dpg.last_item(), True)

    x_data = [x/10 - 8 for x in range(0, 200)]
    y_data = [sin(x) for x in x_data] 

    with dpg.plot(label="Global light theme", width=-1, height=250):
        dpg.add_plot_axis(dpg.mvXAxis, label="This is a regular plot")
        with dpg.plot_axis(dpg.mvYAxis, label="y"):
            dpg.add_shade_series(x_data, y_data, label="Line series") 

    with dpg.plot(label="Light theme bound to plot", width=-1, height=250):
        dpg.bind_item_theme(dpg.last_item(), create_theme_imgui_light())
        dpg.add_plot_axis(dpg.mvXAxis, label="This is a regular plot")
        with dpg.plot_axis(dpg.mvYAxis, label="y"):
            dpg.add_shade_series(x_data, y_data, label="Line series") 

    with dpg.plot(label="Dark theme bound to plot", width=-1, height=250):
        dpg.bind_item_theme(dpg.last_item(), create_theme_imgui_dark())
        dpg.add_plot_axis(dpg.mvXAxis, label="This is a regular plot")
        with dpg.plot_axis(dpg.mvYAxis, label="y"):
            dpg.add_shade_series(x_data, y_data, label="Line series") 


dpg.setup_dearpygui()
dpg.show_viewport()
dpg.start_dearpygui()
dpg.destroy_context()
