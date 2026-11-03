#!/usr/bin/env python3
"""Define a complete Rectangle class."""

RectangleBase = __import__('1-rectangle').Rectangle


class Rectangle(RectangleBase):
    """Represent a rectangle with area and string representation."""

    def area(self):
        """Return the rectangle area."""
        return self._Rectangle__width * self._Rectangle__height

    def __str__(self):
        """Return the rectangle description."""
        return "[Rectangle] {}/{}".format(
            self._Rectangle__width,
            self._Rectangle__height
        )
