from tkinter import *
import os

# Initialising main window
root = Tk()
# Adding title to main window
root.title('MSE659A Python Project')

window_frame = LabelFrame(root, borderwidth=3, relief="groove", padx=23)


title_frame = Frame(window_frame);
title_frame.pack()

title_label = Label(title_frame, text="Simulation of  sedimentation technique with varying particle sizes under ideal conditions");
title_label.pack();

window_frame.pack()


# Starting infinite loop
root.mainloop()