
import tkinter
from tkinter import*
from tkinter import messagebox

todo = tkinter.Tk()
todo.title ("ToDo List")
todo.geometry("500x400")
todo.configure(bg = "bisque")
todo.resizable(False,False)

tasks = []

def addTask():
    task = task_var.get()
    if not task:
        messagebox.showinfo('Empty Entry','Enter a task')
    else:
        tasks.append(task)
        taskList.insert(END, task)
        # store tasks in txt file ie tasks is a list thus use this to write its contents to the txt file use 'a' append instead of 'w' to ensure other tasks are added to the file when program is run later.
        with open('taskfile.txt','a') as filehandle:
            for task in tasks:
                filehandle.write('%s\n' % task)


def listUpdate():
    clearList()
    for i in tasks:
        taskList.insert(END,i)# adds to the end of the list

def delete():
    clicked_task = taskList.curselection()
    for task in clicked_task:
        taskList.delete (task)
        if not task:
            messagebox.showinfo('Cannot Delete', 'No task was selected') 
def deleteAll():
    response = messagebox.askyesno('Delete All','Do you want to delete all tasks?') #use askyesno function to confirm response from user
    if response==True:
        while(len(tasks)!=0):
            tasks.pop()
            #print (tasks)
        clearList()

def clearList():
    taskList.delete(0,END)# deletes in range of specified indices 

task_var = StringVar()
taskLabel = tkinter.Label(todo, text="Enter a task: ", font=("times new roman",14),bg="white")
taskInput = Entry(todo,width=20,bd=2, font=("Verdana,18"),justify="right", textvariable=task_var)
addButton = Button (todo,text="Add a task",font=("times new roman",12),relief="groove",bd=2,bg="white",fg="black",command = addTask)
deleteButton = Button (todo,text="Delete a task",font=("times new roman",12),relief="groove",bd=2,bg="white",fg="black",command=delete)
deleteAllButton = Button (todo,text="Delete all",font=("times new roman",12),relief="groove",bd=2,bg="white",fg="black",command = deleteAll)
taskList = Listbox (todo, height= 15, width=25,bg="white",fg= "black",selectmode='SINGLE') #use listbox to display all tasks.

taskLabel.place(x=40,y=50,width=150,height=30)
taskInput.place(x=40,y=90,width=200,height=30)
addButton.place(x=40,y=150,width=150,height=30)
deleteButton.place(x=40,y=200,width=150,height=30)
deleteAllButton.place(x=40,y=250,width=150,height=30)
taskList.place (x=270,y=50)

listUpdate()
todo.mainloop()



