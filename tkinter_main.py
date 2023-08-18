from tkinter import *;import multiprocessing,subprocess,random

def complete_pool(tasks):
  while 1:
    #try:
    #  ()if(True)in[(True)if(task.successful())else(False)for(task)in(tasks)]else(print("Not all thread tasks have been successful!"));break
    #except:()
    try:
      for task in tasks:
        task.wait()
        print("waiting")
    except:""
  results=[]
  for(task)in(tasks):
    try:
      if(task.get()!=None):
        for(found)in(task.get()):results.append(found)
    except:()
  return results


def ping(ip):
  outp=(outp:=(subprocess.check_output(["ping",ip,"-c","3"])).decode("utf-8").split("\n"))[[True if "transmitted" in x else False for x in outp].index(True)].split(",")[:2]   
  print(outp)
  results=(["".join([j if j in [str(a) for a in range(10)]else "" for j in objx]) for objx in outp])
  return results

def check(update,entry,submit):
  ip=entry.get()
  if len(ip)>15:update.configure(text="IPv4 too long!",bg="black",fg="red")
  elif "."not in ip:update.configure(text="Enter valid IPv4!",bg="black",fg="red")
  elif " "in ip:update.configure(text="No whitespace!",bg="black",fg="red")
  elif True in [False if c in [str(f) for f in range(10)]+["."] else True for c in ip]:update.configure(text="No letters!",bg="black",fg="red")
  else:
    #try:
      if len(ip.split("."))!=4:update.configure(text="Incorrect IPv4 format!",bg="black",fg="red")
      elif True in [True if int(x)>=256 else False for x in ip.split(".")]:update.configure(text="Maximum: 255!",bg="black",fg="red")
      else:
        entry.configure(state="disabled")
        update.configure(text="Pinging...",bg="black",fg="green")
        submit.configure(state="disabled")
        with multiprocessing.Pool() as pool:
          tasks=[]
          tasks.append(pool.apply_async(ping, args=([ip])))
          print("beginning")
          print(complete_pool(tasks))
    #except:update.configure(text="Please re-enter!",bg="black",fg="red")

def main_menu(*args):
  for frame in args[1:]:frame.destroy()
  CENTRAL_WINDOW.geometry("400x200")
  main_frame=Frame(CENTRAL_WINDOW);main_frame["bg"]="black"
  main_frame.pack(anchor=CENTER)
  update=Label(main_frame,text="Please enter an IPv4",fg="white",bg="black")
  update.grid(column=0,row=1,pady=1,padx=1,sticky=W)
  entry=Entry(main_frame,bd=5,bg="black",fg="white")
  entry.grid(column=0,row=0,sticky=W)
  submit=Button(main_frame,text="Check",width=10,command=lambda:check(update,entry,submit),bg="black",fg="red")
  submit.grid(column=1,row=0,pady=1,padx=1)


if __name__ == "__main__":
  CENTRAL_WINDOW=Tk();CENTRAL_WINDOW["bg"]="black";CENTRAL_WINDOW.title("Automating Reconnaissance GUI")
  main_menu(CENTRAL_WINDOW)
  CENTRAL_WINDOW.mainloop()


