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
        self.grids = {}
        self.grid = None
        self.name = ""
        self._parameters = {}

        super().__init__(*args, **kwargs)


    def on_kv_post(self, base_widget):
        self.set_grid()


    def set_grid(self):
        parameters_keys = Grid.parameters.get(self).keys()
        parameters = {}

        self.grid = self.get_grid()
        self.ids.ground.add_widget(self.grid)

        for key in parameters_keys:
            parameters[key] = getattr(self, key)

        self.parameters = parameters


    def get_grid(self):
        name = f"{"x".join([str(i) for i in self.dimension])}"
        grids = self.grids

        try:
            grid = grids[name]

        except KeyError:
            grid = self.generate_grid()
            self.grids[name] = grid

        return grid


    def generate_grid(self):
        grid = GridLayout(
            cols=self.dimension[0],
            rows=self.dimension[1],
            size_hint=(None, None),
            size=(self.cell_size * self.dimension[0], self.cell_size * self.dimension[1])
        )

        if self.show_lines:
            grid.spacing = self.lines_width
            grid.padding = self.lines_width

        cells = [
            MDBoxLayout(
                size_hint=(None, None),
                size=(self.cell_size, self.cell_size),
                md_bg_color=self.life_color
            ) for i in range(self.dimension[0] * self.dimension[1])
        ]

        for cell in cells:
            grid.add_widget(cell)

        else:
            return grid


    def on_parameters(self, instance, value):
        _parameters = self._parameters

        if _parameters:
            print(value)
            print(_parameters)

            # todo: when dimension changes, call set_grid
            # todo: when others change, call update grid with a dict of parameters and values
            # todo: update the grid

        self._parameters = _parameters