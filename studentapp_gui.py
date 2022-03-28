#have to import these modules so have access to them

from tkinter import *
from tkinter import messagebox
import tkinter as tk

import studentapp_main
import studentapp_func

def load_gui(self):

    self.lbl_fname = tk.Label(self.master,text='First Name:')
    self.lbl_fname.grid(row=0,column=0,padx=(27,0),pady=(10,0),sticky=N+W)
    self.lbl_lname = tk.Label(self.master,text='Last Name:')
    self.lbl_lname.grid(row=2,column=0,padx=(27,0),pady=(10,0),sticky=N+W)
    self.lbl_phone = tk.Label(self.master,text='Phone Number:')
    self.lbl_phone.grid(row=4,column=0,padx=(27,0),pady=(10,0),sticky=N+W)
    self.lbl_email = tk.Label(self.master,text='Email Address:')
    self.lbl_email.grid(row=6,column=0,padx=(27,0),pady=(10,0),sticky=N+W)
    self.lbl_course = tk.Label(self.master, text="Course:")
    self.lbl_course.grid(row=8, column = 0, padx =(27, 0), pady = (10,0), sticky = N + W)
    
    self.lbl_info = tk.Label(self.master,text='Information:')
    self.lbl_info.grid(row=0,column=2,padx=(0,0),pady=(10,0),sticky=N+W)
    

    self.txt_fname = tk.Entry(self.master,text='')
    self.txt_fname.grid(row=1,column=0,rowspan=1,columnspan=2,padx=(30,40),pady=(0,0),sticky=N+E+W)
    self.txt_lname = tk.Entry(self.master,text='')
    self.txt_lname.grid(row=3,column=0,rowspan=1,columnspan=2,padx=(30,40),pady=(0,0),sticky=N+E+W)
    self.txt_phone = tk.Entry(self.master,text='')
    self.txt_phone.grid(row=5,column=0,rowspan=1,columnspan=2,padx=(30,40),pady=(0,0),sticky=N+E+W)
    self.txt_email = tk.Entry(self.master,text='')
    self.txt_email.grid(row=7,column=0,rowspan=1,columnspan=2,padx=(30,40),pady=(0,0),sticky=N+E+W)
    self.txt_course = tk.Entry(self.master, text = '')
    self.txt_course.grid(row = 9, column = 0, columnspan = 2, padx=(30,40), pady=(0,0), sticky = N+E+W)

    #Defining the scroll bar 1. Syntax: Scrollbar(master[represents the parent window], options) The Orient
    #option sets our scroll bar in a vertical position. 
    self.scrollbar1 = Scrollbar(self.master,orient=VERTICAL)

    #Creates our listbox. Syntax: Listbox(master, option) Export Selection means, if "on", that a user can select text with mouse,
    # and the selected text will be exported to clipboard. The yscrollcommand  provides a slide controller that is used to implement vertical scrolled widgets, such as Listbox,
    #the "set" connects the listbox and scroll bar.
    self.lstList1 = Listbox(self.master,exportselection=0,yscrollcommand=self.scrollbar1.set)

    # bind function deals with events. Syntax widget.bind(event, handler)
    self.lstList1.bind('<<ListboxSelect>>',lambda event:studentapp_func.onSelect(self,event))
    #
    # use config method to update scroll bar. "command" is the function or method to be called when scroll bar is loaded. "yview" is for vertical scroll bar. 
    #means 
    self.scrollbar1.config(command=self.lstList1.yview)
    #positioning the scroll bar.
    self.scrollbar1.grid(row=1,column=5,rowspan=7,columnspan=1,padx=(0,0),pady=(0,0),sticky=N+E+S)
    #positioning the first list
    self.lstList1.grid(row=1,column=2,rowspan=7,columnspan=3,padx=(0,0),pady=(0,0),sticky=N+E+S+W)
    
    self.btn_add = tk.Button(self.master,width=12,height=2,text='Add',command=lambda: studentapp_func.addToList(self))
    self.btn_add.grid(row=10,column=0,padx=(25,0),pady=(45,10),sticky=W)
    #self.btn_update = tk.Button(self.master,width=12,height=2,text='Update',command=lambda: studentapp_func.onUpdate(self))
    #self.btn_update.grid(row=8,column=1,padx=(15,0),pady=(45,10),sticky=W)#
    self.btn_delete = tk.Button(self.master,width=12,height=2,text='Delete',command=lambda: studentapp_func.onDelete(self))
    self.btn_delete.grid(row=10,column=2,padx=(15,0),pady=(45,10),sticky=W)
    self.btn_close = tk.Button(self.master,width=12,height=2,text='Close',command=lambda: studentapp_func.ask_quit(self))
    self.btn_close.grid(row=10,column=4,columnspan=1,padx=(15,0),pady=(45,10),sticky=E)

    studentapp_func.create_db(self)
    studentapp_func.onRefresh(self)



    if __name__ =="__main__":
        pass
