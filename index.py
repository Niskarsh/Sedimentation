from tkinter import *
import time as tm

# Initialising main window
root = Tk()
root.resizable(0, 0)

global speedEntry, distanceEntry, materialDensity, mediumDensity, mediumViscosity, time, s_label, d_label, start_button, pause_button, stop_button 

speedEntry, distanceEntry, time, materialDensity, mediumDensity, mediumViscosity = 1, 0, 0, 0, 0, 0

run=False

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
mt_label = Label(simulation_frame, text="Material Density : " + str(materialDensity), width=25, anchor=W)
md_label = Label(simulation_frame, text="Medium Density : " + str(mediumDensity), width=25, anchor=E)
v_label = Label(simulation_frame, text="Medium Viscosity : " + str(mediumViscosity), width=25, anchor=W)
time_passed = Label(simulation_frame, text="Time passed : " + str(time))

def drawCanvas(canvas):
	global m1
	canvas.create_rectangle(125, 264, 290, 30, width=3, outline="#3c5396", fill="#b8c9fc")
	m1 = canvas.create_oval(128, 33, 138, 43, fill="red")	

canvas = Canvas(simulation_frame, bg="white")
drawCanvas(canvas)

sp.grid(row=0, column=0, columnspan=2)
s_label.grid(row=1, column=0, padx=(5, 5), columnspan=1, sticky=W)
d_label.grid(row=1, column=1, padx=(5, 5), columnspan=1, sticky=E)
mt_label.grid(row=2, column=0, padx=(5, 5), pady=(5, 0), columnspan=1, sticky=W)
md_label.grid(row=2, column=1, padx=(5, 5), pady=(5, 0), columnspan=1, sticky=E)
v_label.grid(row=3, column=0, padx=(5, 5), pady=(5, 0), columnspan=1, sticky=W)
time_passed.grid(row=4, column=0, padx=5, pady=(5, 0), columnspan=2, sticky=W)
canvas.grid(row=5, column=0, padx=5, pady=(5, 0), columnspan=2, sticky=W+E)
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
	mt_label = Label(simulation_frame, text="Material Density : " + str(materialDensity), width=25, anchor=W)
	mt_label.grid(row=2, column=0, padx=(5, 5), pady=(5, 0), columnspan=1, sticky=W)
	
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
	md_label = Label(simulation_frame, text="Medium Density : " + str(mediumDensity), width=25, anchor=E)
	md_label.grid(row=2, column=1, padx=(5, 5), pady=(5, 0), columnspan=1, sticky=E)

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
	v_label = Label(simulation_frame, text="Medium Viscosity : " + str(mediumViscosity), width=25, anchor=W)
	v_label.grid(row=3, column=0, padx=(5, 5), pady=(5, 0), columnspan=1, sticky=W)
	
mediumViscosity_frame = Frame(control_frame)
mediumViscosity_label = Label(mediumViscosity_frame, text="Medium Viscosity: ")
mediumViscosity = Entry(mediumViscosity_frame, width=30)
b_mediumViscosity = Button(mediumViscosity_frame, text="Set Viscosity", command=lambda:setMediumViscosity(mediumViscosity.get()))

# mediumViscosity.insert(0, "eg: 1x")

mediumViscosity_label.grid(row=0, column=0)
mediumViscosity.grid(row=0, column=1)
b_mediumViscosity.grid(row=1, column=1, sticky=E, pady=(5, 0))

mediumViscosity_frame.grid(row=4, column=0, padx=10, pady=(5, 10), sticky=E)

# Buttons

control_buttons_frame = Frame(control_frame)

def startSimulation():
	root.update()
	global run, time, time_passed, canvas, m1
	run=True
	while(run):
		time = time + .1
		canvas.move(m1, 0, 1)
		t = str(time)
		time_passed.grid_forget()
		time_passed = Label(simulation_frame, text="Time passed : " + str(t[0:t.index(".")+1]+t[t.index(".")+1:t.index(".")+2]))
		time_passed.grid(row=4, column=0, padx=5, pady=(5, 0), columnspan=2, sticky=W)
		root.update()
		tm.sleep(.1)



def start():
	global start_button
	start_button.grid_forget()
	start_button = Button(control_buttons_frame, text="Start", command=start, state=DISABLED)
	pause_button = Button(control_buttons_frame, text="Pause", command=pause, state=NORMAL)
	stop_button = Button(control_buttons_frame, text="Stop", command=stop, state=NORMAL)
	
	start_button.grid(row=0, column=0)
	pause_button.grid(row=0, column=1)
	stop_button.grid(row=0, column=2)
	
	startSimulation()

def pause():
	global run, start_button
	start_button.grid_forget()
	start_button = Button(control_buttons_frame, text="Resume", command=start, state=NORMAL)
	pause_button = Button(control_buttons_frame, text="Pause", command=pause, state=DISABLED)
	stop_button = Button(control_buttons_frame, text="Stop", command=stop, state=NORMAL)
	
	start_button.grid(row=0, column=0)
	pause_button.grid(row=0, column=1)
	stop_button.grid(row=0, column=2)
	run=False

def stop():
	global run, time, start_button, time_passed, canvas
	start_button.grid_forget()
	start_button = Button(control_buttons_frame, text="Start", command=start, state=NORMAL)
	pause_button = Button(control_buttons_frame, text="Pause", command=pause, state=DISABLED)
	stop_button = Button(control_buttons_frame, text="Stop", command=stop, state=DISABLED)
	
	start_button.grid(row=0, column=0)
	pause_button.grid(row=0, column=1)
	stop_button.grid(row=0, column=2)
	run=False
	time=0
	time_passed.grid_forget()
	time_passed = Label(simulation_frame, text="Time passed : " + str(time))
	time_passed.grid(row=4, column=0, padx=5, pady=(5, 0), columnspan=2, sticky=W)

	canvas = Canvas(simulation_frame, bg="white")
	drawCanvas(canvas)
	canvas.grid(row=5, column=0, padx=5, pady=(5, 0), columnspan=2, sticky=W+E)

start_button = Button(control_buttons_frame, text="Start",  state=NORMAL, command=start)
pause_button = Button(control_buttons_frame, text="Pause", state=DISABLED, command=pause)
stop_button = Button(control_buttons_frame, text="Stop", state=DISABLED, command=stop)

start_button.grid(row=0, column=0)
pause_button.grid(row=0, column=1)
stop_button.grid(row=0, column=2)

control_buttons_frame.grid(row=5, column=0, padx=10, pady=(5, 10))



# Packing component frames in window
title_frame.grid(row=0, column=0, columnspan=2, pady=(10, 5))
simulation_frame.grid(row=1, column=0, padx=(10, 5), pady=(5, 10), sticky=N+S)
control_frame.grid(row=1, column=1, padx=(5, 10), pady=(5, 10))

# Packing main frame in window
window_frame.pack(padx=5, pady=5)

# Starting infinite loop
root.mainloop()