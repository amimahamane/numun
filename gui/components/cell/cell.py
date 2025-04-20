import random

from kivy.lang import Builder
from kivymd.uix.boxlayout import MDBoxLayout

Builder.load_file("components/grid/grid.kv")


class Cell(MDBoxLayout):
    def __init__(self, *args, **kwargs):
        attributes_names = {
            "death_color": self.get_random_color,
            "life_color": self.get_random_color,
            "alive": self.is_random_alive
        }

        attributes = {
            key: kwargs.get(key, value()) for key, value in attributes_names.items()
        }

        for key, value in attributes.items():
            setattr(self, key, value)

            if key in kwargs:
                del kwargs[key]

        super().__init__(*args, **kwargs)

    def on_kv_post(self, base_widget):
        self.md_bg_color = self.life_color if self.alive else self.death_color


    def on_touch_down(self, touch):
        if 'button' in touch.profile:
            if self.collide_point(*touch.pos):
                if touch.button == 'left':
                    print("🖱️ Left click detected at", touch.pos)
                    self.alive = not self.alive
                    self.md_bg_color = self.life_color if self.alive else self.death_color


                elif touch.button == 'right':
                    print("🖱️ Right click detected at", touch.pos)

        return super().on_touch_down(touch)


    @staticmethod
    def get_random_color():
        color = tuple(round(random.uniform(0.1, 1.0), 1) for i in range(4))

        return color

    @staticmethod
    def is_random_alive():
        return random.choice([False, True])