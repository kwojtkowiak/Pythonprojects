#Timer that is used to calculate time in app
import time
import datetime

import tkinter
from tkinter import messagebox
import winsound

#Main script - getting current time, adding 25 mins
ct = datetime.datetime.now() #current time
pomodoro_t = 25*60 #pomodoro duration in secs (25 mins)
delta_t = datetime.timedelta(0,pomodoro_t) #time duration
fut_t = ct + delta_t #future time when pomodoro finishes
break_t = 5*60 #break time after pomodoro, 5 mins
finished_t = ct + datetime.timedelta(0,pomodoro_t + break_t) #final time with 5 min break  

#GUI
root = tkinter.Tk() #hiding tkinter's main window. Only alert message box
root.withdraw()

messagebox.showinfo("Pomodoro started!", "\nIt is now " +ct.strftime("%H:%M") + " hrs. \nTimer set for 25 mins.")

total_pomodoros = 0
breaks = 0 #counters 

#Main part
while True:
    #Pomodoro
    if ct < fut_t:
        print("pomodoro")
    #past pomodoro time, break time
    elif fut_t <= ct <= finished_t:
        #check if it is first time, if so ring a bell
        print("in break")
        if breaks == 0:
            print("in break")
            #Sound signal
            for i in range(5):
                winsound.Beep((i+100),700)
            print("Break time!")
            breaks += 1
    #pomodoro and break finished. Check if ready for another pomodoro
    else:
        print("finished")
        #Pomodoro finished. Reset breaks.
        breaks = 0
        #Let the user know that the break is over
        for i in range(10):
            winsound.Beep((i+100),500)
        #Ask if user wants to start again
        usr_ans = messagebox.askyesno("Pomodoro finished!","Would you like to start another run?")
        total_pomodoros += 1
        if usr_ans == True:
            #user wants another pomodoro. Updating values
            ct = datetime.datetime.now()
            fut_t = ct + datetime.timedelta(0,pomodoro_t)
            finished_t = ct + datetime.timedelta(0,pomodoro_t+break_t)
            continue
        elif usr_ans == False:
            #user does not want to continue
            messagebox.showinfo("Pomodoro finished!","\nYou completed"+str(total_pomodoros)+" pomodoros today!")
            break
    #refresh every 20 sec and update time
    print("sleeping")
    time.sleep(20)
    ct = datetime.datetime.now()
    timenow = ct.strftime("%H:%M")