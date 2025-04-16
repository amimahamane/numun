from datetime import datetime
from kivy.clock import Clock
from screeninfo import get_monitors
from kivy.core.window import Window
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager
from kivymd.app import MDApp

Builder.load_file("imports.kv")

class Manager(ScreenManager):
    pass


class Main(MDApp):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        self.manager = None
        self.history = []
        self.monitor = None

    def build(self):
        self.set_window()

        self.manager = Manager()
        return self.manager


    def switch_screen(self, origin, target):
        self.history.append(origin)
        self.manager.current = target


    def set_window(self):
        monitor = self.get_current_monitor()

        width = monitor["width"]
        height = monitor["height"]

        Window.size = (height, height)
        Window.top = 0
        Window.left = 0

        self.monitor = monitor


    @staticmethod
    def get_current_monitor():
        window_x, window_y = Window.left, Window.top

        for monitor in get_monitors():
            if (monitor.x <= window_x < monitor.x + monitor.width and
                    monitor.y <= window_y < monitor.y + monitor.height):
                return {
                    "name": monitor.name,
                    "width": monitor.width,
                    "height": monitor.height,
                    "x": monitor.x,
                    "y": monitor.y
                }

        return None


Main().run()
