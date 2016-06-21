class MillionFrame:
    def __init__(self, width, height, data):
        self._width = width
        self._height = height
        self._data = data

    @property
    def width(self) -> int:
        return self._width

    @property
    def height(self) -> int:
        return self._height

    def get_at_position(self, x, y, hand) -> int:
        if x >= self._width or y >= self._height:
            raise IndexError("Index out of bounds: size (%d : %d) requested: (%d : %d)"
                             % (self._width, self._height, x, y))

        if hand == 1 or hand == "a":
            return self._data[(y * self._width + x) * 2]
        if hand == 2 or hand == "b":
            return self._data[(y * self._width + x) * 2 + 1]
        return None