from kivy.lang import Builder
from kivymd.app import MDApp
from kivymd.uix.boxlayout import MDBoxLayout

Builder.load_file("components/menu/menu.kv")


class Menu(MDBoxLayout):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def on_kv_post(self, base_widget):
        for key, value in self.ids.items():
            if key == self.receiver:
                value.icon.replace("-outline", "")

                value.opacity = 1

            else:
                value.opacity = .5

    def switch(self, clicked_button):
        app = MDApp.get_running_app()

        current_button = self.ids[app.manager.current.lower()]

        if clicked_button != current_button:
            origin = self.receiver.capitalize()
            target = [key.capitalize() for key, value in self.ids.items() if value == clicked_button][0]

            app.switch_screen(origin, target)
