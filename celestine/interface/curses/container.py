""""""

import math

from celestine.window.collection import Rectangle

from .button import Button
from .image import Image
from .label import Label


class Container(Rectangle):
    """"""

    def drop(self, tag, **kwargs):
        """Elements go down. Like a <div> tag."""
        (x_min, y_min, x_max, y_max) = self.get_next()
        return self.item_set(
            tag,
            Drop(
                self.session,
                tag,
                self.turn,
                x_min=x_min,
                y_min=y_min,
                x_max=x_max,
                y_max=y_max,
                **kwargs,
            )
        )

    def grid(self, tag, width, **kwargs):
        """Elements go in a grid. Like the <table> tag."""
        (x_min, y_min, x_max, y_max) = self.get_next()
        return self.item_set(
            tag,
            Grid(
                self.session,
                tag,
                self.turn,
                width,
                x_min=x_min,
                y_min=y_min,
                x_max=x_max,
                y_max=y_max,
                **kwargs,
            )
        )

    def span(self, tag, **kwargs):
        """Elements go sideways. Like a <span> tag."""
        (x_min, y_min, x_max, y_max) = self.get_next()
        return self.item_set(
            tag,
            Span(
                self.session,
                tag,
                self.turn,
                x_min=x_min,
                y_min=y_min,
                x_max=x_max,
                y_max=y_max,
                **kwargs,
            )
        )

    def draw(self, collection):
        """"""
        for (_, item) in self.item.items():
            item.draw(collection)

    def poke(self, x_dot, y_dot):
        """"""
        for (_, item) in self.item.items():
            item.poke(x_dot, y_dot)

    def button(self, tag, text, action):
        """"""
        return self.item_set(
            tag,
            Button(text, action=lambda: self.turn(action)),
        )

    def image(self, tag, image):
        """"""
        return self.item_set(
            tag,
            Image(image),
        )

    def label(self, tag, text):
        """"""
        return self.item_set(
            tag,
            Label(text),
        )

    def __enter__(self):
        return self

    def __exit__(self, *_):
        return False

    def __init__(self, session, name, turn, **kwargs):
        self.session = session
        self.tag = name
        self.turn = turn
        super().__init__(**kwargs)


class Grid(Container):
    """"""

    def button(self, tag, text, action):
        """"""
        name = self._get_tag(tag)
        super().button(name, text, action)

    def image(self, tag, image):
        """"""
        name = self._get_tag(tag)
        super().image(name, image)

    def label(self, tag, text):
        """"""
        name = self._get_tag(tag)
        super().label(name, text)

    def items(self):
        """"""
        yield from [item for (_, item) in self.item.items()]

    def spot(self, x_min, y_min, x_max, y_max):
        """"""
        self.set(x_min, y_min, x_max, y_max)

        partition_x = self.width
        partition_y = math.ceil(len(self.item) / self.width)
        (axis_x, axis_y) = self.get(partition_x, partition_y)

        items = self.items()

        for _ in range(partition_y):
            (ymin, ymax) = next(axis_y)

            for _ in range(partition_x):
                (xmin, xmax) = next(axis_x)

                item = next(items)
                item.spot(xmin, ymin, xmax, ymax)

        axis_x.close()
        axis_y.close()

    def _get_tag(self, name):
        """"""
        length = len(self.item)
        index_x = length % self.width
        index_y = length // self.width

        return F"{name}_{index_x}-{index_y}"

    def __init__(self, session, name, turn, width, **kwargs):
        self.width = width
        super().__init__(session, name, turn, **kwargs)


class Drop(Container):
    """"""

    def spot(self, x_min, y_min, x_max, y_max):
        """"""
        self.set(x_min, y_min, x_max, y_max)

        partition_x = 1
        partition_y = len(self.item)
        (axis_x, axis_y) = self.get(partition_x, partition_y)

        for (_, item) in self.item.items():
            (xmin, xmax) = next(axis_x)
            (ymin, ymax) = next(axis_y)

            item.spot(xmin, ymin, xmax, ymax)

        axis_x.close()
        axis_y.close()


class Span(Container):
    """"""

    def spot(self, x_min, y_min, x_max, y_max):
        """"""
        self.set(x_min, y_min, x_max, y_max)

        partition_x = len(self.item)
        partition_y = 1
        (axis_x, axis_y) = self.get(partition_x, partition_y)

        for (_, item) in self.item.items():
            (xmin, xmax) = next(axis_x)
            (ymin, ymax) = next(axis_y)

            item.spot(xmin, ymin, xmax, ymax)

        axis_x.close()
        axis_y.close()
