
import matplotlib
matplotlib.use('TkAgg')
import numpy as np
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure
from tkinter import *
import matplotlib.dates as dates
from myframes.categorical_frame import transform_categorical_frame
from myframes.numeric_frame import transform_numeric_frame
from statsmodels.tsa.stattools import adfuller

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
from abc import ABC, abstractmethod



# weather_r = read.csv('weather.csv')
#as.ts(weather_r)
#library(zoo)
#read.zoo(weather_r,header = True, format = "%d-%m-%Y")
#
#
#
#

class plot_object_super(object):
    def __init__(self,window ,df_,column_name,grid_list,title  = 'A plot',figsize = (5,5)):
        self.window = window
        self.df = df_
        self.pack_coords = grid_list
        #self.grid_list = grid_list
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
#for stationarity of dataframe 
class stationarity_frame(tk.Frame):
    def __init__(self,parent,df):
        self.parent= parent
        tk.Frame.__init__(self, parent)  
        self.variable = StringVar(self)
        self.rolling_window_var = StringVar(self)
        self.rolling_window_var.set('5')
        self.df =df 
        self.current_plot = None
        #self.scrollbar = Scrollbar(self)
        #self.scrollbar.grid(row = 0 , column = 100)
        if(StaticDataFrame.loaded_csv== True):
            df_ = df
            column_list = []
            for column in df:
                column_list.append(column)
            
            vcmd = (self.register(self.rollingWindowValidation), '%S')

            self.select_window = Entry(self,textvariable = self.rolling_window_var, width = 5, validate = 'key', vcmd = vcmd)


            self.select_window.grid(row = 5, column = 5 )

            self.options = OptionMenu(self, self.variable, *column_list)
            self.options.grid(row = 1, column = 1)
            self.button_plot = Button(self,text= "Plot", command = self.plot_function)

            self.button_plot.grid(row = 10, column = 1 )

    def rollingWindowValidation(self,S):
        if S in ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']:
            return True
        bell(self) 
        return False       

    def plot_function(self):
        try:
            if(self.current_plot!=None):
                self.current_plot.destroy()
                                
            #plot thwe selected column from the drop down menu 

            column_selected = self.variable.get()
            label = Label(self,text= "Graph_"+str(column_selected))
            label.grid(row = 15, column = 1)
            #print('PLOT_FUNCTION')

            self.frame_of_plots = tk.Frame(self)
            self.frame_of_plots.grid(row = 25, column = 1)

            self.subframe_of_plots = tk.Frame(self.frame_of_plots)
            self.subframe_of_plots2 = tk.Frame(self.frame_of_plots)
            self.subframe_of_plots.pack(side = tk.TOP)
            self.subframe_of_plots2.pack(side = tk.BOTTOM)

            self.frame_of_document = tk.Frame(self)
            self.frame_of_document.grid(row = 25,column = 100)


            plt_objct = rolling_plot_object(self.subframe_of_plots,StaticDataFrame.df,self.variable.get(),self.rolling_window_var.get(),tk.LEFT,'Rolling mean plot',figsize = (3,3),rolling_type_s = "mean")
            plt_objct_median = rolling_plot_object(self.subframe_of_plots,StaticDataFrame.df,self.variable.get(),self.rolling_window_var.get(),tk.RIGHT,'Rolling median plot',figsize = (3,3),rolling_type_s = "median")
            plt_objct_std = rolling_plot_object(self.subframe_of_plots2,StaticDataFrame.df,self.variable.get(),self.rolling_window_var.get(),tk.LEFT,'Rolling std plot',figsize = (3,3),rolling_type_s = "std")
            #result_adfuller = adfuller(self.df[self.variable.get()])
            self.text_result_adfuller = self.text_result_adfuller = tk.Text(self.frame_of_document, wrap=WORD, width=35, height= 40)

            dftest = adfuller(self.df[self.variable.get()], autolag='AIC')
            dfoutput = pd.Series(dftest[0:4], index=['Test Statistic','p-value','#Lags Used','Number of Observations Used'])
            for key,value in dftest[4].items():
                dfoutput['Critical Value (%s)'%key] = value
            document_text = str(dfoutput)
            self.text_result_adfuller.insert(INSERT,document_text)            
            
            #self.entry_result_adfuller = tk.Entry(self)
            #self.text_result_adfuller.insert(INSERT,result_adfuller)
            self.text_result_adfuller.pack(side = tk.BOTTOM)


            self.label_result_adfuller = tk.Label(self.frame_of_document,text = "Adfuller Test results")
            self.label_result_adfuller.pack(side = tk.TOP)
            

            #self.entry_result_adfuller.grid(row = 25,column = 100)
            #self.entry_result_adfuller.insert(0,result_adfuller)

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

                



#rolling plot object in python
class rolling_plot_object(plot_object_super):
    def __init__(self,  window,df_,column_name,window_rolling_int,pack_coords,title  = 'A plot',figsize = (5,5),rolling_type_s= 'mean'):
        super(rolling_plot_object, self).__init__(window,df_,column_name,pack_coords,title,figsize)            
        self.window_rolling_int = window_rolling_int

        print('lol'+str(self.window_rolling_int))
        self.rolling_type_str = rolling_type_s
        self.plot_rolling(column_name)

    
    
    def get_plot_object(self):
        if(self.canvas != None):
            return self.canvas
        else:
            return None

    #plots rolling mean example
    def plot_rolling(self,column_name):  
        #self.remove_plot()
        try:  
            fig = Figure(self.figsize)
            plt.tight_layout()
            a = fig.add_subplot(111)
            self.df_rolling = self.df
            
            if(self.rolling_type_str == 'mean'):
                self.rolling_column = self.df_rolling.rolling(int(self.window_rolling_int)).mean().fillna(0)
            elif(self.rolling_type_str == 'median'):
                self.rolling_column = self.df_rolling.rolling(int(self.window_rolling_int)).median().fillna(0)
            elif(self.rolling_type_str == 'std'):   
                self.rolling_column = self.df_rolling.rolling(int(self.window_rolling_int)).std().fillna(0)
                print('run deep run high')
            else:
                self.rolling_column = self.df_rolling.rolling(int(self.window_rolling_int)).mean().fillna(0)
            #self.rolling_column= self.df_rolling.rolling(int(self.window_rolling_int)).mean().fillna(0)
            self.rolling_column.plot( y  = column_name,ax= a,title = self.title)  
            

            self.canvas = FigureCanvasTkAgg(fig, master=self.window)
            #self.canvas.get_tk_widget().grid(row = self.grid_list[0], column= self.grid_list[1])
            self.canvas.get_tk_widget().pack(side = self.pack_coords,fill = tk.BOTH)
            self.canvas = self.canvas.get_tk_widget()
            
            
            #self.canvas.draw()
        except Exception as e:
            print('message___1123')
            exc_type, exc_obj, exc_tb = sys.exc_info()
            print(e.__doc__,str(exc_obj),exc_tb.tb_lineno)
            #print(e.message) 

#we want to make the validation entry to get only numerical values
#OK ? ????? ?? ??? ? ? ? ? ? ? 
    
