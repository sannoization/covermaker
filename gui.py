import dearpygui.dearpygui as dpg

from main import run

dpg.create_context()
dpg.create_viewport(title='Covermaker 1.0.0', width=500, height=500)

with dpg.font_registry():
    default_font = dpg.add_font(file='resources/Montserrat-SemiBold.ttf', size=20)
    second_font = dpg.add_font(file='resources/Montserrat-Regular.ttf', size=20)
    dpg.add_font_range_hint(dpg.mvFontRangeHint_Cyrillic, parent=default_font)
    dpg.add_font_range_hint(dpg.mvFontRangeHint_Cyrillic, parent=second_font)

def test_callback(sender, data):
    heading = dpg.get_value('heading')
    date = dpg.get_value('date')
    result_image = dpg.get_value('result_image')
    if result_image == '':
        result_image = 'res'
    result_image += '.jpg'
    print(heading)
    print(date)
    print(result_image)
    dpg.show_item('result_saved')
    dpg.set_value('result_heading', 'heading: ' + heading)
    dpg.set_value('result_date', 'date: ' + date)
    dpg.set_value('result_filename', 'in file: ' + result_image)
    run(heading=heading, date=date, result_image=result_image)


with dpg.window(label="Covermaker 1.0.0",
                tag='window',
                width=500,
                height=500,
                no_resize=True,
                no_move=True):
    dpg.bind_font(default_font)
    text1 = dpg.add_text("Enter heading")
    input1 = dpg.add_input_text(tag="heading",
                       hint='enter heading...',
                       multiline=True,
                       height=100)
    text2 = dpg.add_text("Enter date")
    input2 = dpg.add_input_text(tag="date",
                       hint='01.02.2022',
                       multiline=True,
                       height=100)
    text3 = dpg.add_text("Enter output filename")
    input3 = dpg.add_input_text(tag="result_image",
                       hint='filename')
    dpg.add_spacer(height=3)
    dpg.add_button(label="Save", callback=test_callback, tag='save_button')
    dpg.add_spacer(height=5)
    dpg.add_text('Saved!', tag='result_saved', show=False)
    dpg.add_text('', tag='result_heading')
    dpg.add_text('', tag='result_date')
    dpg.add_text('', tag='result_filename')

    dpg.bind_item_font(input1, second_font)
    dpg.bind_item_font(input2, second_font)
    dpg.bind_item_font(input3, second_font)

dpg.setup_dearpygui()
dpg.show_viewport()
dpg.start_dearpygui()
dpg.destroy_context()
