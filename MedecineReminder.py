import tkinter as tk
from tkinter import messagebox
import datetime

reminderrunning=False
def checkreminder():
    global reminderrunning
    if not reminderrunning:
        return 

    Now = datetime.datetime.now()
    timenow=Now.strftime("%H:%M")
    timenowD=datetime.datetime.strptime(timenow,"%H:%M")

    hours=hourspin.get()
    minutes=minutespin.get()
    MedReminder = f"{hours}:{minutes}"
    MedReminderD=datetime.datetime.strptime(MedReminder,"%H:%M")
    
    DoseTake = dose1.get()
    Medicine_Name = medicineentry.get()


    if timenowD == MedReminderD:
        messagebox.showwarning("MedicineReminder",f"Time to take your {DoseTake} dose of {Medicine_Name}")
   
    root.after(1000, checkreminder)
    


def ReminderStart():
    global reminderrunning
    reminderrunning=True
    messagebox.showinfo("Medicine Reminder","Reminder has started sucessfully")
    checkreminder()
def ReminderStop():
    global reminderrunning
    reminderrunning=False
    messagebox.showinfo("Medicine Reminder","Reminder stopped sucessfully.")


root=tk.Tk()
root.title("Medicine Reminder App 💊")
root.geometry("380x420")
root.resizable(False,False)



medecinelabel=tk.Label(root,text="Medicine Reminder",font=("Arial",16,"bold"))
medecinelabel.grid(row=0,column=0,columnspan=2)


medicineName=tk.Label(root,text="Medicine Name")
medicineName.grid(row=1,column=0,pady=15)

medicineentry=tk.Entry(root, width=30)
medicineentry.grid(row=1,column=1,pady=15)



dosetype=tk.Label(root,text="Dose Type").grid(row=2,column=0,columnspan=2,pady=15)
dose1=tk.StringVar(value="Morning")
reminderrunning=False
tk.Radiobutton(root,text="Morning",variable=dose1,value="Morning").grid(row=3,column=0)
tk.Radiobutton(root,text="Evening",variable=dose1,value="Evening").grid(row=3,column=1)



remindertime=tk.Label(root,text="Reminder Time (HH:MM)").grid(row=4,column=0,columnspan=2,pady=15)
hourspin=tk.Spinbox(root,from_=0,to=23,width=5)
hourspin.grid(row=5,column=0)



minutespin=tk.Spinbox(root,from_=0,to=59,width=5)
minutespin.grid(row=5,column=1)



startreminder=tk.Button(root, text="Start Reminder",font=("Arial",15),bg="green",fg="white",command=ReminderStart)
startreminder.grid(row=6,column=0,pady=15,padx=15)
stopreminder=tk.Button(root, text="Stop Reminder",font=("Arial",15),bg="red",fg="white",command=ReminderStop).grid(row=6,column=1,pady=15)
root.mainloop()

