from kivy.clock import Clock
from kivy.lang import Builder
from kivy.properties import DictProperty
from kivy.uix.gridlayout import GridLayout
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.floatlayout import MDFloatLayout

Builder.load_file("components/grid/grid.kv")


class Grid(MDFloatLayout):
    parameters = DictProperty(
        {
            "dimension": None,
            "life_color": None,
            "death_color": None,
            "lines_color": None,
            "show_lines": None,
            "lines_width": None,
            "cell_size": None,
        }
    )

    def __init__(self, *args, **kwargs):
        self.content = None
        self.name = ""
        self._parameters = {}

        super().__init__(*args, **kwargs)


    def on_kv_post(self, base_widget):
        Clock.schedule_once(self.set_content, 1)


    def set_content(self, dt):
        parameters_keys = Grid.parameters.get(self).keys()
        parameters = {}

        self.content = self.get_content()
        self.ids.ground.add_widget(self.content)

        for key in parameters_keys:
            parameters[key] = getattr(self, key)

        self.parameters = parameters


    def get_content(self):
        content = self.content or self.generate_content()

        return content


    def generate_content(self):
        content = GridLayout(
            cols=self.dimension[0],
            rows=self.dimension[1],
            size_hint=(None, None),
            size=(self.cell_size * self.dimension[0], self.cell_size * self.dimension[1])
        )

        if self.show_lines:
            content.spacing = self.lines_width
            content.padding = self.lines_width

        cells = [
            MDBoxLayout(
                size_hint=(None, None),
                size=(self.cell_size, self.cell_size),
                md_bg_color=self.life_color
            ) for i in range(self.dimension[0] * self.dimension[1])
        ]

        for cell in cells:
            content.add_widget(cell)

        else:
            return content


    def on_parameters(self, instance, value):
        _parameters = self._parameters

        if _parameters:
            print(value)
            print(_parameters)

            # todo: when dimension changes, call set_grid
            # todo: when others change, call update grid with a dict of parameters and values
            # todo: update the grid

        self._parameters = _parameters