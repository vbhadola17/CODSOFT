#importing module
from tkinter import *
from tkinter import messagebox

#creating function
def newTask():
    task=my_entry.get()
    if task != "":
        lb.insert(END, task)
        my_entry.delete(0,"end")
    else:
        messagebox.showwarning("warning","enter some task.")
def deleteTask():
    lb.delete(ANCHOR)

#configuring & creating mainwindow
ws=Tk()
ws.geometry("500x450+500+200")
ws.title("pythonguides")
ws.config(bg="#223441")
ws.resizable(width=False,height=False)

#creating frame
frame=Frame(ws)
frame.pack(pady=10)
#adding listbox
lb=Listbox(frame,width=25,height=8,font=('roman',18),
bd=0,fg='#464646',highlightthickness=0,
selectbackground='#a6a6a6',activestyle='none',)
lb.pack(side=LEFT, fill=BOTH)

#Addition of data
task_list=['wake up','drink water','yoga','work','lunch',
'nap','work']
for item in task_list:
    lb.insert(END,item)

#addition of scrollbars
sb=Scrollbar(frame)
sb.pack(side=RIGHT,fill=BOTH)

lb.config(yscrollcommand=sb.set)
sb.config(command=lb.yview)

#addition of entry box
my_entry=Entry(ws,font=('times',24))
my_entry.pack(pady=20)

#addition of another frame for buttons
button_frame=Frame(ws)
button_frame.pack(pady=20)

#adding buttons
addTask_button=Button(button_frame,text='add task',
font=('times',14), bg='#c5f776',padx=20,pady=10,command=newTask)
addTask_button.pack(fill=BOTH,expand=True,side=LEFT)

delTask_button=Button(
    button_frame,
    text='Delete Task',
    font=('times 14'),
    bg='#ff8b61',
    padx=20,
    pady=10,
    command=deleteTask
)
delTask_button.pack(fill=BOTH, expand=True, side=LEFT)

ws.mainloop()