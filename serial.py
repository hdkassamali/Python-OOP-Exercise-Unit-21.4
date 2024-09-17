"""Python serial number generator."""


class SerialGenerator:
    """Machine to create unique incrementing serial numbers.

    >>> serial = SerialGenerator(start=100)

    >>> serial.generate()
    100

    >>> serial.generate()
    101

    >>> serial.generate()
    102

    >>> serial.reset()

    >>> serial.generate()
    100
    """

    def __init__(self, start):
        """Make a new generator, starting at start."""
        self.start = self.original_value = start

    def __repr__(self):
        """SHow representation"""
        return f"<SerialGenerator start={self.start} next={self.start + 1}>"

    def generate(self):
        """Generates a serial number from self.start, incrementing by 1 each time."""
        serial_num = self.start
        self.start += 1
        return serial_num

    def reset(self):
        """Resets self.start to the original value passed in."""
        self.start = self.original_value
