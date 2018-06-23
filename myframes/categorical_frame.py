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

#we create two frames for the transform df window
#one to preprocess numerical columns 
#and aother to preprocess categorical values
class transform_categorical_frame(tk.Frame):
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
        
        self.numerical_option.grid(row = 60, column = 1)
        
        self.entries = []
        
        self.transform_numerical_columns = tk.Button(self, text = "TransformCategorical", command = self.transform_categorical,bg="lightblue")
        self.transform_numerical_columns.grid(row =5,column = 1 )
        
        self.add_button = tk.Button(self, text = "Substract Categorical columns", command = self.remove_last_from_list,bg = "yellow")
        self.add_button.grid(row =65,column = 1)
        self.add_button = tk.Button(self, text = "Append Categorical columns", command = self.addToListNumeric,bg = "yellow")
        self.add_button.grid(row = 80,column = 1)
        
    #transform numericl
    def transform_categorical(self):
        return
        # open("andrea.txt",'w+')
        
        # final_column_list = []
        # list_entries = [str(e.get()) for e in self.entries]
        
       
        # for l_e_item in list_entries:
        #     if(l_e_item != '' ):
        #         final_column_list.append(l_e_item)
        
        
        # if(StaticDataFrame.loaded_csv== False):
        #     return
        # #print(self.loaded_csv)
        
        # for i_ in range(len(final_column_list)):
        #     if(final_column_list[i_]  not in self.df.columns.values):
        #         final_column_list.pop(i_)
        
        # if not final_column_list:
        #     return
        
        
        # self.df = replace_if_non_numeric(self.df,final_column_list)
        # StaticDataFrame.set_dataframe(self.df)
        
    #remove last from list 
    def remove_last_from_list(self):
        print(self.entries)
        
        if(len(self.entries) == 0 ):
            return 
        else:
            poped =self.entries.pop()
            poped.grid_forget()
        return entries
    
    #add to list numeric
    def addToListNumeric(self):
        
        entry_to_append= tk.Entry(self)
        column_to_append= self.optionvariable.get()
        
        
        if(column_to_append != 'NONE'):
            for entry_ in self.entries:
                entry_already_inserted = entry_.get()
                if(entry_already_inserted == column_to_append ):
                    return 
            entry_to_append.insert(0,column_to_append)
        else:
            return
        entry_to_append.grid(row =100+len(self.entries), column = 1)
        
        self.entries.append(entry_to_append)
        return 
