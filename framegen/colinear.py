from framegen.framegen import FrameGenerator
from msq import MillionFrame


class ColinearGenerator(FrameGenerator):
    """Generator that generates frames with both hands 180 degree to each other"""
    def __init__(self, width, height):

        self._width = width
        self._height = height

    def get_frame(self, **kwargs) -> MillionFrame:
        """Creates and returns the frame"""

        if 'position' not in kwargs:
            raise ValueError("Argument 'position' required")

        position = kwargs['position']

        frame = MillionFrame(self._width, self._height)

        hand_a_position = position % 200
        hand_b_position = (position + 100) % 200

        for x in range(self._width):
            for y in range(self._height):
                frame.set_at_index(x, y, 'a', hand_a_position)
                frame.set_at_index(x, y, 'b', hand_b_position)
        return frame
