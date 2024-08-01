#!/usr/local/bin/python3

from math import pi, sin
from typing import List
import dearpygui.dearpygui as dpg

dpg.create_context()
dpg.create_viewport(title=f"Test - {dpg.get_dearpygui_version()}", width=700, height=700)

def create_bar_group(
        total_bars: int = 30,
        group_size: int = 3,
        labels: List[str] = [f"Data {i+1}" for i in range(3)],
        stacked: bool = False,
        shift: int = 0):

    bar_data = [sin(x/total_bars*pi) for x in range(total_bars)]
    print(f"Creating bar group series:\n{total_bars=}, {group_size=}, {labels=}")

    if dpg.does_item_exist("plot"):
        dpg.delete_item("plot")
    with dpg.plot(label="Regular plot", width=-1, height=500, parent="main-wnd", tag="plot"):
        dpg.add_plot_legend()
        dpg.add_plot_axis(dpg.mvXAxis, label="x")
        with dpg.plot_axis(dpg.mvYAxis, label="y"):
            dpg.add_bar_group_series(bar_data, labels, group_size, label="histogram", stacked=stacked, shift=shift)


with dpg.window(tag="main-wnd"):
    dpg.set_primary_window(dpg.last_item(), True)
    with dpg.group(horizontal=True, horizontal_spacing=20):
        dpg.add_input_int(label="bars", width=80, default_value=30, tag="bars-count")
        dpg.add_input_int(label="per group", width=80, default_value=3, tag="group-size")
        dpg.add_input_int(label="labels", width=80, default_value=3, tag="labels-count")
        dpg.add_checkbox(label="Stacked", tag="stacked")

        dpg.add_button(label="Create", callback=lambda: create_bar_group(
            dpg.get_value("bars-count"), dpg.get_value("group-size"),
            [f"Data {i+1}" for i in range(dpg.get_value("labels-count"))],
            dpg.get_value("stacked")
        ))

    dpg.add_spacer(height=12)
    dpg.add_text("Predefined tests (must all fail, see errors in the console):")
    with dpg.group(horizontal=True):
        dpg.add_button(label="Bad group size", callback=lambda: create_bar_group(group_size=4))
        dpg.add_button(label="Zero group size", callback=lambda: create_bar_group(group_size=0))
        # No, this is a valid situation
        # dpg.add_button(label="Zero item size", callback=lambda: create_bar_group(total_bars=0))
        dpg.add_button(label="Bad labels count", callback=lambda: create_bar_group(labels=["What"]))

    dpg.add_separator()

create_bar_group(shift=-5)

dpg.setup_dearpygui()
dpg.show_viewport()
# dpg.show_style_editor()
dpg.start_dearpygui()
dpg.destroy_context()
