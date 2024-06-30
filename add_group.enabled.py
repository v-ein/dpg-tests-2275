import dearpygui.dearpygui as dpg

dpg.create_context()
dpg.create_viewport(title=f"Test - {dpg.get_dearpygui_version()}", width=700, height=700)

with dpg.theme() as theme:
    for comp_type in (dpg.mvGroup,):
        with dpg.theme_component(comp_type, enabled_state=False):
            dpg.add_theme_color(dpg.mvThemeCol_Text, (255, 0, 0)) 
            dpg.add_theme_color(dpg.mvThemeCol_TextDisabled, (255, 255, 0)) 
        with dpg.theme_component(comp_type, enabled_state=True):
            dpg.add_theme_color(dpg.mvThemeCol_Text, (0, 255, 255)) 
            dpg.add_theme_color(dpg.mvThemeCol_TextDisabled, (0, 0, 255)) 

with dpg.window():
    dpg.set_primary_window(dpg.last_item(), True)
    dpg.bind_item_theme(dpg.last_item(), theme)

    with dpg.group(horizontal=True):
        dpg.add_checkbox(label="Enabled", callback=lambda s, checked: dpg.configure_item("group", enabled=checked), default_value=True)

    dpg.add_spacer(height=12)
    dpg.add_text(
        "Colors in an enabled group: Text is cyan, TextDisabled is blue\n"
        "Colors in a disabled group: Text is red, TextDisabled is yellow\n"
        "Some widgets use Text, some (rarely) use TextDisabled.\n"
        "Some (like a selectable) even use the alpha channel (controlled with mvStyleVar_DisabledAlpha)."
    )

    with dpg.group(tag="group"):
        dpg.add_text("Text")
        def create_widgets(enabled):
            dpg.add_button(label="Button", callback=lambda: print("Button clicked"), enabled=enabled)
            dpg.add_selectable(label="Selectable", callback=lambda s, a: print(f"Selectable: {a}"), enabled=enabled)
            dpg.add_input_text(default_value="Text input", callback=lambda s, a: print(f"Text input: {a}"), enabled=enabled)
            dpg.add_input_text(hint="Input's hint", callback=lambda s, a: print(f"Text input: {a}"), enabled=enabled)
            dpg.add_combo(items=[f"item {i}" for i in range(10)], callback=lambda s, a: print(f"Combo: {a}"), enabled=enabled)

        create_widgets(True)
        create_widgets(False)

dpg.setup_dearpygui()
dpg.show_viewport()
dpg.start_dearpygui()
dpg.destroy_context()