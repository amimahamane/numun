from kivy.lang import Builder
from kivy.uix.gridlayout import GridLayout
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.floatlayout import MDFloatLayout

Builder.load_file("components/grid/grid.kv")


class Grid(MDFloatLayout):
    def __init__(self, *args, **kwargs):
        self.grids = {}
        self.grid = None
        self.name = ""

        super().__init__(*args, **kwargs)


    def on_kv_post(self, base_widget):
        self.set_grid()


    def set_grid(self):
        self.grid = self.get_grid()

        self.ids.ground.add_widget(self.grid)

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
