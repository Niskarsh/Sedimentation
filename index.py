from tkinter import *
import os

# Initialising main window
root = Tk()
root.resizable(0,0)

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

# Speed Frame
speed_frame = Frame(control_frame)
speed_label = Label(speed_frame, text="Speed: ")
speed = Entry(speed_frame, width=30)
b_speed = Button(speed_frame, text="Set Speed")

speed.insert(0, "eg: 1x")

speed_label.grid(row=0, column=0)
speed.grid(row=0, column=1, sticky=E)
b_speed.grid(row=1, column=1, sticky=E, pady=(5,0))

speed_frame.grid(row=0, column=0, padx=10, pady=(10,5), sticky=E)

# Distance Frame
distance_frame = Frame(control_frame)
distance_label = Label(distance_frame, text="Distance to be mapped: ")
distance = Entry(distance_frame, width=30)
b_distance = Button(distance_frame, text="Map Distance")

# distance.insert(0, "eg: 1x")

distance_label.grid(row=0, column=0)
distance.grid(row=0, column=1)
b_distance.grid(row=1, column=1, sticky=E, pady=(5,0))

distance_frame.grid(row=1, column=0, padx=10, pady=(5,10))

# Packing component frames in window
title_frame.grid(row=0, column=0, columnspan=2, pady=(10,5))
simulation_frame.grid(row=1, column=0, padx=(10,5), pady=(5,10))
control_frame.grid(row=1, column=1, padx=(5,10), pady=(5,10))

# Packing main frame in window
window_frame.pack(padx=5, pady=5)

# Starting infinite loop
root.mainloop()