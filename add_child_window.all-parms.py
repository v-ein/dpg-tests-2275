#!/usr/local/bin/python3

import warnings
import dearpygui.dearpygui as dpg

print(dpg.__file__)
warnings.simplefilter('always', DeprecationWarning)

dpg.create_context()
dpg.create_viewport(title=f"Test - {dpg.get_dearpygui_version()}", width=900, height=700)

flashers = []
child_windows = []

with dpg.theme() as global_theme:
    with dpg.theme_component(dpg.mvAll):
        dpg.add_theme_color(dpg.mvThemeCol_ChildBg, (51, 102, 51))
dpg.bind_theme(global_theme)

with dpg.window():
    dpg.set_primary_window(dpg.last_item(), True)
    flash_checkbox = dpg.add_checkbox(label="Flashers enabled")

with dpg.item_handler_registry() as resize_handler:
    dpg.add_item_resize_handler(callback=lambda s, w: print(f"[{dpg.get_frame_count():4}] Resize event: {dpg.get_item_alias(dpg.get_item_children(w, slot=1)[0])}"))

def create_child_window(caption, **kwargs):
    # Need a group to track child resize events
    with dpg.group():
        dpg.bind_item_handler_registry(dpg.last_item(), resize_handler)

        with dpg.child_window(**kwargs) as child:
            child_windows.append([child, [0, 0]])

            dpg.add_button(label=caption)
            with dpg.collapsing_header(label="Expand me"):
                dpg.add_text("dolor sit amet, consectetur adipiscing elit")

            flashers.append(dpg.add_text("A flasher to make child size change with time", show=False))


with dpg.window(width=350, height=300, pos=(0, 50)):
    dpg.add_text("Lorem")

    create_child_window(
        "Resizable child + frame_style",
        tag="resizable",
        resizable_x=True, resizable_y=True,
        frame_style=True
    )

    create_child_window(
        "Fixed-size child + frame_style",
        tag="fixed-size",
        width=200, height=100,
        auto_resize_x=True, auto_resize_y=True,
        resizable_x=True, resizable_y=True,
        frame_style=True
    )


with dpg.window(width=400, height=300, pos=(400, 50)):
    dpg.add_text("Lorem")

    create_child_window(
        "Autosized child",
        tag="autosized",
        auto_resize_x=True, auto_resize_y=True,
        resizable_x=True, resizable_y=True
    )

    create_child_window(
        "always_auto_resize",
        tag="always_auto_resize",
        always_auto_resize=True,
        auto_resize_x=True, auto_resize_y=True,
        resizable_x=True, resizable_y=True
    )


with dpg.window(width=350, height=250, pos=(0, 400)):
    dpg.add_text("Lorem")

    create_child_window(
        "Borderless regular",
        tag="borderless",
        width=200, height=100,
        border=False
    )

    create_child_window(
        "always_use_window_padding",
        tag="always_use_window_padding",
        width=200, height=100,
        border=False,
        always_use_window_padding=True
    )


def check_child_window_sizes():
    for entry in child_windows:
        child, old_size = entry
        cur_size = dpg.get_item_rect_size(child)
        if cur_size != old_size:
            print(f"[{dpg.get_frame_count():4}] Size changed: {dpg.get_item_alias(child)}, {old_size} -> {cur_size}")
            entry[1] = cur_size

dpg.setup_dearpygui()
dpg.show_viewport()

while (dpg.is_dearpygui_running()):
    if dpg.get_value(flash_checkbox):
        show = (dpg.get_frame_count() // 60 % 2 == 0)
        for flasher in flashers:
            dpg.configure_item(flasher, show=show)

    check_child_window_sizes()
    dpg.render_dearpygui_frame()

dpg.destroy_context()
