
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
from statsmodels.tsa.seasonal import seasonal_decompose
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


#creates a frame that performs tsl decomposition
#mfka

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
class decomposition_frame(tk.Frame):
    def __init__(self,parent,df):
        self.parent= parent
        tk.Frame.__init__(self, parent)  
        self.variable = StringVar(self)

        #self.rolling_window_var = StringVar(self)
        #self.rolling_window_var.set('5')
        self.df =df 
        self.current_plot = None
        #self.scrollbar = Scrollbar(self)
        #self.scrollbar.grid(row = 0 , column = 100)
        print('imheere')
        if(StaticDataFrame.loaded_csv== True):

            df_ = df
            column_list = []
            for column in df:
                column_list.append(column)  
            
            #vcmd = (self.register(self.rollingWindowValidation), '%S')
            #self.select_window = Entry(self,textvariable = self.rolling_window_var, width = 5, validate = 'key', vcmd = vcmd)
            #self.select_window.grid(row = 5, column = 5 )



            self.options = OptionMenu(self, self.variable, *column_list)
            self.options.grid(row = 1, column = 1)
            self.button_plot = Button(self,text= "Plot", command = self.plot_function)

            self.button_plot.grid(row = 10, column = 1 )


    def plot_function(self):
        try:
            if(self.current_plot!=None):
                self.current_plot.destroy()
                                
            #plot thwe selected column from the drop down menu 
            #gets the selected option from option menu 
            column_selected = self.variable.get()
            label = Label(self,text= "Graph_"+str(column_selected))
            label.grid(row = 15, column = 1)
            #print('PLOT_FUNCTION')

            self.frame_of_plots = tk.Frame(self)
            self.frame_of_plots.grid(row = 25, column = 1)


            # self.subframe_of_plots = tk.Frame(self.frame_of_plots)
            obs_plot = plot_object_decompose(self.frame_of_plots,StaticDataFrame.df,self.variable.get(),tk.TOP,'Rolling mean plot',figsize = (4,2),decomp_type= 'obs')
            trend_plot  = plot_object_decompose(self.frame_of_plots,StaticDataFrame.df,self.variable.get(),tk.TOP,'Rolling mean plot',figsize = (4,2))
            seas_plot = plot_object_decompose(self.frame_of_plots,StaticDataFrame.df,self.variable.get(),tk.BOTTOM,'Rolling mean plot',figsize = (4,2),decomp_type= 'seasonal')
            resid_plot = plot_object_decompose(self.frame_of_plots,StaticDataFrame.df,self.variable.get(),tk.BOTTOM,'Rolling mean plot',figsize = (4,2),decomp_type= 'resid')
                    
            #self.current_plot = decompose_plot.get_plot_object()   

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
#########
class plot_object_decompose(plot_object_super):
    def __init__(self,  window,df_,column_name,pack_coords,title  = 'A plot',figsize = (5,5),decomp_type= 'trend'):
        super(plot_object_decompose, self).__init__(window,df_,column_name,pack_coords,title,figsize)            
        #self.window_rolling_int = window_rolling_int
        self.decomp_type = decomp_type

        self.plot(column_name )  

    
    def get_plot_object(self):
        if(self.canvas != None):
            return self.canvas
        else:
            return None

    #plots rolling mean example
    def plot(self,column_name):  
        #self.remove_plot()
        try:  

            fig = Figure(self.figsize)
            plt.tight_layout()
            a = fig.add_subplot(111)
            #self.df_rolling = self.df

            #self.rolling_column = self.df_rolling.rolling(int(self.window_rolling_int)).std().fillna(0)
            
            #self.rolling_column= self.df_rolling.rolling(int(self.window_rolling_int)).mean().fillna(0)
            #self..plot( y  = column_name,ax= a,title = self.title)  


                    
            df_new = make_column_positive(self.df.copy(),column_name)

            #seasonal decompose

            self.result_sdcm = seasonal_decompose(df_new[column_name], model='multiplicative', freq=1)
                
            
            if(self.decomp_type == 'trend'):
                dataframe_to_plot= pd.DataFrame(self.result_sdcm.trend)
                dataframe_to_plot.plot(y = column_name,ax = a,title = 'Trend')
            elif(self.decomp_type =='obs'):
                dataframe_to_plot = pd.DataFrame(self.result_sdcm.observed)
                dataframe_to_plot.plot(y = column_name, ax = a, title = 'Observed')
            elif(self.decomp_type =='seasonal'):
                dataframe_to_plot = pd.DataFrame(self.result_sdcm.seasonal)
                dataframe_to_plot.plot(y = column_name,ax = a,title = 'Seasonal')
            elif(self.decomp_type =='resid'):
                dataframe_to_plot = pd.DataFrame(self.result_sdcm.resid)
                dataframe_to_plot.plot(y = column_name,ax = a,title = 'residual')
            
        
                        
            


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

#make column positive
def make_column_positive(df,column):
    min_ = df[column].min()
    
    if(min_<= 0):
        df[column] = df[column]-min_+1
    return df
    
