from datetime import date, datetime
from encodings import utf_8
from fileinput import close
from tkinter import ACTIVE, ANCHOR, END, Entry, Listbox
from datetime import datetime


class Model:
    
    def __init__(self):
        self.list_file_name = 'list.txt' #file name to vriable
        self.date_now = datetime.now()
        self.list_elemnts = []
 
    #User input section
    
    
    def get_user_input(self):
        with open(self.list_file_name, 'a+', encoding='utf-8') as file:
            file.write(''.join(self.list_elemnts))
            file.write('\n') 
            del self.list_elemnts[:]      
        
    #Delete entire list
    def delete_entire_list(self):
        'Removes all items from list'
        with open(self.list_file_name, 'w', encoding='utf-8') as file:
            file.write('')
    

