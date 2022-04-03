from cmath import exp
from datetime import datetime
from this import d
from tkinter import *
import tkinter.font as tkFont
from tkinter import ttk
from turtle import width
from Controller import *
from Model import *
from setuptools import Command
import datetime as dt


class View(Tk):
    
    def __init__(self, controller):
        super().__init__() #For a tk
        #Few variables
        self.controller = controller
        self.userinput = StringVar()
        self.defaultFontStyle = tkFont.Font(family='Verdana', size=10, weight='bold')
        self.TitleFontStyle = tkFont.Font(family='Verdana', size=28)
        
        #Main view
        self.geometry('500x800') #Window resolutin
        self.resizable(False, False) # Resolution is fixed
        self.title('To-Do List') #Tk window title
        
        
        #Frames
        self.top_frame = self.create_top_frame()
        self.center_frame = self.create_center_frame()
        self.bottom_frame = self.create_bottom_frame()
        
        
        #Widgets
        self.title_date()
        self.list_elements()
        self.create_user_input()
        self.create_remove_button()
        self.create_reset_button()
        self.del_file_path()

        
    
    def main(self):
        self.update()
        self.mainloop()
            
    #Frames section
    def create_top_frame(self):
        frame = Frame(self, bg='#F1F1F1', height='100')
        frame.pack(expand=False, fill='both')
        return frame
    
    def create_center_frame(self):
        frame = Frame(self, bg='#DEF6F7', height='400')
        frame.pack(expand=True, fill='both')
        return frame
    
    def create_bottom_frame(self):
        frame = Frame(self, bg='#B9B6AA')
        frame.pack(expand=True, fill='both')
        return frame
    
    #Title function
    def title_date(self):
        date =dt.datetime.now()
        date_format = f'{date:%A, %d.%m.%Y}'
        title_show = Label(self.top_frame, text=date_format, font=self.TitleFontStyle, anchor='center')
        title_show.pack(pady=20)
    
    def list_elements(self):
        self.todo_list = Listbox(self.center_frame, bg='#CAE8DA', font=self.defaultFontStyle, height=35, width=55)
        
        scroll = Scrollbar(self.center_frame, orient=VERTICAL, command=self.todo_list.yview)
        scroll.place(x=439,y=51, height=455)
        self.todo_list.config(yscrollcommand=scroll.set)
        scroll_hot = Scrollbar(self.center_frame, orient=HORIZONTAL, command=self.todo_list.xview)
        scroll_hot.place(x= 51, y=507, width=400)
        self.todo_list.config(xscrollcommand=scroll_hot.set)
        self.todo_list.grid(row=0, column=2, padx=50, pady=50)
        
    #input section
    def create_user_input(self):
        self.enter_info = Label(self.bottom_frame, text='Enter To-Do List elements', width=10 , font=self.defaultFontStyle)
        self.enter_info.grid(row=1, column=0, padx=5, pady=5)
        
        self.enter_value = Entry(self.bottom_frame, textvariable=self.userinput)
        self.enter_value.grid(row=1, column=1, padx=5, pady=5)
        self.enter_value.focus() #Makse a textbox active

        
        self.button = Button(self.bottom_frame, text='Send', font=self.defaultFontStyle, command=lambda:self.controller.send_btn_clicked())
        self.button.grid(row=1, column=2, padx=5, pady=5)
        
    #Buttons section  
    def create_remove_button(self):
        del_e_info = Label(self.bottom_frame, text='Select at least one element and delte it', font=self.defaultFontStyle)
        del_e_info.grid(row=2, column=0, columnspan=2, padx=5, pady=5)
        
        button = Button(self.bottom_frame, text='Delete element', width=10, font=self.defaultFontStyle, command=lambda:self.controller.del_btn_clicked())
        button.grid(row=2, column=2, padx=5, pady=5)
        
    def create_reset_button(self):    
        self.del_all_info = Label(self.bottom_frame, text='With this button you reset the content block', font=self.defaultFontStyle)
        self.del_all_info.grid(row=3, column=0, columnspan=2, padx=5, pady=5)
        
        self.button_all = Button(self.bottom_frame, text='Reset All', width=10, font=self.defaultFontStyle, command=lambda:self.controller.reset_btn_clicked())
        self.button_all.grid(row=3, column=2, padx=5, pady=5)
    
    def del_file_path(self):
        self.del_file = Label(self.bottom_frame, text='Delete file list.txt', font=self.defaultFontStyle)
        self.del_file.grid(row=4, column=0, columnspan=2, padx=5, pady=5)
        
        self.del_file_button = Button(self.bottom_frame, text='Delete file', width=10, font=self.defaultFontStyle, command=lambda:self.controller.delete_file())
        self.del_file_button.grid(row=4, column=2, padx=5, pady=5)
        
