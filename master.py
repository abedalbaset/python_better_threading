import os
import time
import threading

dir='thread_class.py variable'
def start_script():
    action = os.system("python "+dir)

obj=[]

def start_script_as_thread():
    th = threading.Thread(target=start_script)
    obj.append(th)
    obj[len(obj)-1].start()


start_script_as_thread()
