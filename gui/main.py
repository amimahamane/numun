from datetime import datetime

from kivy.clock import Clock
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

    def build(self):
        self.manager = Manager()

        return self.manager

    def on_start(self):
        pass

    def switch_screen(self, origin, target):
        self.history.append(origin)
        self.manager.current = target

Main().run()
