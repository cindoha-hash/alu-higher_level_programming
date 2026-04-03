#!/usr/bin/python3
"""Square class module."""

from models.rectangle import Rectangle


class Square(Rectangle):
    """Square class."""

    def __init__(self, size, x=0, y=0, id=None):
        """Initialize square instance."""
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        """Get size."""
        return self.width

    @size.setter
    def size(self, value):
        """Set size."""
        self.width = value
        self.height = value

    def __str__(self):
        """Return informal string representation."""
        return "[Square] ({}) {}/{} - {}".format(
            self.id, self.x, self.y, self.size
        )

    def update(self, *args, **kwargs):
        """Assign attributes from args or kwargs."""
        attrs = ["id", "size", "x", "y"]
        if args:
            for i, value in enumerate(args):
                if i < len(attrs):
                    setattr(self, attrs[i], value)
        else:
            for key, value in kwargs.items():
                setattr(self, key, value)

    def to_dictionary(self):
        """Return dictionary representation of square."""
        return {
            "id": self.id,
            "size": self.size,
            "x": self.x,
            "y": self.y
        }
