# from tkinter import *
import tkinter as tk
from compress_module import compress, decompress
from tkinter import filedialog


def open_file():
    filename = filedialog.askopenfilename(
        initialdir='/', title="Select a file to compress")
    return filename


def compression(i, o):
    compress(i, o)


def decompression(i, o):
    decompress(i, o)


Window = tk.Tk()

Window.title("Compression Engine")
Window.geometry("600x400")

# input_entry = tk.Entry(Window)
# output_entry = tk.Entry(Window)

# input_entry1 = tk.Entry(Window)
# output_entry1 = tk.Entry(Window)

# input_label = tk.Label(Window, text="File to be compressed")
# output_label = tk.Label(Window, text="Name of compressed file")
# input_label1 = tk.Label(Window, text="File to be Decompressed")
# output_label1 = tk.Label(Window, text="Name of Decompressed file")

# compress_button = tk.Button(Window, text="Compress", command=lambda: compression(
#     input_entry.get(), output_entry.get()))
# lambda fetch real time values from the field

compress_button = tk.Button(Window, text="Compress", command=lambda: compression(
    open_file(), "compressed_Output1.txt"))


decompress_button = tk.Button(Window, text="Decompress", command=lambda: decompression(
    open_file(), "decompressed_Output1.txt"))

# input_label.grid(row=0, column=0)
# input_entry.grid(row=0, column=1)
# output_label.grid(row=1, column=0)
# output_entry.grid(row=1, column=1)
# input_label1.grid(row=3, column=0)
# input_entry1.grid(row=3, column=1)
# output_label1.grid(row=4, column=0)
# output_entry1.grid(row=4, column=1)

compress_button.grid(row=2, column=1)
decompress_button.grid(row=5, column=1)

Window.mainloop()
