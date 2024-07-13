#!/usr/local/bin/python3

from math import cos, pi, sin
import dearpygui.dearpygui as dpg

dpg.create_context()
dpg.configure_app(anti_aliased_fill=True, anti_aliased_lines=True, anti_aliased_lines_use_tex=True)
dpg.create_viewport(title=f"Test - {dpg.get_dearpygui_version()}", width=700, height=900)


with dpg.window():
    dpg.set_primary_window(dpg.last_item(), True)

    def on_option(sender, checked, opt_name):
        args = {opt_name: checked}
        dpg.configure_app(**args)

    with dpg.group(horizontal=True):
        for opt in ("anti_aliased_fill", "anti_aliased_lines", "anti_aliased_lines_use_tex"):
            dpg.add_checkbox(label=opt, callback=on_option, user_data=opt, default_value=True)

    x_data = [x/2 for x in range(0, 20)]
    x_data2 = [-x for x in x_data]
    y_data = [10*sin(x) for x in x_data]

    y_data2 = [-y for y in y_data]
    
    with dpg.theme() as marker_theme:
        with dpg.theme_component():
            dpg.add_theme_style(dpg.mvPlotStyleVar_Marker, dpg.mvPlotMarker_Circle, category=dpg.mvThemeCat_Plots)

    with dpg.plot(width=-1, height=400, tag="plot"):
        dpg.add_plot_legend(tag="plot-legend")
        x_axis = dpg.add_plot_axis(dpg.mvXAxis, no_tick_labels=True)
        with dpg.plot_axis(dpg.mvYAxis, no_tick_labels=True) as y_axis:
            dpg.add_line_series(x_data, y_data, label="lines")
            dpg.bind_item_theme(dpg.last_item(), marker_theme)
            dpg.add_shade_series(x_data2, y_data2, label="fill")
            dpg.bind_item_theme(dpg.last_item(), marker_theme)

    def calc_poly_points(center_x, center_y, radius, vertices_count, init_angle=0):
        return [
            (
                center_x + radius * sin((a / vertices_count + init_angle) * 2 * pi),
                center_y + radius * cos((a / vertices_count + init_angle) * 2 * pi)
            )
            for a in range(vertices_count)
        ]

    with dpg.drawlist(width=650, height=400):
        dpg.draw_polygon(calc_poly_points(150, 150, 150, 5, 0.01))
        dpg.draw_polygon(calc_poly_points(500, 150, 150, 5, 0.01), fill=(153, 102, 204), color=(0, 0, 0, -255))

        # Anti-aliased fill is seen on round shapes but not on polygons; that seems to be the way ImGui implements it.
        dpg.draw_circle((150, 150), 100, fill=(153, 102, 204), color=(0, 0, 0, -255))


dpg.setup_dearpygui()
dpg.show_viewport()
dpg.start_dearpygui()
dpg.destroy_context()
