from tkinter import *
from tkinter import messagebox
from scapy.all import rdpcap
from scapy.all import *
import math

#############################################################################


############################################################################

def live():
    pass

def IP():
    p = rdpcap(path)
    global src_addr
    src_addr = []
    for i in range(len(p)):
        if p[i]['IP'].src not in src_addr:
            src_addr.append(p[i]['IP'].src)
    messagebox.showinfo("IPs",src_addr+["    "])

def Subnet():
    p = rdpcap(path)
    global src_addr
    src_addr = []
    for i in range(len(p)):
        if p[i]['IP'].src not in src_addr:
            src_addr.append(p[i]['IP'].src)
    src_addr_count = []
    src_addr_count = [0]*(len(src_addr))
    for i in range(len(p)):
        for j in range(len(src_addr)):
            if p[i]['IP'].src == src_addr[j]:
                src_addr_count[j]+=1
    messagebox.showinfo("number of packets",(src_addr,src_addr_count))
def Port():
    pass

def Alerts():
    p = rdpcap('/root/Downloads/udp_refined.pcap')
    src_addr = []
    for i in range(len(p)):
        if p[i]['IP'].src not in src_addr:
            src_addr.append(p[i]['IP'].src)
    print(src_addr)

    src_addr_count = []
    src_addr_count = [0]*(len(src_addr))
    for i in range(len(p)):
        for j in range(len(src_addr)):
            if p[i]['IP'].src == src_addr[j]:
                src_addr_count[j]+=1
    print(src_addr_count)
    for i in range(len(src_addr)):
        print("number of 100 threshold alerts for " + str(src_addr[i]) + " is " +str(int(math.floor(src_addr_count[i]/100))))
        print("number of 1000 threshold alerts for "+ str(src_addr[i]) + " is " +str(int(math.floor(src_addr_count[i]/1000))))
        print("number of 5000 threshold alerts for "+ str(src_addr[i]) + " is " +str(int(math.floor(src_addr_count[i]/5000))))

def start_pcap_analysis():
    root.destroy()
    global root
    root = Tk()

    print(path)
    label0 = Label(root, text = "Action to be performed", bg = "green")
    button1 = Button(root, text = "All IP connections", command = IP)
    button2 = Button(root, text = "All subnets connections", command = Subnet)
    button3 = Button(root, text = "Alerts descriptions", command = Alerts)
    
    label0.grid(row = 0)
    button1.grid(row = 1, column = 0)
    button2.grid(row = 1, column = 1)
    button3.grid(row = 2, column = 0)

    root.mainloop()

def pcap():
    root.destroy()
    global root
    def pcap_action():
        global path
        path = entry7.get()
        messagebox.showinfo("hi","reached")
        start_pcap_analysis()
    root = Tk() 

    label0 = Label(root, text = "Pcap File Study", bg = "green", font = 20)
    label1 = Label(root, text = "Path of the file")
    entry7 = Entry(root)
    button = Button(root, text = "Submit", command = pcap_action)

    label0.grid(row = 0)
    label1.grid(row = 1, column = 0)
    entry7.grid(row = 1, column = 1)
    button.grid(row = 2, column = 1)

    root.mainloop()

def func_after_validation():
    global root
    root = Tk()

    label1 = Label(root, text = "Choose your option", bg = "green", font = 20)
    button1 = Button(root, text = "Study existing pcap file", command = pcap)
    button2 = Button(root, text = "Live Network study", command = live)

    label1.grid(row = 0)
    button1.grid(row = 1)
    button2.grid(row = 2)

    root.mainloop()

def validation():
    if((entry1.get() == " " and entry2.get() == " ") or(entry1.get() =="Rishabh" and entry2.get() == "Kumar") or (entry1.get() == "Shekhar" and entry2.get() == "Lohach")):
        messagebox.showinfo("Great", "Login Successful")
        root.destroy()
        func_after_validation()
    else:
        messagebox.showinfo("Not great", "Login Unsuccessful")

##############################################################################

root = Tk()

label0 = Label(root, text = "Welcome to mapping tool", bg = "green" , font = 20)
label1 = Label(root, text = "Enter your Username")
entry1 = Entry(root) 
label2 = Label(root, text = "Enter your password")
entry2 = Entry(root)
button1 = Button(root, text = "Submit", command = validation)

label0.grid(row = 0, columnspan = 2)
label1.grid(row = 1, column = 0)
entry1.grid(row = 1, column = 1)
label2.grid(row = 2, column = 0)
entry2.grid(row = 2, column = 1)
button1.grid(row = 3, column = 1)

root.mainloop()
