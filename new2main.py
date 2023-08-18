from tkinter import *;import multiprocessing,subprocess,time,random,re

class app:
    def __init__(self,me):
        self.me=me;self.me["bg"]="black";self.me.title("Reconnaissance")
        self.ipframe=Frame(self.me,bg="black");self.ipframe.grid(row=0,column=0,sticky="NSW")
        self.footer=Label(self.me,text="Enter IPv4!",bg="black",fg="white",font="bold");self.footer.grid(row=1,column=0,sticky="NSW")
        self.ipentry=Entry(self.ipframe,bg="black",fg="white",font="bold");self.ipentry.grid(row=0,column=0,sticky="NSW")
        self.ipsubmit=Button(self.ipframe,text="Check",bg="black",fg="white",font="bold",state="disabled");self.ipsubmit.grid(row=0,column=1,sticky="NSW");self.ipsubmit.bind("<Enter>", self.onipsubmithover)
        self.ipadd=Button(self.ipframe,text="+",bg="black",fg="green",font="bold",state="disabled",command=lambda:self.addanotherip);self.ipadd.grid(row=1,column=0,sticky="NSW")

    def onipsubmithover(self,event):
        if None==re.compile("^((25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)$").match(self.ipentry.get()):#"1.1.1.1"):
            self.footer.config(text="Incorrect IPv4 format!",fg="red")
            self.me.after(2000,self.reset)
        else:
            self.footer.config(text="Add IPv4 or Start.")
            self.ipsubmit.config(state="active",text="Start",fg="green",command=lambda:"")
            self.ipentry.config(state="disabled")
            self.ipadd.config(state="normal")
            
    def reset(self):
        self.footer.config(text="Enter IPv4!",fg="white")

    def addanotherip(self):
        new_entry = Entry(self.ipframe, bg="black", fg="white", font="bold")
        new_entry.grid(row=self.ipframe.grid_size()[1], column=0, sticky="NSW")

if __name__ == "__main__":
    program=Tk()
    app(program)
    program.mainloop()

