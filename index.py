from tkinter import *
import os

# Initialising main window
root = Tk()
# Adding title to main window
root.title('MSE659A Python Project')

# Main frame holding everything together
window_frame = LabelFrame(root, borderwidth=3, relief="groove")

# Frame that holds title
title_frame = Frame(window_frame)
title_label = Label(title_frame, text="Simulation of  sedimentation technique with varying particle sizes under ideal conditions")
title_label.pack()

# Frame holding simulation section of window
simulation_frame = LabelFrame(window_frame, text="Simulation")
titl_frame = Frame(simulation_frame)
titl_label = Label(titl_frame, text="Simulation of  sedimentation technique with varying particle sizes under ideal conditions")
titl_label.pack()
titl_frame.pack()
# Frame holding the section that takes input
control_frame = LabelFrame(window_frame, text="Controls")
tit_frame = Frame(control_frame)
tit_label = Label(tit_frame, text="Simulation of  sedimentation technique with varying particle sizes under ideal conditions")
tit_label.pack()
tit_frame.pack()
# Packing component frames in window
title_frame.grid(row=0, column=0, columnspan=2, pady=(10,5))
simulation_frame.grid(row=1, column=0, padx=(10,5), pady=(5,10))
control_frame.grid(row=1, column=1, padx=(5,10), pady=(5,10))

# Packing main frame in window
window_frame.pack(padx=5, pady=5)

# Starting infinite loop
root.mainloop()