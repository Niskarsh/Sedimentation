from tkinter import *
import os

# Initialising main window
root = Tk()
root.resizable(0, 0)

global speedEntry, distanceEntry, materialDensity, mediumDensity, time, s_label, d_label

speedEntry, distanceEntry, time, materialDensity, mediumDensity = 1, 0, 0, 0, 0

# Adding title to main window
root.title('MSE659A Python Project')

# Main frame holding everything together
window_frame = LabelFrame(root, borderwidth=3, relief="groove")

# Frame that holds title
title_frame = Frame(window_frame)
title_label = Label(title_frame, text="Simulation of Sedimentation technique with varying particle sizes under ideal conditions")
title_label.pack()

# Frame holding simulation section of window
simulation_frame = LabelFrame(window_frame, text="Simulation")

# Selected Parameters
sp = Label(simulation_frame, text="Selected Parameters")
s_label = Label(simulation_frame, text="Speed : " + str(speedEntry) + "x", width=15, anchor=W)
d_label = Label(simulation_frame, text="Distance Mapped : " + str(distanceEntry), width=25, anchor=E)
time_passed = Label(simulation_frame, text="Time passed : " + str(time))

sp.grid(row=0, column=0, columnspan=2)
s_label.grid(row=1, column=0, padx=(5, 5), columnspan=1, sticky=W)
d_label.grid(row=1, column=1, padx=(5, 5), columnspan=1, sticky=E)
time_passed.grid(row=2, column=0, padx=5, columnspan=2, sticky=W)

# Frame holding the section that takes input
control_frame = LabelFrame(window_frame, text="Controls")

# Speed Frame
def setSpeed(speed):
	speedEntry = speed
	speedEntry = speedEntry[:-1]
	s_label = Label(simulation_frame, text="Speed : " + str(speedEntry) + "x", width=15, anchor=W)
	s_label.grid(row=1, column=0, padx=(5, 5), columnspan=1, sticky=W)

speed_frame = Frame(control_frame)
speed_label = Label(speed_frame, text="Speed: ")
speed = Entry(speed_frame, width=30)
b_speed = Button(speed_frame, text="Set Speed", command=lambda:setSpeed(speed.get()))

speed.insert(0, "eg: 1x")

speed_label.grid(row=0, column=0)
speed.grid(row=0, column=1, sticky=E)
b_speed.grid(row=1, column=1, sticky=E, pady=(5, 0))

speed_frame.grid(row=0, column=0, padx=10, pady=(10, 5), sticky=E)

# Distance Frame
def setMapping(distance):
	distanceEntry = distance
	d_label = Label(simulation_frame, text="Distance Mapped : " + str(distanceEntry), width=25, anchor=E)
	d_label.grid(row=1, column=1, padx=(5, 5), columnspan=1, sticky=E)

distance_frame = Frame(control_frame)
distance_label = Label(distance_frame, text="Distance to be mapped: ")
distance = Entry(distance_frame, width=30)
b_distance = Button(distance_frame, text="Map Distance", command=lambda:setMapping(distance.get()))

# distance.insert(0, "eg: 1x")

distance_label.grid(row=0, column=0)
distance.grid(row=0, column=1)
b_distance.grid(row=1, column=1, sticky=E, pady=(5, 0))

distance_frame.grid(row=1, column=0, padx=10, pady=(5, 10), sticky=E)

# Material Density Frame
def setMaterialDensity(density):
	materialDensity = density
	
materialDensity_frame = Frame(control_frame)
materialDensity_label = Label(materialDensity_frame, text="Material Density: ")
materialDensity = Entry(materialDensity_frame, width=30)
b_materialDensity = Button(materialDensity_frame, text="Set Density", command=lambda:setMaterialDensity(materialDensity.get()))

# materialDensity.insert(0, "eg: 1x")

materialDensity_label.grid(row=0, column=0)
materialDensity.grid(row=0, column=1)
b_materialDensity.grid(row=1, column=1, sticky=E, pady=(5, 0))

materialDensity_frame.grid(row=2, column=0, padx=10, pady=(5, 10), sticky=E)

# Medium Density Frame
def setMediumDensity(density):
	mediumDensity = density
	
mediumDensity_frame = Frame(control_frame)
mediumDensity_label = Label(mediumDensity_frame, text="Medium Density: ")
mediumDensity = Entry(mediumDensity_frame, width=30)
b_mediumDensity = Button(mediumDensity_frame, text="Set Density", command=lambda:setMediumDensity(mediumDensity.get()))

# mediumDensity.insert(0, "eg: 1x")

mediumDensity_label.grid(row=0, column=0)
mediumDensity.grid(row=0, column=1)
b_mediumDensity.grid(row=1, column=1, sticky=E, pady=(5, 0))

mediumDensity_frame.grid(row=3, column=0, padx=10, pady=(5, 10), sticky=E)

# Medium Viscosity Frame
def setMediumViscosity(viscosity):
	mediumViscosity = viscosity
	
mediumViscosity_frame = Frame(control_frame)
mediumViscosity_label = Label(mediumViscosity_frame, text="Medium Viscosity: ")
mediumViscosity = Entry(mediumViscosity_frame, width=30)
b_mediumViscosity = Button(mediumViscosity_frame, text="Set Viscosity", command=lambda:setMediumViscosity(mediumViscosity.get()))

# mediumViscosity.insert(0, "eg: 1x")

mediumViscosity_label.grid(row=0, column=0)
mediumViscosity.grid(row=0, column=1)
b_mediumViscosity.grid(row=1, column=1, sticky=E, pady=(5, 0))

mediumViscosity_frame.grid(row=4, column=0, padx=10, pady=(5, 10), sticky=E)

# Packing component frames in window
title_frame.grid(row=0, column=0, columnspan=2, pady=(10, 5))
simulation_frame.grid(row=1, column=0, padx=(10, 5), pady=(5, 10), sticky=N+S)
control_frame.grid(row=1, column=1, padx=(5, 10), pady=(5, 10))

# Packing main frame in window
window_frame.pack(padx=5, pady=5)

# Starting infinite loop
root.mainloop()