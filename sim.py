import tkinter as tk
from tkinter.filedialog import askopenfile
from clock import Clock
import msq

DIMENSIONS = (24, 12)


class Simulator(tk.Frame):
    def __init__(self, parent):
        super(Simulator, self).__init__(parent)

        # create empty matrix for the clocks
        self._clocks = [[0 for x in range(DIMENSIONS[1])] for y in range(DIMENSIONS[0])]

        # instantiate the clocks
        for i in range(DIMENSIONS[0]):
            for j in range(DIMENSIONS[1]):
                self._clocks[i][j] = Clock(self)
                self._clocks[i][j].grid(row=j, column=i)

        def _simulation_step(msq_reader: msq.MsqReader):
            # read next frame from file
            frame = msq_reader.next_frame()

            # check if frame is valid
            if frame is not None:
                for x in range(DIMENSIONS[0]):
                    for y in range(DIMENSIONS[1]):
                        self._clocks[i][j].set_hand_a(frame.get_at_position(x, y, 1)/200.0)
                        self._clocks[i][j].set_hand_b(frame.get_at_position(x, y, 2)/200.0)



def main():

    # init Tkinter
    root = tk.Tk()

    # create buttons
    button_container = tk.Frame(root)
    button_container.pack(side=tk.TOP, fill=tk.BOTH, expand=True)
    open_button = tk.Button(master=button_container, text="Open", command=open_file)

    open_button.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
    play_button = tk.Button(master=button_container, text=u"\u25B6" + " Play")
    play_button.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

    # create simulator
    simulator = Simulator(root)
    simulator.pack(side=tk.TOP, fill=tk.BOTH, expand=True)

    root.geometry('820x450+300+300')

    root.mainloop()


def open_file():
    filename = askopenfile(filetypes=[("Million Sequence files", "*.msq")])




if __name__ == '__main__':
    main()
