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
        
        #initiate the general info label
        self.labelTitleVariable = tkinter.StringVar()
        titlelabel = tkinter.Label(self, textvariable=self.labelTitleVariable, anchor="w", fg="black", bg="lightgrey")
        titlelabel.grid(column=0,row=0,columnspan=2,sticky="EW")
        self.labelTitleVariable.set(u"Pick RL Trial")

        #initiate the Travelling Salesman Button
        button = tkinter.Button(self,text=u"Travelling Salesman",
                                command=self.OnTSButtonClick)
        button.grid(column=0,row=1)

        #Add a label to indicate the last selected RL Trial
        self.labelVariable = tkinter.StringVar()
        label = tkinter.Label(self,textvariable=self.labelVariable,
                              anchor="w",fg="white",bg="blue")
        label.grid(column=0,row=2,columnspan=2,sticky='EW')
        self.labelVariable.set(u"Type the trial you want to run")

        self.grid_columnconfigure(0,weight=1)
        self.resizable(True,False)
        self.update()
        self.geometry(self.geometry())   
        
    #definition to run the travelling salesman program   
    def OnTSButtonClick(self):
        self.labelVariable.set( " Travelling Salesman" )
        TS.TS1Graph(7,1,8,0.8)


if __name__ == "__main__":
    app = RLTrialsGUI_tk(None)
    app.title('RL Trials')
    app.mainloop()
