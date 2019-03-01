# -*- coding: utf-8 -*-

import tkinter
import TS

class RLTrialsGUI_tk(tkinter.Tk):
    def __init__(self,parent):
        tkinter.Tk.__init__(self,parent)
        self.parent = parent
        self.initialize()

    def initialize(self):
        self.grid()
        
        self.labelTitleVariable = tkinter.StringVar()
        titlelabel = tkinter.Label(self, textvariable=self.labelTitleVariable, anchor="w", fg="black", bg="lightgrey")
        titlelabel.grid(column=0,row=0,columnspan=2,sticky="EW")
        self.labelTitleVariable.set(u"Pick RL Trial")

#        self.entryVariable = tkinter.StringVar()
#        self.entry = tkinter.Entry(self,textvariable=self.entryVariable)
#        self.entry.grid(column=0,row=0,sticky='EW')
#        self.entry.bind("<Return>", self.OnPressEnter)
#        self.entryVariable.set(u"Choosing a trial to run")

        button = tkinter.Button(self,text=u"Travelling Salesman",
                                command=self.OnTSButtonClick)
        button.grid(column=0,row=1)
        button = tkinter.Button(self,text=u"Other Trial",
                                command=self.OnOtherButtonClick)
        button.grid(column=1,row=1)

        self.labelVariable = tkinter.StringVar()
        label = tkinter.Label(self,textvariable=self.labelVariable,
                              anchor="w",fg="white",bg="blue")
        label.grid(column=0,row=2,columnspan=2,sticky='EW')
        self.labelVariable.set(u"Type the trial you want to run")

        self.grid_columnconfigure(0,weight=1)
        self.resizable(True,False)
        self.update()
        self.geometry(self.geometry())       
        #self.entry.focus_set()
        #self.entry.selection_range(0, tkinter.END)

    def OnTSButtonClick(self):
        self.labelVariable.set( " Travelling Salesman" )
        TS.TS1Graph()
 
    def OnOtherButtonClick(self):
        self.labelVariable.set( " (This should open the Other graphs)" )
        #self.entry.focus_set()
        #self.entry.selection_range(0, tkinter.END)

    #def OnPressEnter(self,event):
        #self.labelVariable.set( self.entryVariable.get()+" (TODO: Program)" )
        # self.entry.focus_set()
        # self.entry.selection_range(0, tkinter.END)


if __name__ == "__main__":
    app = RLTrialsGUI_tk(None)
    app.title('RL Trials')
    app.mainloop()
