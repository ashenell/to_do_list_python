from Controller import *


class TodolistApp:
    
    def __init__(self):
        app = Controller()
        app.main() #Graphical widow for mainloop
        
if __name__ == '__main__':
    todo_lists = TodolistApp()