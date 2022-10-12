import dearpygui.dearpygui as dpg
import main
from main import run

dpg.create_context()
dpg.create_viewport(title='Covermaker 1.0.0', width=500, height=500)

with dpg.handler_registry():
    run()
with dpg.window(label="Covermaker 1.0.0",
                width=500,
                height=500,
                no_resize=True,
                no_move=True):
    dpg.add_text("Enter heading")
    dpg.add_input_text(default_value="Quick brown fox", tag="heading")
    dpg.add_text("Enter date")
    dpg.add_input_text(default_value="2022/02/02", tag="date")
    dpg.add_button(label="Save")

dpg.setup_dearpygui()
dpg.show_viewport()
dpg.start_dearpygui()
dpg.destroy_context()