from tkinter import *
from tkinter import messagebox
from colour import Color
import time as tm

# Initialising main window
root = Tk()
root.resizable(0, 0)

global speedEntry, distanceEntry, materialDensityEntry, mediumDensityEntry, mediumViscosityEntry, time, s_label, d_label, start_button, pause_button, stop_button 

speedEntry, distanceEntry, time, materialDensityEntry, mediumDensityEntry, mediumViscosityEntry, distanceMapParameter = 1, 328.0, 0.0, 0.0, 0.0, 0.0, 1.0
sizeRange = [0.0, 0.0]

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
mt_label = Label(simulation_frame, text="Material Density : " + str(materialDensityEntry), width=25, anchor=W)
md_label = Label(simulation_frame, text="Medium Density : " + str(mediumDensityEntry), width=25, anchor=E)
v_label = Label(simulation_frame, text="Medium Viscosity : " + str(mediumViscosityEntry), width=25, anchor=W)
sz_label = Label(simulation_frame, text="Size range : " + str(sizeRange[0])+ "μ to " + str(sizeRange[len(sizeRange)-1]) + "μ", width=25, anchor=E)
time_passed = Label(simulation_frame, text="Time passed : " + str(time))

def drawCanvas(canvas):
	global m1, m
	canvas.create_rectangle(125, 358, 290, 30, width=3, outline="#3c5396", fill="#b8c9fc")
	# m1 = canvas.create_oval(128, 33, 138, 43, fill="red")
	# (m1, a, v, reached, x1, y1, x2, y2, fill)
	# m = [(m1, 0.0, 0.0, sizeRange[0], False, 128, 33, 138, 43, "red")]

canvas = Canvas(simulation_frame, bg="white", height=360)
drawCanvas(canvas)

sp.grid(row=0, column=0, columnspan=2)
s_label.grid(row=1, column=0, padx=(5, 5), columnspan=1, sticky=W)
d_label.grid(row=1, column=1, padx=(5, 5), columnspan=1, sticky=E)
mt_label.grid(row=2, column=0, padx=(5, 5), pady=(5, 0), columnspan=1, sticky=W)
md_label.grid(row=2, column=1, padx=(5, 5), pady=(5, 0), columnspan=1, sticky=E)
v_label.grid(row=3, column=0, padx=(5, 5), pady=(5, 0), columnspan=1, sticky=W)
sz_label.grid(row=3, column=1, padx=(5, 5), pady=(5, 0), columnspan=1, sticky=E)
time_passed.grid(row=4, column=0, padx=5, pady=(5, 0), columnspan=2, sticky=W)
canvas.grid(row=5, column=0, rowspan=2, padx=5, pady=(5, 0), columnspan=2, sticky=W+E)
# Frame holding the section that takes input
control_frame = LabelFrame(window_frame, text="Controls")

# Speed Frame
def setSpeed(speed):
	global speedEntry
	speedEntry = speed
	speedEntry = speedEntry[:-1]
	s_label = Label(simulation_frame, text="Speed : " + str(speedEntry) + "x", width=15, anchor=W)
	s_label.grid(row=1, column=0, padx=(5, 5), columnspan=1, sticky=W)

speed_frame = Frame(control_frame)
speed_label = Label(speed_frame, text="Speed: ")
speed = Entry(speed_frame, width=30)
b_speed = Button(speed_frame, text="Set Speed", command=lambda:setSpeed(speed.get()), state=DISABLED)

speed.insert(0, "1x")

speed_label.grid(row=0, column=0)
speed.grid(row=0, column=1, sticky=E)
b_speed.grid(row=1, column=1, sticky=E, pady=(5, 0))

speed_frame.grid(row=0, column=0, padx=10, pady=(10, 5), sticky=E)

# Distance Frame
def setMapping(distance):
	global distanceEntry, distanceMapParameter
	distanceEntry = float(distance)
	distanceMapParameter = 328/distanceEntry
	d_label = Label(simulation_frame, text="Distance Mapped : " + str(distanceEntry), width=25, anchor=E)
	d_label.grid(row=1, column=1, padx=(5, 5), columnspan=1, sticky=E)

distance_frame = Frame(control_frame)
distance_label = Label(distance_frame, text="Distance to be mapped: ")
distance = Entry(distance_frame, width=30)
b_distance = Button(distance_frame, text="Map Distance", command=lambda:setMapping(distance.get()))

distance.insert(0, "Default mapping: 328m to 328px")

distance_label.grid(row=0, column=0)
distance.grid(row=0, column=1)
b_distance.grid(row=1, column=1, sticky=E, pady=(5, 0))

distance_frame.grid(row=1, column=0, padx=10, pady=(5, 10), sticky=E)

# Material Density Frame
def setMaterialDensity(density):
	global materialDensityEntry
	materialDensityEntry = float(density)
	mt_label = Label(simulation_frame, text="Material Density : " + str(materialDensityEntry), width=25, anchor=W)
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
	global mediumDensityEntry
	mediumDensityEntry = float(density)
	md_label = Label(simulation_frame, text="Medium Density : " + str(mediumDensityEntry), width=25, anchor=E)
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
	global mediumViscosityEntry
	mediumViscosityEntry = float(viscosity)
	v_label = Label(simulation_frame, text="Medium Viscosity : " + str(mediumViscosityEntry), width=25, anchor=W)
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

# Particle size range Frame
def setSizeRange(r1, r2):
	global sizeRange, m, canvas
	r1, r2 = float(r1), float(r2)
	
	blue = Color("#fffac7")
	colors = list(blue.range_to(Color("#c75300"),16))
	
	sizeRange = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
	m = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
	for i in range(16):
		sizeRange[i] = r1 + (i)*(r2-r1)/15
		ml = canvas.create_oval(128+10*i, 33, 138+10*i, 43, fill=colors[i].hex)
		m[i] = (ml, 0.0, 0.0, sizeRange[i], False, False, 128+10*i, 33, 138+10*i, 43, 43, colors[i].hex)

	print(sizeRange)
	# for index, (shape, a, v, size, reached, x1, y1, x2, y2, fill) in enumerate(m):
	# 	m[index] = (shape, a, v, sizeRange[0], reached, x1, y1, x2, y2, fill)
	sz_label = Label(simulation_frame, text="Size range : " + str(sizeRange[0])+ "m to " + str(sizeRange[len(sizeRange)-1]) + "m", width=25, anchor=E)
	sz_label.grid(row=3, column=1, padx=(5, 5), pady=(5, 0), columnspan=1, sticky=E)
	
sizeRange_frame = Frame(control_frame)
sizeRange_label = Label(sizeRange_frame, text="Size Range: ")
sizeRange_label_2 = Label(sizeRange_frame, text=" : ")
sizeRangeInitial = Entry(sizeRange_frame, width=10)
sizeRangeFinal = Entry(sizeRange_frame, width=10)
b_sizeRange = Button(sizeRange_frame, text="Set Size Range", command=lambda:setSizeRange(sizeRangeInitial.get(), sizeRangeFinal.get()))

# mediumViscosity.insert(0, "eg: 1x")

sizeRange_label.grid(row=0, column=0)
sizeRangeInitial.grid(row=0, column=1, sticky=E)
sizeRange_label_2.grid(row=0, column=2, sticky=E)
sizeRangeFinal.grid(row=0, column=3, sticky=E)
b_sizeRange.grid(row=1, column=0, columnspan=4, sticky=E, pady=(5, 0))

sizeRange_frame.grid(row=5, column=0, padx=10, pady=(5, 10), sticky=E)

# Buttons

control_buttons_frame = Frame(control_frame)


def allStopped():
	global m
	stop = True
	for index, (shape, a, v, size, reached, stopped, x1, y1, x2, y2, y, fill) in enumerate(m):
		if not(stopped):
			stop = False

	return stop


def calculateNextMove():
	global time, time_passed, canvas, m1, m, mediumDensityEntry, materialDensityEntry, mediumViscosityEntry, distanceMapParameter
	# m = [(0, 0, False, 128, 33, 138, 43, "red")]
	increment = 0
	if allStopped():
		pause()
		return

	for index, (shape, a, v, size, reached, stopped, x1, y1, x2, y2, y, fill) in enumerate(m):
		if reached:
			increment = v*.1*distanceMapParameter
			if (y + increment > 358):
				increment = 358 - y
				a = 0
				v = 0
				stopped = True
			m[index] = (shape, a, v, size, reached, stopped, x1, y1, x2, y2, y+increment, fill)	
			canvas.move(shape, 0, increment)
			print("acc "+str(a)+" vel "+ str(v))
		else:
			a  = 9.8 - ((9.8*mediumDensityEntry)/materialDensityEntry) - ((18*v*mediumViscosityEntry)/(materialDensityEntry*size*size))
			if a>0:
				v = v + a*.1
				increment = v*.1*distanceMapParameter
				if (y + increment > 358):
					increment = 358 - y
					a = 0
					v = 0
					stopped = True
				m[index] = (shape, a, v, size, reached, stopped, x1, y1, x2, y2, y+increment, fill)
				canvas.move(shape, 0, increment)
				print("acc "+str(a)+" vel "+ str(v))
			else:
				increment = v*.1*distanceMapParameter
				if (y + increment > 358):
					increment = 358 - y
					a = 0
					v = 0
					stopped = True
				m[index] = (shape, a, v, size, True, stopped, x1, y1, x2, y2, y+increment, fill)
				canvas.move(shape, 0, increment)
				print("Reached "+str(reached)+ " vel "+ str(v))


def startSimulation():
	root.update()
	global run, time, time_passed, canvas, m1
	run=True
	while(run):
		time = time + .1
		calculateNextMove()
		# canvas.move(m1, 0, 1)
		t = str(time)
		time_passed.grid_forget()
		time_passed = Label(simulation_frame, text="Time passed : " + str(t[0:t.index(".")+1]+t[t.index(".")+1:t.index(".")+2]))
		time_passed.grid(row=4, column=0, padx=5, pady=(5, 0), columnspan=2, sticky=W)
		root.update()
		tm.sleep(.1)



def start():
	global start_button, materialDensityEntry, mediumDensityEntry, mediumViscosityEntry, sizeRange, distanceEntry
	# Checks all entries are received or not	 
	if not(distanceEntry and materialDensityEntry and mediumDensityEntry and mediumViscosityEntry and sizeRange[0] and sizeRange[1]):
		messagebox.showerror("Empty Entry", "Please fill all entries and press corresponding set button. Do cross check in Selected Parameters section on the left")
		return

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

	canvas.grid_forget()
	canvas =  Canvas(simulation_frame, bg="white", height=360)
	drawCanvas(canvas)
	canvas.grid(row=5, column=0, padx=5, pady=(5, 0), columnspan=2, sticky=W+E)

start_button = Button(control_buttons_frame, text="Start",  state=NORMAL, command=start)
pause_button = Button(control_buttons_frame, text="Pause", state=DISABLED, command=pause)
stop_button = Button(control_buttons_frame, text="Stop", state=DISABLED, command=stop)

start_button.grid(row=0, column=0)
pause_button.grid(row=0, column=1)
stop_button.grid(row=0, column=2)

control_buttons_frame.grid(row=6, column=0, padx=10, pady=(5, 10))



# Packing component frames in window
title_frame.grid(row=0, column=0, columnspan=2, pady=(10, 5))
simulation_frame.grid(row=1, column=0, padx=(10, 5), pady=(5, 10), sticky=N+S)
control_frame.grid(row=1, column=1, padx=(5, 10), pady=(5, 10))

# Packing main frame in window
window_frame.pack(padx=5, pady=5)

# Starting infinite loop
root.mainloop()

