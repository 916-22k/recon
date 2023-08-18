from tkinter import *;import multiprocessing,subprocess,random,re
def ipclear(ipentry,ipremove,ipfooter):
    
    ipfooter.destroy();ipremove.destroy()
    print(ipfooter.grid_info()["row"])

def ipvalidate(meframe,ipremove,ipentry,ipsubmit,ipfooter):
    if None==re.compile("^((25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)$").match("1.1.1.1"):#ipentry.get()):
        ipfooter.configure(text="Incorrect IPv4 format!",fg="red")
    else:
        ipentry.config(state="disabled")
        ipsubmit.grid_forget()
        ipadd=Button(meframe,bg="black",fg="green",font="bold",command=lambda:addip(ipadd))
        ipremove=Button(meframe,text="-",fg="black",bg="red",font="bold",command=lambda:ipclear(ipentry,ipremove,ipfooter));ipremove.grid(sticky="W",row=int(ipentry.grid_info()["row"])+1,column=0)
        print(ipentry.grid_info()["row"])


def addip(meframe,ipremove,ipentry,ipsubmit,ipfooter):""



if __name__ == "__main__":
    me=Tk();me["bg"]="black";me.title("Reconnaissance")
    meframe=Frame(me,bg="black",width=800,height=200);meframe.grid(sticky="W")
    ipfooter=Label(me,fg="white",font="bold",bg="black",text="Please enter an IPv4 above.");ipfooter.grid(row=1,column=0,sticky="W")
    ip_manager=[[
        Button(meframe,bg="black",fg="white",font="bold",text="-",state="disabled",command=lambda:ipclear(*ip_manager[0])),
        Entry(meframe,bg="grey",width=17),
        Button(meframe,bg="black",fg="white",width=10,text="Check",command=lambda:ipvalidate(meframe,*ip_manager[0],ipfooter))]]
    #ipremove,ipentry,ipsubmit
    for ind,obj in enumerate(ip_manager[0]):obj.grid(sticky="NSEW",row=0,column=ind)
    
    me.mainloop()


