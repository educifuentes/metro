class Station:
    """Representation of a metro station with color and adjacent stations attributes.
    Attributes:
    next: list
        adjacent stations of the station
    color: str
        color of the station
    """

    def __init__(self, next, color):
        self.next = next
        self.color = color
