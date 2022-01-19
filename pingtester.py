import ipaddress, os
from tkinter import *

def click():
    rst = start.get()
    global i1 
    i1 = (rst)
    rst = end.get()
    global i2 
    i2 = (rst)
    print(i1,i2)
    ip_cal()

def ip_cal():
    start_ip = int(ipaddress.ip_address(i1))
    end_ip = int(ipaddress.ip_address(i2))

    for i in range(start_ip,end_ip+1):
        now =ipaddress.ip_address(i)
        print(now)
        os.system('start cmd.exe /k "mode con cols=75 lines=25 && ping %d -t "' %now)


window = Tk()
window.title("ping test")
window.geometry("240x240")
lbl=Label(window,font=("Arial",15))
lbl.grid(column=0,row=0)

Label(window, text="Start IP :", bg="light grey").grid(row=0, sticky=W)
Label(window, text="End IP :", bg="light grey").grid(row=1, sticky=W)

start = StringVar()
end = StringVar()

start = Entry(window)
start.grid(row=0, column=1)

end = Entry(window)
end.grid(row=1, column=1)

action = Button(window,text="Enter",command=click)
action.grid(column=10,row=1)

window.mainloop()