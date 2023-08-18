from tkinter import *;import os,sys,threading,time,subprocess,requests,pexpect,asyncio,multiprocessing,random,re
def complete_pool(tasks):
  while 1:
    try:()if(True)in[(True)if(task.successful())else(False)for(task)in(tasks)]else(print("Not all thread tasks have been successful!"));break
    except:()
  results=[]
  for(task)in(tasks):
    try:
      if(task.get()!=None):
        for(found)in(task.get()):results.append(found)
    except:()
  return results
def request_async(*args):return[requests.get(args[0]).status_code,args[0]]
def ping(ip):outp=(outp:=(subprocess.check_output(["ping",ip,"-c","2"])).decode("utf-8").split("\n"))[[(True)if"transmitted"in(x)else(False)for(x)in(outp)].index(True)].split(",")[:2];return(["".join([(j)if(j)in[str(a)for(a)in(range(10))]else""for(j)in(objx)])for(objx)in(outp)])
class app:
    def __init__(self,me):
        self.pool=multiprocessing.Pool() 
        self.me=me;self.me["bg"]="black";self.me.title("Reconnaissance")
        self.ipFrame=Frame(self.me,bg="black");self.ipFrame.grid(row=0,column=0,sticky="NW")
        self.ipEntry=Entry(self.ipFrame,bg="black",fg="white",font="bold",state="normal");self.ipEntry.grid(row=0,column=0,sticky="NSW")
        self.ipSubmit=Button(self.ipFrame,text="Add IPv4",bg="black",fg="white",font="bold",state="disabled",command=self.pingip_check1,highlightbackground="black",highlightcolor="black");self.ipSubmit.grid(row=0,column=1,sticky="NSW");self.ipSubmit.bind("<Enter>",self.checkip);self.ipSubmit.bind("<Leave>",self.reverttext)
        self.ipWarning=Label(self.ipFrame,text="Type IPv4 ^",bg="black",fg="white",font="bold");self.ipWarning.grid(row=1,columnspan=2,sticky="NSW")
        self.ipFrame.columnconfigure(0,weight=1)
        self.ipTextWidget=Text(self.ipFrame,bg="black",fg="white",wrap="word",width=1,height=1,state="disabled",highlightthickness=0,highlightbackground="black",highlightcolor="black");self.ipTextWidget.grid(row=2,column=0,columnspan=2,sticky="NSEW")
        self.pingchecks=[]
        self.enumFrame=Frame(self.me,bg="black");self.enumFrame.grid(row=0,column=1,sticky="NW")
        self.enumStart=Button(self.enumFrame,text="Start",bg="black",fg="white",font="bold",state="disabled",command=lambda:"",highlightbackground="black",highlightcolor="black");self.enumStart.grid(row=0,column=0,sticky="NSW");self.enumStart.bind("<Enter>",self.checkAllIPs);self.enumStart.bind("<Leave>",self.reverttext)
    def checkAllIPs(self,event):
      fail=False
      for ind,obj in enumerate((local:=self.ipTextWidget.get("1.0", "end-1c")).split("\n")):
        if obj!="" and "🟢" not in obj:fail=True
      if fail==True:self.ipWarning.config(text="Still pinging...",fg="red")
      elif local=="":self.ipWarning.config(text="Need at least one IPv4!",fg="red")
      else:self.ipWarning.config(text="Start enumeration with IPv4s?",fg="green");self.enumStart.config(state="normal",fg="green",activebackground="green",activeforeground="black")


    def checkip(self,event):
        self.ipSubmit.config(state="disabled")
        if self.ipEntry.get()=="":self.ipWarning.configure(text="Cannot be blank!",fg="red")
        elif None==re.compile("^((25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)$").match(self.ipEntry.get()): self.ipWarning.config(text="Invalid IPv4 format!",fg="red")
        else:self.ipWarning.configure(text="Add to list?",fg="green");self.ipSubmit.config(state="normal",fg="green",activebackground="green",activeforeground="black")
    def reverttext(*args):args[0].ipWarning.configure(text="Type IPv4 ^",fg="white")
    def pingip_check1(self):
      if self.ipEntry.get() in self.ipTextWidget.get("1.0", "end-1c"):self.ipWarning.config(text="Duplicate IPv4!",fg="red");self.me.after(2000,self.reverttext)
      else:self.pingchecks.append((local:=threading.Thread(target=self.pingip_check2,daemon=True)));local.start()
      self.ipSubmit.config(state="disabled")
    def pingip_check2(self):
      self.ipTextWidget.config(state="normal");self.ipTextWidget.insert("end",(ip:=self.ipEntry.get())+"\n");self.ipEntry.delete(0,"end");self.ipTextWidget.config(state="disabled")
      self.ipTextWidget.config(height=int(self.ipTextWidget.index("end-1c").split(".")[0]))
      tasks=[]
      for o in range(5):tasks.append(self.pool.apply_async(ping,args=([ip])))
      tasks_results=complete_pool(tasks)
      for ind,obj in enumerate(self.ipTextWidget.get("1.0", "end-1c").split("\n")):
        if ip in obj:location=str(self.ipTextWidget.get("1.0", "end-1c").split("\n").index(obj)+1)+"."+str(obj.index(ip))
      if len(tasks_results)==0:self.ipWarning.config(text="Host down!",fg="red");self.ipTextWidget.config(state="normal");self.ipTextWidget.delete(location,str(int(location[:location.index(".")])+1)+"."+location[location.index(".")+1:]);self.me.after(2000,self.reverttext);self.ipTextWidget.config(state="disabled")
      elif sum([int(tasks_results[o]) for o in range(0,len(tasks_results),2)])>5:
        self.ipTextWidget.config(state="normal");self.ipTextWidget.insert(location,"🟢");self.ipTextWidget.config(state="disabled")
    



if __name__ == "__main__":
    program=Tk()
    app(program)
    program.mainloop()

