import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import (FigureCanvasTkAgg, NavigationToolbar2Tk)
from matplotlib.figure import Figure
import numpy as np
from tkinter import *
# import Bluetooth as bt
data = []
 
def start_plot():
    # print(f"pl:{bluetooth.packet_loss}")
    global data
    # value = bluetooth.listen()
    # print(f"Received {value} is type of {type(value)}. Packet loss: {bluetooth.packet_loss}")
    value = np.random.uniform(0, 5)
    data.append(value)
    ax.clear()  # Clear the plot
    # data.append(np.random.uniform(0, 5))
    ax.plot(data, color="blue")
 
    # Set the plot properties again after clearing
    ax.set_title("Electrocadiogram")
    ax.set_xlabel("Time(Sec)")
    ax.set_ylabel("Ressistance(Ω)")
    ax.set_xlim(0, 200)
    ax.set_ylim(min(data)-10000, max(data)+10000)
    ax.grid(visible=True, which='major', color='#666666', linestyle='-')
    ax.minorticks_on()
    canvas.draw_idle()
    main_window.after(100, start_plot) # in milliseconds, 1000 for 1 second
    if len(data) > 200:
        data.pop(0)
 
def on_close():
    main_window.destroy()
    # bluetooth.s.close()
 
def close_window():
    main_window.destroy()
    # bluetooth.s.close()
 
def clearData():
    global data
    data = []
    ax.clear()
    ax.set_title("Electrocadiogram")
    ax.set_xlabel("Time(Sec)")
    ax.set_ylabel("Ressistance(Ω)")
    ax.set_xlim(0, 200)
    ax.set_ylim(50000, 250000)
    ax.grid(visible=True, which='major', color='#666666', linestyle='-')
    ax.minorticks_on()
    canvas.draw_idle()
 
# Create Bluetooth object
# bluetooth = bt.Bluetooth()
 
 
# Create main window
main_window = Tk()
main_window.configure(background='light blue')
main_window.title("ECG-LArdmon")
main_window.geometry('830x700')
main_window.resizable(width=False, height=False)
 
# Create frames
plotting_frame = LabelFrame(main_window, text='Real Time', bg='white', width=300, height=440, bd=5, relief=SUNKEN)
controls_frame = LabelFrame(main_window, text='Controls', background='light grey', height=150)
 
# Pack frames
controls_frame.pack(fill='both', expand='1', side=TOP, padx=20, pady=10)
plotting_frame.pack(fill='both', expand='yes', side=BOTTOM, padx=20 , pady=10)
 
# Create buttons
start_button = Button(controls_frame, text='Start Monitoring', width=16, height=2, borderwidth=3, command=start_plot)
exit_button = Button(controls_frame, text='Close', width=10, height=2, borderwidth=3, command=main_window.destroy)
clear_button = Button(controls_frame, text='Clear', width=10, height=2, borderwidth=3, command=clearData)
 
# Pack buttons
start_button.pack(side=LEFT, padx=26)
exit_button.pack(side=RIGHT, padx=26)
clear_button.pack(side=RIGHT, padx=26)
 
# Create figure and axis
fig = Figure()
ax = fig.add_subplot(111)
 
# Set plot properties
ax.set_title("Polygraph")
ax.set_xlabel("Time(Sec)")
ax.set_ylabel("Ressistance(Ω)")
ax.set_xlim(0, 200)
ax.set_ylim(50000, 250000)
ax.grid(visible=True, which='major', color='#666666', linestyle='-')
ax.minorticks_on()
ax.grid(visible=True, which='minor', color='#666666', linestyle='-', alpha=0.2)
 
canvas = FigureCanvasTkAgg(fig, master=plotting_frame)
canvas.get_tk_widget().place(x = 0, y = 0, width = 720, height = 500)
canvas.draw()
 
main_window.protocol("WM_DELETE_WINDOW", on_close)
 
main_window.mainloop()