# imports for required modules and packages
import kivymd
from graphs import PressureChart, VolumeChart, FlowChart
import kivy.garden.matplotlib.backend_kivy
from kivymd.uix.dropdownitem import MDDropDownItem
from kivymd.uix.label import MDLabel
from kivymd.uix.menu import MDDropdownMenu
from layoutmargin import AddMargin, MarginLayout
from kivy.factory import Factory
from kivymd.app import MDApp
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.boxlayout import BoxLayout
from kivy.graphics import Color, Rectangle
from kivy.properties import BooleanProperty
from kivymd.uix.bottomsheet import MDCustomBottomSheet
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.screen import MDScreen
from kivymd.uix.taptargetview import MDTapTargetView


# Defining global variables


class CustBoxLayout(BoxLayout, MarginLayout):
    def __init__(self, **kwargs):
        super(CustBoxLayout, self).__init__(**kwargs)
        with self.canvas.before:
            Color(.4, .3, .3, 1)
            self.rec = Rectangle(size=self.size, pos=self.pos)
        self.bind(size=self._update_rec, pos=self._update_rec)

    def _update_rec(self, instance, value):
        self.rec.pos = instance.pos
        self.rec.size = instance.size


class MyLabel(MDLabel, AddMargin):
    pass


class MonitorScreen(MDScreen, MarginLayout):
    def __init__(self, **kwargs):
        super(MonitorScreen, self).__init__(**kwargs)

    def go_back_to_control(self):
        self.manager.current = 'control'


class ContentCustomSheet(MDBoxLayout, MarginLayout):
    def __init__(self, screen=None, **kwargs):
        super(ContentCustomSheet, self).__init__(**kwargs)
        self.screen = screen
        self.tap_target_view = MDTapTargetView(
            widget=self.ids.commitTipsButton,
            widget_position="right_bottom",
            title_text="Tips for You",
            title_text_size="20sp",
            description_text="After selecting a numeric values in\nthe above controls using the\nincrement or decrement " +
                             "buttons,\nclick on the new number to\ncommit to the ventilator",
            description_text_color=[1, 1, .5, 1]
        )

    def tap_target_start(self):
        if self.tap_target_view.state == "close":
            self.tap_target_view.start()
        else:
            self.tap_target_view.stop()

    def numeric_buttons_callback(self, button_type=None, widget=None):
        """
        This method is called by the increment and decrement buttons in the bottom sheet of the Control Screen
        :param button_type: str value, its either 'decrement' or 'increment'
        :param widget: The widget whose text is to be updated
        :return: None
        """
        value_char = ''
        if widget.text.isdigit():
            value_digit = eval(widget.text)
        else:
            values = widget.text.split(':')
            value_char = values[0] + ':'
            value_digit = eval(values[-1])
        if button_type == 'decrement':
            value_digit -= 1
        else:
            value_digit += 1
        widget.text = value_char + str(value_digit)


class ControlScreen(MDScreen):
    bluetooth_state = BooleanProperty(defaultvalue=False)

    def __init__(self, **kwargs):
        super(ControlScreen, self).__init__(**kwargs)

    def see_active_devices(self):
        menu_items = [{"icon": "git", "text": f"Item {i}"} for i in range(5)]
        self.menu_available_devices = MDDropdownMenu(
            caller=self.ids.available_devices,
            items=menu_items,
            position="bottom",
            width_mult=4,
        )
        self.menu_available_devices.bind(on_release=self.set_item_available_device)
        self.menu_available_devices.open()

    def see_paired_devices(self):
        menu_items = [{"icon": "git", "text": f"Item {i}"} for i in range(5)]
        self.menu_paired_devices = MDDropdownMenu(
            caller=self.ids.paired_devices,
            items=menu_items,
            position="bottom",
            width_mult=4,
        )
        self.menu_paired_devices.bind(on_release=self.set_item_paired_device)
        self.menu_paired_devices.open()

    def set_item_available_device(self, instance_menu, instance_menu_item):
        assert isinstance(self.ids.drop_item, MDDropDownItem)
        self.ids.available_devices.set_item(instance_menu_item.text)
        self.menu_available_devices.dismiss()

    def set_item_paired_device(self, instance_menu, instance_menu_item):
        assert isinstance(self.ids.drop_item, MDDropDownItem)
        self.ids.paired_devices.set_item(instance_menu_item.text)
        self.menu_paired_devices.dismiss()


class ScreenManagement(ScreenManager):
    pass


class VentilatorApp(MDApp):
    custom_sheet = None

    def show_bottom_sheet(self, screen=None):
        self.custom_sheet = MDCustomBottomSheet(screen=Factory.ContentCustomSheet(screen=screen))
        self.custom_sheet.open()

    def build(self):
        self.theme_cls.primary_palette = "Green"  # "Purple", "Red"
        self.theme_cls.primary_hue = "500"  # "500"
        self.theme_cls.primary_dark_hue = "800"
        #self.theme_cls.theme_style = "Dark"


if __name__ == '__main__':
    VentilatorApp().run()

'''
MDSpinner:
        size_hint: None, None
        size: dp(46), dp(46)
        pos_hint: {'center_x': .5, 'center_y': .5}
        active: True if check.active else False
'''