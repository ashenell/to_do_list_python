from Model import *
from View import *
from tkinter import *
import tkinter as tk
from tkinter import messagebox
import os
from os.path import exists
class Controller:
    
    def __init__(self):
        self.model = Model()
        self.view = View(self)
        self.check_file_path()
       
    
    def main(self):
        self.view.main() #Going to run in View.py main method
    #Send items clicked 
    def send_btn_clicked(self):
        task = self.view.enter_value.get()
        if task != '':
            self.view.todo_list.insert(END, task)
            self.model.list_elemnts.append(task)
            self.view.userinput.set('')
            self.model.get_user_input()
        else:
            messagebox.showwarning('Wartning', 'Please etner some text.')
    #File control and checks        
    def check_file_path(self):
        self.file_exists = os.path.exists(self.model.list_file_name)
        if self.file_exists == False:
           with open(self.model.list_file_name, 'a+', encoding='UTF-8') as file:
               file.readlines()
        self.read_to_listbox()
    #Reading files to listbox controller    
    def read_to_listbox(self):
        with open(self.model.list_file_name, 'r', encoding='UTF-8') as file_content:
            for x in file_content:
                self.view.todo_list.insert(END, x)
    #Delete button clicked            
    def del_btn_clicked(self):
        self.delete_single_item()
    #Reset button clicked
    def reset_btn_clicked(self):
        self.message = messagebox.askquestion('Warning', 'Are you suer you wanna delete entire list')
        if self.message == 'yes':
            self.model.delete_entire_list()
            self.view.todo_list.delete(0, END)
        else:
            messagebox.showinfo('Return', 'Return back to-do list')
    #Delete file clicked
    def delete_file(self):
        self.reset_btn_clicked()
        if self.message == 'yes':
            os.remove(self.model.list_file_name)
    #File and listbox controller
    def delete_single_item(self):
        self.removed_lines = self.view.todo_list.curselection()
        with open(self.model.list_file_name, 'r', encoding='utf-8') as file:
            lines = file.readlines() 
            with open(self.model.list_file_name, 'w', encoding='utf-8') as file:
                for i,line in enumerate(lines):
                    if i not in self.removed_lines:
                        file.write(line)
        self.view.todo_list.delete(ANCHOR)
            

    
