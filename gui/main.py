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
        self.window_bar_size = None

    def build(self):
        self.set_window()

        Clock.schedule_interval(self.info, 1)

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
        Window.left = (width // 2) - (height // 2)

        self.monitor = monitor

    def info(self, dt):
        monitor = self.get_current_monitor()
        size = Window.size

        print(size)
        print((monitor["width"], monitor["height"]))

        side = {*size}

        if len(side) > 1:
            if self.are_close(size[0], monitor["width"]//2, size[0]//100):
                side = min(side)

                Window.maximize()
                Window.size = (side, side)

            elif self.are_close(size[0], monitor["width"], size[0]//100):
                Window.restore()


    @staticmethod
    def are_close(first_value, second_value, tolerance):
        difference = abs(first_value - second_value)

        return difference <= tolerance

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
