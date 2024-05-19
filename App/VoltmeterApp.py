import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import (FigureCanvasTkAgg, NavigationToolbar2Tk)
from matplotlib.figure import Figure
import numpy as np
from tkinter import *


class VoltmeterApp():
    def __init__(self, communication):
        self._data = []
        self.communication = communication
        self.create_main_window()
        self.create_frames()
        self.pack_frames()
        self.create_buttons()
        self.pack_buttons()
        self.create_figure_and_axis()
        self.set_plot_properties()
        self.create_canvas()
        self.main_window.protocol("WM_DELETE_WINDOW", self.on_close)
        self.main_window.mainloop()

    def create_main_window(self):
        self.main_window = Tk()
        self.main_window.configure(background='light blue')
        self.main_window.title("Voltmeter")
        self.main_window.geometry('830x700')
        self.main_window.resizable(width=False, height=False)

    def create_frames(self):
        self.plotting_frame = LabelFrame(self.main_window, text='Real Time', bg='white', width=300, height=440, bd=5, relief=SUNKEN)
        self.controls_frame = LabelFrame(self.main_window, text='Controls', background='light grey', height=150)
 
    def create_buttons(self):
        self.start_button = Button(self.controls_frame, text='Start Monitoring', width=16, height=2, borderwidth=3, command=self.start_plot)
        self.exit_button = Button(self.controls_frame, text='Close', width=10, height=2, borderwidth=3, command=self.main_window.destroy)
        self.clear_button = Button(self.controls_frame, text='Clear', width=10, height=2, borderwidth=3, command=self.clearData)

    def create_figure_and_axis(self):
        self.fig = Figure()
        self.ax = self.fig.add_subplot(111)
 
    def pack_frames(self):
        self.controls_frame.pack(fill='both', expand='1', side=TOP, padx=20, pady=10)
        self.plotting_frame.pack(fill='both', expand='yes', side=BOTTOM, padx=20 , pady=10)

    def pack_buttons(self):
        self.start_button.pack(side=LEFT, padx=26)
        self.exit_button.pack(side=RIGHT, padx=26)
        self.clear_button.pack(side=RIGHT, padx=26)
 
    def set_plot_properties(self):
        self.ax.set_title("Polygraph")
        self.ax.set_xlabel("Time(Sec)")
        self.ax.set_ylabel("Ressistance(Ω)")
        self.ax.set_xlim(0, 200)
        self.ax.set_ylim(50000, 250000)
        self.ax.grid(visible=True, which='major', color='#666666', linestyle='-', alpha=0.2)
        self.ax.minorticks_on()

    def create_canvas(self):
        self.canvas = FigureCanvasTkAgg(self.fig, master=self.plotting_frame)
        self.canvas.get_tk_widget().place(x = 0, y = 0, width = 720, height = 500)
        self.canvas.draw()


    def set_communication_commands(self, start_function, stop_function, read_function, write_function):
        self.communication.start = start_function
        self.communication.stop = stop_function
        self.communication.read = read_function
        self.communication.write = write_function
        

    def start_plot(self):
        value = self.communication.read()
        self._data.append(value)
        self.ax.clear()  # Clear the plot
        self.ax.plot(self._data, color="blue")
    
        # Set the plot properties again after clearing
        self.ax.set_title("Voltmeter")
        self.ax.set_xlabel("Time(Sec)")
        self.ax.set_ylabel("Voltage(V)")
        self.ax.set_xlim(0, 200)
        self.ax.set_ylim(min(self._data)-10000, max(self._data)+10000)
        self.ax.grid(visible=True, which='major', color='#666666', linestyle='-')
        self.ax.minorticks_on()
        self.canvas.draw_idle()
        self.main_window.after(100, self.start_plot) # in milliseconds, 1000 for 1 second
        if len(self._data) > 200:
            self._data.pop(0)

    def on_close(self):
        self.main_window.destroy()
        self.communication.stop()
    
    def close_window(self):
        self.main_window.destroy()
        self.communication.stop()

    def clearData(self):
        self._data = []
        self.ax.clear()
        self.ax.set_title("Voltmeter")
        self.ax.set_xlabel("Time(Sec)")
        self.ax.set_ylabel("Ressistance(Ω)")
        self.ax.set_xlim(0, 200)
        self.ax.set_ylim(50000, 250000)
        self.ax.grid(visible=True, which='major', color='#666666', linestyle='-')
        self.ax.minorticks_on()
        self.canvas.draw_idle()
