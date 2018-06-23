
import matplotlib
matplotlib.use('TkAgg')
import numpy as np
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure
from tkinter import *
import matplotlib.dates as dates
from myframes.categorical_frame import transform_categorical_frame
from myframes.numeric_frame import transform_numeric_frame


import pandas as pd 
import numpy as np
import re
from datetime import datetime
import matplotlib.pyplot as plt
import datetime
from matplotlib import pyplot
from pandas import Series
import matplotlib.figure as mplfig
from matplotlib.figure import Figure 
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

from matplotlib.backends.backend_agg import FigureCanvasAgg
import matplotlib.backends.tkagg as tkagg
import tkinter as tk 
from tkinter import ttk

import matplotlib
matplotlib.use('TkAgg')
import numpy as np
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure
from tkinter import *
import matplotlib.dates as dates
from StaticDataFrame import StaticDataFrame 
    
#plot object superclass
class plot_object_super(object):
    def __init__(self,window ,df_,column_name,grid_list,title  = 'A plot',figsize = (5,5)):
        self.window = window
        self.df = df_
        self.grid_list = grid_list
        self.figsize = figsize
        self.title = title
        self.current_plot = None
        self.canvas = None

        #self.plot(column_name)

    #returns plot object
    def get_plot_object(self):
        if(self.canvas != None):
            return self.canvas
        else:
            return None


#creates a plot data frame
class plot_frame(tk.Frame):
    def __init__(self,parent,df):
        self.parent= parent
        tk.Frame.__init__(self, parent)  
        self.variable = StringVar(self)
        self.current_plot = None
        #self.scrollbar = Scrollbar(self)
        #self.scrollbar.grid(row = 0 , column = 100)

        if(StaticDataFrame.loaded_csv== True):
            df_ = df
            column_list = []
            for column in df:
                column_list.append(column)
            
            self.options = OptionMenu(self, self.variable, *column_list)
            self.options.grid(row = 1, column = 1)
            self.button_plot = Button(self,text= "Plot", command = self.plot_function)
            self.button_plot.grid(row = 10, column = 1 )

    def plot_function(self):
        try:
            if(self.current_plot!=None):
                self.current_plot.destroy()
                                
            #plot thwe selected column from the drop down menu 

            column_selected = self.variable.get()
            label = Label(self,text= "Graph_"+str(column_selected))
            label.grid(row = 15, column = 1)
            #print('PLOT_FUNCTION')
            plt_objct = plot_object(self,StaticDataFrame.df,self.variable.get(),(25,1),'A simple PLot',figsize = (4,5))
            #roll_objct = plot_object(self,StaticDataFrame.df,self.variable.get(),(25,150),'ROlling Mean 2 window ',figsize=(4,5))


            self.current_plot = plt_objct.get_plot_object()
            #if(tkagg_plot_object!=None):
            #    tkagg_plot_object.destroy()

            #canvas.get_tk_widget().pack(side =TOP, fill = BOTH, expand = True)
        except Exception as e:
            print('message___1123')
            tb= e.__traceback__
            print('Traceback'+str(tb))
            exc_type, exc_obj, exc_tb = sys.exc_info()
            print(e.__doc__,str(exc_obj),exc_tb.tb_lineno)

            #print(e.message)      

                

# #creates time series object python
# class plot_object:
#     def __init__(self,  window,df_,column_name,grid_list,title  = 'A plot',figsize = (5,5)):
#         self.window = window
#         self.df = df_
#         self.grid_list = grid_list
#         self.figsize = figsize
#         self.title = title
#         self.current_plot = None
#         self.canvas = None

#         #self.box = Entry(window)
#         #self.button = Button (window, text="check", command=self.plot)
#         #self.box.pack ()
#         self.plot(column_name)
#         #self.button.pack()
    
#     def get_plot_object(self):
#         if(self.canvas != None):
#             return self.canvas
#         else:
#             return None
#     def plot (self,column_name):  
#         #self.remove_plot()

#         try:
            
#             fig = Figure(self.figsize)
#             plt.tight_layout()
#             a = fig.add_subplot(111)
#             self.df.plot( y = column_name,ax= a,title = self.title)

#             #new_x = dates.num2date(df_['date'])
#             #a
#             #lol =1
#             #a.plot(lol1, lol2, color = 'red')
#             #a.plot(p, range(2 +max(x)),color='blue')
           
#             #a.set_title ("Estimation Grid", fontsize=16)
#             #a.set_ylabel("Y", fontsize=14)
#             #a.set_xlabel("X", fontsize=1
#             self.canvas = FigureCanvasTkAgg(fig, master=self.window)
#             self.canvas.get_tk_widget().grid(row = self.grid_list[0], column= self.grid_list[1])
#             self.canvas = self.canvas.get_tk_widget()
            
            
#             #self.canvas.draw()
#         except Exception as e:
#             print('message___1123')
#             exc_type, exc_obj, exc_tb = sys.exc_info()
#             print(e.__doc__,str(exc_obj),exc_tb.tb_lineno)
#             #print(e.message)      
            





#creates time series object python
class plot_object(plot_object_super):
    def __init__(self,  window,df_,column_name,grid_list,title  = 'A plot',figsize = (5,5)):
        super(plot_object, self).__init__(window,df_,column_name,grid_list,title,figsize)

        self.plot(column_name)

    # def get_plot_object(self):
    #     if(self.canvas != None):
    #         return self.canvas
    #     else:
    #         return None

    #plots_stuff    
    def plot(self,column_name):  
        try:
            fig = Figure(self.figsize)
            plt.tight_layout()
            a = fig.add_subplot(111)
            self.df.plot( y = column_name,ax= a,title = self.title)
            
            self.canvas = FigureCanvasTkAgg(fig, master=self.window)
            self.canvas.get_tk_widget().grid(row = self.grid_list[0], column= self.grid_list[1])
            self.canvas = self.canvas.get_tk_widget()
            
        except Exception as e:
            print('message___1123')
            exc_type, exc_obj, exc_tb = sys.exc_info()
            print(e.__doc__,str(exc_obj),exc_tb.tb_lineno)
            #print(e.message)      
            










#rolling plot object in python
class rolling_plot_object:
    def __init__(self,  window,df_,column_name,grid_list,title  = 'A plot',figsize = (5,5)):
        self.window = window
        self.df = df_
        self.grid_list = grid_list
        self.figsize = figsize
        self.title = title
        self.current_plot = None
        self.canvas = None

            
        self.plot_rolling(column_name)
        
    
    def get_plot_object(self):
        if(self.canvas != None):
            return self.canvas
        else:
            return None

    def plot_rolling(self,column_name):  
        #self.remove_plot()
        try:   
            fig = Figure(self.figsize)
            plt.tight_layout()
            a = fig.add_subplot(111)
            #self.df_rolling = self.df.rolling(window = 2 ).mean().fillna(0)
            self.rolling_column= self.df_rolling.rolling(2).mean().fillna(0)
            self.rolling_column.plot( y  = column_name,ax= a,title = self.title)            

            #new_x = dates.num2date(df_['date'])
            #a
            #lol =1
            #a.plot(lol1, lol2, color = 'red')
            #a.plot(p, range(2 +max(x)),color='blue')
           
            #a.set_title ("Estimation Grid", fontsize=16)
            #a.set_ylabel("Y", fontsize=14)
            #a.set_xlabel("X", fontsize=1
            self.canvas = FigureCanvasTkAgg(fig, master=self.window)
            self.canvas.get_tk_widget().grid(row = self.grid_list[0], column= self.grid_list[1])
            self.canvas = self.canvas.get_tk_widget()
            
            
            #self.canvas.draw()
        except Exception as e:
            print('message___1123')
            exc_type, exc_obj, exc_tb = sys.exc_info()
            print(e.__doc__,str(exc_obj),exc_tb.tb_lineno)
            #print(e.message) 