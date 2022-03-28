
#Python Version: 3.9.5

#Author: Vicky Jones

#Purpose: to create a student tracking system application using Python, Tkinter and SQLite3

#Tested OS: this code was written and tested on Windows 10

import os
from tkinter import *
from tkinter import messagebox
import tkinter as tk
import sqlite3

import studentapp_gui
import studentapp_func

class ParentWindow(Frame): #connects the Tkinter Frame object to the
#child object we created called ParentWindow.

    
    def __init__(self, master, *args, **kwargs): #"master" parameter is the parent widget, which is the Frame widget. 
        Frame.__init__(self,master, *args, **kwargs)

        #configure our main frame. "self.master" is like address to get access to the tkinter Frame widget

        self.master = master
        self.master.minsize(500,400) #(height, width)
        self.master.maxsize(500,400)

        #centering our main window with our own function 

        studentapp_func.center_window(self,500,300) #need to pass in "self" to access all
        #attributes, methods. 

        self.master.title("The Student Tracker App")
        self.master.configure(bg="#F0F0F0")
        #setting up a protocol or rule that if MS red box with X is clicked, do the ask_quit method
        self.master.protocol("WM_DELETE_WINDOW", lambda: studentapp_func.ask_quit(self))
        
        arg = self.master

        studentapp_gui.load_gui(self)






if __name__ == "__main__":
    root = tk.Tk()
    App = ParentWindow(root)
    root.mainloop() #method that loops forever, waiting for events from the user, until the user exits the program
#root refers to our main window of our application. 
