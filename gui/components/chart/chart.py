from kivy import platform
from kivy.graphics import Color, Line, Ellipse
from kivy.lang import Builder
from kivy.properties import ListProperty
from kivy.uix.widget import Widget
from kivymd.uix.floatlayout import MDFloatLayout
from kivymd.uix.label import MDLabel
import math

Builder.load_file("components/chart/chart.kv")


class Circle(Widget):
    def __init__(self, color=(1, 0, 0, 1), size=3, **kwargs):
        super().__init__(**kwargs)
        self.color = color  # Dot color
        self.size_hint = (None, None)  # Ensure size is independent of layout
        self.size = (size, size)  # Set the size of the dot
        self.bind(pos=self.update_canvas)  # Update the canvas if position changes
        self.update_canvas()

    def update_canvas(self, *args):
        """Draw a single point (dot) on the canvas."""
        self.canvas.clear()
        with self.canvas:
            Color(*self.color)  # Set the color of the dot
            Ellipse(pos=self.pos, size=self.size)

class Chart(MDFloatLayout):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.reference = None
        self.app = None
        self._data = None

        self.points = []
        self.point = None

    def __setattr__(self, item, value):
        if item == "data":
            self.reference = self.ids["reference"]
            self.content = self.ids["content"]
            self.x_axis = self.ids["x_axis"]
            self.y_axis = self.ids["y_axis"]
            self._data = value
            self.parent_size = self.parent.parent.size

            self.draw_reference()
            self.draw_content()

        else:
            super().__setattr__(item, value)

    def draw_reference(self):
        def get_limits():
            return [2* (self.parent_size[1] // 3), self.parent_size[1]]

        def get_lines():
            parent_size = self.parent_size

            limits = get_limits()
            height = limits[1] - limits[0]

            lines_count = 11
            _step = height // lines_count

            _lines = []

            for j in range(lines_count):
                _lines.append(
                    ((0, (2 * (parent_size[1] // 3) + (_step * (j + 1)))), (parent_size[0], (2 * (parent_size[1] // 3) + (_step * (j + 1)))))
                )

            return _lines, _step

        reference = self.reference
        x_axis = self.x_axis
        y_axis = self.y_axis
        data = self._data
        lines, step = get_lines()

        for line in lines:
            with reference.canvas:
                Color(1, 1, 1, .3)
                Line(points=line, width=1)

        for i in range(len(data["x"])):
            label = MDLabel(text=str(data["x"][i]), halign="center", opacity=.3, font_style="Caption")
            x_axis.add_widget(label)

        for i in range(11):
            label = MDLabel(text=f"{str(round((max(data['y']) * i) / 10 / 1000))}K", halign="center", opacity=.3, font_style="Caption", adaptive_size=False)
            label.pos_hint = {"center_x": .5, "center_y": round((.1 * i), 1)}
            y_axis.add_widget(label)

        self.ids["name"].text = data["name"]

    def draw_content(self):
        parent_size = self.parent_size
        content = self.content
        base_x = 0

        step_x = parent_size[0] // 7

        y_data = self._data["y"]
        max_y = max(y_data)

        points = []

        for i in range(len(y_data)):
            circle = Circle()
            pos_hint = {"center_x" : ((step_x * i) + (step_x/2))/parent_size[0], "center_y": y_data[i] / max_y}
            circle.pos_hint = pos_hint
            points.append(pos_hint)
            content.add_widget(circle)

        else:
            links = self.generate_interpolated_points(points)

            for link in links:
                circle = Circle()
                circle.pos_hint = link
                content.add_widget(circle)

    @staticmethod
    def generate_interpolated_points(points, steps=300):
        # todo: v2: add the blue line chart for incomes
        # todo: v2: add on_clik receiver on chart to switchbetween income, outcome and solde
        """
        Generate interpolated points between each pair of points.

        :param points: List of points with 'center_x' and 'center_y' keys
        :param steps: Number of interpolated points between each pair
        :return: List of interpolated points
        """
        interpolated_points = []

        for j in range(len(points) - 1):
            # Get start and end points
            start = points[j]
            end = points[j + 1]

            # Add the start point to the result
            interpolated_points.append(start)

            # Generate interpolated points
            for t in range(1, steps):
                fraction = t / steps
                new_x = start['center_x'] + fraction * (end['center_x'] - start['center_x'])
                new_y = start['center_y'] + fraction * (end['center_y'] - start['center_y'])
                interpolated_points.append({'center_x': new_x, 'center_y': new_y})

        # Add the final point
        interpolated_points.append(points[-1])

        return interpolated_points
