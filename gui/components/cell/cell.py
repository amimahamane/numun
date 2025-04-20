from kivy.lang import Builder
from kivymd.uix.boxlayout import MDBoxLayout

Builder.load_file("components/grid/grid.kv")


class Cell(MDBoxLayout):
    def __init__(self, *args, **kwargs):
        self.color = kwargs.get("color", (1, 0, 0, 1))

        if "color" in kwargs:
            del kwargs["color"]

        super().__init__(*args, **kwargs)

    def on_kv_post(self, base_widget):
        self.md_bg_color = self.color