import io
from msq.millionFrame import MillionFrame


class MsqWriter:
    def __init__(self, file, width, height, frame_rate=30):

        self._width = width
        self._height = height
        self._frame_rate = frame_rate

        # check if it has a header
        self._file = open(file, 'w+b')
        marker = self._file.read(7)
        if len(marker) == 0:
            self._write_header()
        elif marker != b"MILLION":
            raise Exception("File not empty and not a msq file")

        # seek to one byte before end of file
        self._file.seek(-1, 2)

        # ensure that last byte is 0xFF
        if self._file.read(1) != b'\xFF':
            raise Exception("Cannot append. File not properly terminated with 0xFF")

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self._file.close()

    def _write_header(self):
        # seek to beginning
        self._file.seek(0, 0)

        self._file.write(b'MILLION')
        self._file.write(bytes([1, self._width, self._height, self._frame_rate, 255]))

    def append(self, frame: MillionFrame):
        if frame.height != self._height or frame.width != self._width:
            raise Exception("Dimension mismatch")

        # Write the data
        self._file.write(frame.raw_data)
        # Write the terminating 0xFF
        self._file.write(b'\xFF')

    def close(self):
        self._file.close()
