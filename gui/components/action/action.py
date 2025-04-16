from kivy.lang import Builder
from kivymd.uix.floatlayout import MDFloatLayout

Builder.load_file("components/action/action.kv")


class Action(MDFloatLayout):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def on_kv_post(self, base_widget):
        parameters = {
            "icon": self.icon,
            "text": self.text,
        }

        parameter = "_".join([i for i, j in parameters.items() if j])

        for key, value in self.ids.items():
            if key != parameter:
                self.remove_widget(value)

            else:
                value.opacity = 1
