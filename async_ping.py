import os,sys,threading,time,subprocess,requests,pexpect,asyncio,multiprocessing;from termcolor import colored;error_handler=lambda *args:print(colored("[!]","white","on_red",attrs=["bold"])+" "+args[0])
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
def ping(ip):outp=(outp:=(subprocess.check_output(["ping",ip,"-c","2"])).decode("utf-8").split("\n"))[[True if "transmitted" in x else False for x in outp].index(True)].split(",")[:2]   ;return(["".join([j if j in [str(a) for a in range(10)]else "" for j in objx]) for objx in outp])
if __name__ == "__main__":
  targetip="1.1.1.1";pool=multiprocessing.Pool() 
  tasks=[]
  tasks.append(pool.apply_async(ping, args=([targetip])))
  tasks.append(pool.apply_async(ping, args=([targetip])))
  tasks.append(pool.apply_async(ping, args=([targetip])))
  tasks.append(pool.apply_async(ping, args=([targetip])))
  tasks.append(pool.apply_async(ping, args=([targetip])))
  tasks_results=complete_pool(tasks)
  print(tasks_results)
  




