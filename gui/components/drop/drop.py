from kivy.clock import Clock
from kivy.lang import Builder
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.menu import MDDropdownMenu

Builder.load_file("components/drop/drop.kv")


class Drop(MDBoxLayout):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.dropdown = None

    def on_kv_post(self, base_widget):
        self.ids["field"].text = str(self.items[0])

    def open(self):
        items = [
            {
                "viewclass": "OneLineListItem",
                "text": str(i),
                "on_release": lambda x = i : self.select_item(str(x))
            } for i in self.items
        ]

        self.dropdown = MDDropdownMenu(
            caller=self.ids["caller"],
            items=items,
        )

        self.dropdown.open()

    def select_item(self, item):
        self.ids["field"].text = item
        Clock.schedule_once(self.dropdown.dismiss, .2)

    def __getattr__(self, item):
        if item == "text":
            return self.ids["field"].text

        else:
            super().__getattr__(item)

    def __setattr__(self, key, value):
        if key == "text":
            self.ids["field"].text = value

        else:
            super().__setattr__(key, value)