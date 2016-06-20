import tkinter as tk
import math


class Clock(tk.Canvas):
    """Class that describes a clock UI object"""
    CENTER = (17, 17)
    RADIUS = 16

    def __init__(self, parent):
        """Clock initializer"""
        super(Clock, self).__init__(parent, width=2*self.CENTER[0], height=2*self.CENTER[1], highlightthickness=0)
        self.parent = parent

        # Fields that hold the current positions of the hands. Should be in 0<=pos<1
        self._hand_a_position = 0.00
        self._hand_b_position = 0.00

        # Create UI elements at the initial positions
        self._create_circle(self.CENTER[0], self.CENTER[1], self.RADIUS, outline='#cacaca')
        self._hand_a = self._create_hand(self._hand_a_position, width=2)
        self._hand_b = self._create_hand(self._hand_b_position, width=2)

    def _create_circle(self, x, y, r, **kwargs):
        """Private member that allows creating a circle"""
        return self.create_oval(x - r, y - r, x + r, y + r, **kwargs)

    def _create_hand(self, position, **kwargs):
        """Private member that allows creating a hand at the given position"""
        return self.create_line(self.CENTER[0], self.CENTER[1],
                                self.CENTER[0]+self.RADIUS * math.cos(2 * math.pi * position),
                                self.CENTER[1]+self.RADIUS * math.sin(2 * math.pi * position), **kwargs)

    @property
    def hand_a_position(self):
        """Returns the current position of hand a"""
        return self._hand_a_position

    @property
    def hand_b_position(self):
        """Returns the current position of hand b"""
        return self._hand_b_position

    def set_hand_a(self, position):
        """Sets the position of hand a to the given position"""
        if position < 0.0 or position >= 1.0:
            raise ValueError('Hand position out of bounds')
        self.delete(self._hand_a)
        self._hand_a_position = position
        self._hand_a = self._create_hand(position)

    def set_hand_b(self, position):
        """Sets the position of hand b to the given position"""
        if position < 0.0 or position >= 1.0:
            raise ValueError('Hand position out of bounds')
        self.delete(self._hand_b)
        self._hand_b_position = position
        self._hand_b = self._create_hand(position)

