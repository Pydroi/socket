import pyautogui
import threading
import time
time.sleep(3)
msg="hi"#what msg?
msg=str(msg)
MX=1000#max amount of msg





def spam(msgq):
    count=0
    while count<MX:
        pyautogui.typewrite(msgq)
        pyautogui.moveTo(1801,978)#send button
        pyautogui.leftClick()#ledt click
        count+=1

spam(msg)
  
#send=threading.Thread(target=spam  ,args=(msg,) ,daemon=True)
#send_2=threading.Thread(target=spam  ,args=(msg,) )

#send_2.start()

#print(pyautogui.position())
