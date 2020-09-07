## Filename: main.py

import random
from collections import deque

from kivymd.uix.boxlayout import MDBoxLayout
from matplotlib import style, animation
from matplotlib import pyplot as plt
from matplotlib import use as mpl_use
from kivy.clock import Clock
import numpy as np


mpl_use('module://kivy.garden.matplotlib.backend_kivy')
style.use('dark_background')


class PressureChart(MDBoxLayout):
    POINTS = 100

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        self.fig, ax1 = plt.subplots()
        self.xdata = np.linspace(-30, 0, self.POINTS)
        self.ydata = deque([0] * self.POINTS, maxlen=self.POINTS)
        self.fig = plt.figure()
        self.ax1 = self.fig.add_subplot(1, 1, 1)
        self.line, = self.ax1.plot(self.xdata, self.ydata, 'r-', linewidth=1.0)
        plt.grid(True)
        self.on_data()

    def on_data(self, *args):
        self.ax1.set_title('Pressure in cmH20')
        self.ax1.set_xlabel('units')
        self.ax1.set_ylabel('Pressure (cmH20)')
        self.mpl_canvas = self.fig.canvas
        self.mpl_canvas.draw_idle()
        self.add_widget(self.mpl_canvas)
        Clock.schedule_interval(self.update, 1/25)
    def update(self, *args):
        self.ydata.extend(self.get_data())
        self.line.set_ydata(self.ydata)
        plt.ylim(min(self.ydata), max(self.ydata))
        self.mpl_canvas.draw_idle()

    def get_data(self):
        '''the function that gets and returns new data'''
        return [random.randrange(100) for _ in range(random.randint(20, 50))]


class FlowChart(MDBoxLayout):
    POINTS = 100

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        self.fig, ax1 = plt.subplots()
        self.xdata = np.linspace(-30, 0, self.POINTS)
        self.ydata = deque([0] * self.POINTS, maxlen=self.POINTS)
        self.fig = plt.figure()
        self.ax1 = self.fig.add_subplot(1, 1, 1)
        self.line, = self.ax1.plot(self.xdata, self.ydata, 'r-', linewidth=1.0)
        plt.grid(True)
        self.on_data()

    def on_data(self, *args):
        self.ax1.set_title('Flow in I/Minute')
        self.ax1.set_xlabel('units')
        self.ax1.set_ylabel('Volume (I/Minute)')
        self.mpl_canvas = self.fig.canvas
        self.mpl_canvas.draw_idle()
        self.add_widget(self.mpl_canvas)
        Clock.schedule_interval(self.update, 1/25)
    def update(self, *args):
        self.ydata.extend(self.get_data())
        self.line.set_ydata(self.ydata)
        plt.ylim(min(self.ydata), max(self.ydata))
        self.mpl_canvas.draw_idle()

    def get_data(self):
        '''the function that gets and returns new data'''
        return [random.randrange(100) for _ in range(random.randint(20, 50))]


class VolumeChart(MDBoxLayout):
    POINTS = 100

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        self.fig, ax1 = plt.subplots()
        self.xdata = np.linspace(-30, 0, self.POINTS)
        self.ydata = deque([0] * self.POINTS, maxlen=self.POINTS)
        self.fig = plt.figure()
        self.ax1 = self.fig.add_subplot(1, 1, 1)
        self.line, = self.ax1.plot(self.xdata, self.ydata, 'r-', linewidth=1.0)
        plt.grid(True)
        self.on_data()

    def on_data(self, *args):
        self.ax1.set_title('Volume in milliliters')
        self.ax1.set_xlabel('units')
        self.ax1.set_ylabel('Volume (ml)')
        self.mpl_canvas = self.fig.canvas
        self.mpl_canvas.draw_idle()
        self.add_widget(self.mpl_canvas)
        Clock.schedule_interval(self.update, 1/25)
    def update(self, *args):
        self.ydata.extend(self.get_data())
        self.line.set_ydata(self.ydata)
        plt.ylim(min(self.ydata), max(self.ydata))
        self.mpl_canvas.draw_idle()

    def get_data(self):
        '''the function that gets and returns new data'''
        return [random.randrange(100) for _ in range(random.randint(20, 50))]

class Chart(MDBoxLayout):
    POINTS = 100

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        self.fig, (self.ax1, self.ax2, self.ax3) = plt.subplots(3)
        # The first sub plot
        self.x1data = np.linspace(-30, 0, self.POINTS)
        self.y1data = deque([0] * self.POINTS, maxlen=self.POINTS)
        self.line1, = self.ax1.plot(self.x1data, self.y1data, 'r-', linewidth=1.0)
        # The second sub plot
        self.x2data = np.linspace(-30, 0, self.POINTS)
        self.y2data = deque([0] * self.POINTS, maxlen=self.POINTS)
        self.line2, = self.ax2.plot(self.x2data, self.y2data, 'r-', linewidth=1.0)
        # The third sub plot
        self.x3data = np.linspace(-30, 0, self.POINTS)
        self.y3data = deque([0] * self.POINTS, maxlen=self.POINTS)
        self.line3, = self.ax3.plot(self.x3data, self.y3data, 'r-', linewidth=1.0)
        self.fig.suptitle('Graphical Visualization')

        plt.grid(True)
        self.on_data()

    def on_data(self, *args):
        self.ax1.set_title('Pressure in cmH20')
        self.ax1.set_xlabel('units')
        self.ax1.set_ylabel('Pressure (cmH20)')
        self.ax2.set_title('Flow in I/Minute')
        self.ax2.set_xlabel('units')
        self.ax2.set_ylabel('Flow (I/Minute)')
        self.ax3.set_title('Volume in milliliters')
        self.ax3.set_xlabel('units')
        self.ax3.set_ylabel('Volume (ml)')
        self.mpl_canvas = self.fig.canvas
        self.mpl_canvas.draw_idle()
        self.add_widget(self.mpl_canvas)
        Clock.schedule_interval(self.update, 1/25)
    def update(self, *args):
        self.y1data.extend(self.get_data())
        self.line1.set_ydata(self.y1data)
        self.y2data.extend(self.get_data())
        self.line2.set_ydata(self.y2data)
        self.y3data.extend(self.get_data())
        self.line3.set_ydata(self.y3data)
        plt.ylim(min(self.y1data), max(self.y1data))
        self.mpl_canvas.draw_idle()

    def get_data(self):
        '''the function that gets and returns new data'''
        return [random.randrange(100) for _ in range(random.randint(20, 50))]
