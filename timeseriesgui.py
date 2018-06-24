
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
from myframes.plot_frame import plot_frame
from myframes.stationarity_frame import stationarity_frame
from myframes.decompose_frame import decomposition_frame
from myframes.autocorr_frame import autocorr_frame


#we create two frames for the transform df window
#one to preprocess numerical columns 
#and aother to preprocess categorical values
class transform_datekey_frame(tk.Frame):
    def __init__(self,parent):
        
        self.parent= parent
        self.df = StaticDataFrame.get_dataframe()
        
        tk.Frame.__init__(self, parent)
        
        self.optionvariable = StringVar(self)
        self.optionvariable.set('NONE')
        
        column_list = []
        if(StaticDataFrame.loaded_csv== True):
            #f_ = df
            for column in self.df:
                column_list.append(column)
            print(column_list)
        else:
            return
                   
        self.numerical_option = OptionMenu(self, self.optionvariable, *column_list)
        
        self.numerical_option.grid(row = 1, column = 1)
        

        self.transform_numerical_columns = tk.Button(self, text = "Make Date Column as Index", command = self.transform_key,bg="lightblue")
        self.transform_numerical_columns.grid(row =5,column = 1 )
                
        
    #transform date column and set df index
    def transform_key(self):
        datetime_label =  pd.to_datetime(self.df[self.optionvariable.get()],dayfirst = True)   
        self.df.set_index(datetime_label, inplace=True)
        print('transform key')
        StaticDataFrame.set_dataframe(self.df)
        print(StaticDataFrame.get_dataframe().head(5))







class plot_object:
    def __init__(self,  window,df_,column_name,grid_list,title  = 'A plot',figsize = (5,5)):
        self.window = window
        self.df = df_
        self.grid_list = grid_list
        self.figsize = figsize
        self.title = title
        #self.box = Entry(window)
        #self.button = Button (window, text="check", command=self.plot)
        #self.box.pack ()
        self.plot(column_name)
        #self.button.pack()
    
    
    def plot (self,column_name):       
        fig = Figure(self.figsize)
        plt.tight_layout()
        a = fig.add_subplot(111)
        self.df.plot( y = column_name,ax= a,title = self.title)
        #new_x = dates.num2date(df_['date'])
        #a
        
        #lol =1
        #a.plot(lol1, lol2, color = 'red')
        #a.plot(p, range(2 +max(x)),color='blue')
       
        #a.set_title ("Estimation Grid", fontsize=16)
        #a.set_ylabel("Y", fontsize=14)
        #a.set_xlabel("X", fontsize=14) 
        canvas = FigureCanvasTkAgg(fig, master=self.window)
        canvas.get_tk_widget().grid(row = self.grid_list[0], column= self.grid_list[1])
        canvas.draw()


# a window hat browses csv time series and displays it 
#create windows

class WindowTS(tk.Frame):
    def __init__(self,parent):
        self.loaded_csv= False  
        self.parent= parent
        tk.Frame.__init__(self, parent)
        self.button2 = tk.Button(master= self, text="Browse CSV", command =
                                 self.browse_button,bg="lightblue")
        
        
        self.entry_list = []
        self.header_list = []
        
        self.button2.grid(row= 1, column = 1)
        self.df = None
        self.add_menu()
           # Allow user to select a directory and store it in global var
        # called folder_path    
    
    
    
    def refresh_grid(self):
        print('head_size')
        for entry_item in self.entry_list:
            entry_item.delete(0, END)
        for header_item in self.header_list:
            header_item.delete(0,END)
        
        head_size =10
        
        rows, cols = StaticDataFrame.df.shape
                
        print('head_size')
        for r in (range(head_size)):
            for c in range(0,cols):
                if(r == 0 ):
                    
                    e.insert(0, columns_[c])
                    #e.grid(row = 5,column  = c)
                else:
                    #e = tk.Entry(self)
                    #self.entry_list.append(e)
                    e.insert(0, StaticDataFrame.df.iloc[r-10,c])
                    #e.grid(row=r+10, column=c)    
            
            
     
    def browse_button(self):  
        filename = filedialog.askopenfilename()
        print(filename)
        if(not filename == ''):
            self.loaded_csv = True
            self.filepath = filename
            #self.refresh_gui()
            self.display_csv()
            
        
    def add_menu(self):
        
        self.menubar = tk.Menu(self,tearoff = 0 )
        self.menubar.add_command(label="Transform time series", command=self.pop_preprocess_window)  
        self.menubar.add_command(label = "Plot Time Series", command = self.pop_plot_window)
        self.menubar.add_command(label = "TestStationarity", command = self.pop_stationarity_window)
        self.menubar.add_command(label = "TrendSeasonal Decomposition", command = self.pop_tsldecompose_window)
        self.menubar.add_command(label = "ACF PACF functions",command = self.pop_autocorr)
        #self.menubar.add_command(label="Quit!", command=self.parent.quit)
        #self.menubar.add_command(label="MachineLearning", command=self.machine_learning_window)
        self.parent.config(menu = self.menubar )
        #self.menubar.grid(row = 0 , column = 0 )
         


    def pop_autocorr(self):
        self.top_autocorr = tk.Toplevel(self.parent)
        if(StaticDataFrame.loaded_csv == True):
            self.autocorr_frame = autocorr_frame(self.top_autocorr,StaticDataFrame.df)
            self.autocorr_frame.grid(row = 0 , column = 0 , pady = (10,10))

            
    #tsl decompose window in tkinter
    #creates a top level with tsl decompose plots and tests
    def pop_tsldecompose_window(self):
        self.top_decompose= tk.Toplevel(self.parent)
        if(StaticDataFrame.loaded_csv==True):
            self.decomposition_frame = decomposition_frame(self.top_decompose,StaticDataFrame.df)
            self.decomposition_frame.grid(row = 0 , column = 0 , pady=(10,10))



    #stationarity window tkinter 
    #creates a top level with stationarity plots and tests
    def pop_stationarity_window(self):
        self.top_stationarity = tk.Toplevel(self.parent)
        if(StaticDataFrame.loaded_csv==True):
            self.stationarity_frame = stationarity_frame(self.top_stationarity,StaticDataFrame.df)

            self.stationarity_frame.grid(row = 0 , column = 0 , pady=(10,10))


    #pop plot window
    def pop_plot_window(self):
        self.top_plot = tk.Toplevel(self.parent)
        #self.top_plot_frame = plot_frame(self.top_plot)
              
        #we should add a frame then add inside the scrolling bar and the canvas 
        if(StaticDataFrame.loaded_csv== True):
            #self.enclosing_frame = tk.Frame(self.top_plot)
            #self.enclosing_frame.grid(row = 0,column = 0 )

            #elf.vscrollbar = tk.Scrollbar(self.enclosing_frame, orient = VERTICAL)
            #self.vscrollbar.grid(row = 0 , column =0)

            #self.top_plot_canvas = tk.Canvas(self.enclosing_frame,yscrollcommand = self.vscrollbar.set)
            self.top_plot_frame = plot_frame(self.top_plot,StaticDataFrame.df)

            #self.top_plot_canvas.create_window(0,0, anchor = tk.NW, window = self.top_plot_frame, width = 200, height = 200)
            #self.top_plot_canvas.grid(row = 0 , column = 0 )
            self.top_plot_frame.grid(row = 0 , column = 0, pady = (10,10) )
            #else:

            #self.top_plot_frame = error_frame(self.top_plot,'Error not found')

            
    def pop_preprocess_window(self):
        print('imin')
        self.top_preprocess = Toplevel(self.parent)
        
        #self.top_frame = preprocess_frame(self.top_preprocess,StaticDataFrame.get_dataframe() )
        

        self.datetimeFrame = transform_datekey_frame(self.top_preprocess)
        self.top_frame = transform_numeric_frame(self.top_preprocess)
        self.top_cat_frame = transform_categorical_frame(self.top_preprocess)

        self.datetimeFrame.grid(row = 0 ,column = 0,pady =(20,20), padx = (10,10) )

        self.top_frame.grid(row=50, column = 0 ,pady =(20,20), padx = (10,10))
        self.top_cat_frame.grid(row = 100, column = 0 ,pady = (20,20) ,padx = (10,10))
    #display csv
    
    #refresh_gui 
    def refresh_gui(self):
        self.button2.grid_forget()
        print('self.button')
        self.refresh = tk.Button(master= self, text="Refresh", command =
                                 self.refresh_grid,bg="lightblue")
        
        
        
        print('browse_gui')
        
        self.refresh.grid(row = 1, column  =1)
        
    
    def display_csv(self):
        df =  pd.read_csv(self.filepath)
        
        StaticDataFrame.set_dataframe(df)
        self.df = df
        
       
        
        #label= tk.Label(self, text="The payment options are displayed below")
        rows, cols = self.df.shape
        columns_ =self.df.columns.values
        #iterate over columns_
        
        head_size =10
        if(rows<10):
            head_size = rows
        

        print(head_size)
        for r in (range(head_size+11)):
            for c in range(0,cols):
                if(r == 0 ):
                    e =tk.Entry(self)
                    self.header_list.append(e)
                    e.insert(0, columns_[c])
                    e.grid(row = 5,column  = c)
                else:
                    e = tk.Entry(self)
                    self.entry_list.append(e)
                    #print(self.current_plot)
                    e.insert(0, StaticDataFrame.df.iloc[r-11,c])
                    e.grid(row=r+10, column=c)

if __name__ == '__main__':
    if __name__ == '__main__':
        root = tk.Tk()
        wts = WindowTS(root)
        wts.pack()
        root.mainloop()

