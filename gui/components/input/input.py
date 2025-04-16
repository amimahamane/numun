from kivy.lang import Builder
from kivymd.uix.boxlayout import MDBoxLayout

Builder.load_file("components/input/input.kv")


class Input(MDBoxLayout):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def __getattr__(self, item):
        if item == "text":
            return self.ids["field"].text

        else:
            super().__getattr__(item)

    def __setattr__(self, item, value):
        if item == "text":
            self.ids["field"].text = value

        else:
            super().__setattr__(item, value)