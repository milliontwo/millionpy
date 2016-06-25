import io
import array
import itertools
from msq.millionFrame import MillionFrame


class MSQParseError(Exception):
    pass


class MsqReader:
    """A reader class that provides functionality to read the MSQ file format"""

    def __init__(self, file):
        self._file = open(file, 'rb')

        # check marker
        marker = self._file.read(7)
        if marker != b"MILLION":
            raise MSQParseError("Not correct type of file")

        # get version
        self._version = int.from_bytes(self._file.read(1),  byteorder='big')
        if self._version != 1:
            raise MSQParseError("MSQ Version not supported")

        # get dimensions
        self._dimensions = (int.from_bytes(self._file.read(1), byteorder='big'),
                            int.from_bytes(self._file.read(1), byteorder='big'))

        # get frame rate
        self._frame_rate = int.from_bytes(self._file.read(1), byteorder='big')

        # check end of header
        a = self._file.read(1)
        if a != b'\xFF':
            raise MSQParseError("Header not terminated by 0xFF")

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self._file.close()

    def _byte_array_to_int_array(self, byte_array):
        int_array = array.array("B", itertools.repeat(0, len(byte_array)))
        for i in range(len(byte_array)):
            int_array[i] = byte_array[i]
        return int_array

    def next_frame(self) -> MillionFrame:
        size = self._dimensions[0]*self._dimensions[1]*2
        data = self._byte_array_to_int_array(self._file.read(size))

        # Check if there was even enough data left for a frame. Return None if we reached end
        if len(data) != size:
            return None

        # Check if next frame is 0xFF to ensure that the read that is a proper frame
        if self._file.read(1) != b'\xFF':
            raise MSQParseError("Frame not terminated by 0xFF")

        return MillionFrame(self._dimensions[0], self._dimensions[1], data)

    @property
    def dimensions(self):
        return self._dimensions

    @property
    def frame_rate(self):
        return self._frame_rate

    @property
    def version(self):
        return self._version

    def close(self):
        self._file.close()
