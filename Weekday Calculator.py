#Input in the entry boxes of 'Year', 'Month' and 'Day'
#Month must be written as a number between 1-12
#Press "Calculate" button to return weekday of the given date

import time
from tkinter import *

root = Tk()
root.title("Weekday Calculator")
root.geometry('390x340')
root.resizable(width = False, height = False)
    
#Clear command
def clear():
    Yeardisplay.delete(0,END)
    Monthdisplay.delete(0,END)
    Daydisplay.delete(0,END)
    Weekdaydisplay.delete(0, END)
    
#Convert command
def convert():
    year = (Yeardisplay.get())
    month = (Monthdisplay.get())
    day = (Daydisplay.get())
    if  True in [f == '1' or f == '2' or f == '3'
    or f == '4' or f == '5' or f == '6' or f == '7'
    or f == '8' or f == '9' for f in year and month and day]:
        if int(month) <= 12:
            if int(month) == 2:
                if (((int(year) % 4) == 0 and
                not (int(year) % 100) == 0)
                or (int(year) % 400) == 0):
                    if int(day) <= 29:
                        change_display()
                    else:
                        error_display('Error') 
                else:
                    if int(day) <= 28:
                        change_display()
                    else:
                        error_display() 
            if (int(month) in [1,3,5,7,8,10,12]):
                if int(day) <= 31:
                    change_display()
                else:
                    error_display(s) 
            elif (int(month) in [4,6,9,11]):
                if int(day) <= 30:
                    change_display()
                else:
                    error_display('Error') 
        else:
            error_display('Error')             
    else:
        if year == '':
            if month == '':               
                if day == '':
                    error_display('')                     
                else:
                    error_display('Error')              
            else:
                error_display('Error')       
        else:
            error_display('Error')
            
def change_display():
    Weekdaydisplay.delete(0,END)
    Weekdaydisplay.insert(INSERT, message())
    
def error_display(s):
    Yeardisplay.delete(0,END)
    Yeardisplay.insert(INSERT, s)
    Monthdisplay.delete(0, END)
    Monthdisplay.insert(INSERT, s)
    Daydisplay.delete(0,END)
    Daydisplay.insert(INSERT, s)
    Weekdaydisplay.delete(0, END)
    Weekdaydisplay.insert(INSERT, s)

def message(): 
    year = Yeardisplay.get()
    month = Monthdisplay.get()
    day = Daydisplay.get()
    weekday = ['Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday']
    a = int((14 - int(month))/12)
    y = int(year) - a
    m = int(month) + (12*a) -2
    d = (int(day) + y + int(y/4) - int(y/100) + int(y/400) + int((31*m)/12)) % 7
    
    StrYear = int(time.strftime("%Y"))
    StrMonth = int(time.strftime("%m"))
    StrDay = int(time.strftime("%d"))
    DisplayTime = JulianDN(year, month, day)
    CurrentDate = JulianDN(StrYear, StrMonth, StrDay)

    if DisplayTime == CurrentDate:
        message = (' Today is a ' + weekday[d])
    elif DisplayTime == CurrentDate + 1:
        message = (' Tomorrow will be a ' + weekday[d])
    elif DisplayTime == CurrentDate - 1:
        message = (' Yesterday was a ' + weekday[d])
    elif DisplayTime > CurrentDate:
        message = (wordmonth(month) + ' ' + day + ' , ' + year + ' will be a ' + weekday[d])
    elif DisplayTime < CurrentDate:
        message = (wordmonth(month) + ' ' + day + ' , ' + year + ' was a ' + weekday[d])
    return message

def JulianDN(Y,M,D):
    a = int((14 - int(M))/12)
    y = int(Y) + 4800 - a
    m = int(M) + (12 * a) - 3
    JDN = int(D) + int(((153 * m) + 2) /5) + (365 * y) + int(y/4) - int(y/100) + int(y/400) - 32045
    return JDN

def wordmonth(month):
    monthname = ['January', 'February', 'March', 'April', 'May', 'June',
              'July', 'August', 'September', 'October', 'November', 'December']
    month = int(Monthdisplay.get()) -1
    return monthname[month]

#Title
Title = Label(root, text= "Weekday Calculator", font = ('Avenir', 18, 'normal'))
Title.grid(column = 0, columnspan = 7, padx = 5, pady = 5)

#Description
Description = Label(root, text= "This program determines the weekday of any given dates", font = ('Avenir', 15, 'normal'))
Description.grid(row = 1, column = 0, columnspan = 7, padx = 5, pady = 5)

#Entry Boxes
Year = Label(root, padx = 9, text = "Year (yyyy):", font = ('Avenir', 15, 'normal'))
Year.grid(row = 2, sticky = W, padx = 0)
Yeardisplay = Entry(root, width = 33)
Yeardisplay.grid(row = 2, column = 1, sticky = E)

Month = Label(root, padx = 9, text = "Month (mm):", font = ('Avenir', 15, 'normal'))
Month.grid(row = 3, sticky = W, padx = 0)
Monthdisplay = Entry(root, width = 33)
Monthdisplay.grid(row = 3, column = 1, sticky = E)

Day = Label(root, padx = 9, text = "Day (dd):", font = ('Avenir', 15, 'normal'))
Day.grid(row = 4, sticky = W, padx = 0)
Daydisplay = Entry(root, width = 33)
Daydisplay.grid(row = 4, column = 1, sticky = E)

Week = Label(root, padx = 8, text="Weekday:", font = ('Avenir', 15, 'normal'))
Week.grid(row = 5, sticky = W, padx = 0)
Weekdaydisplay = Entry(root, width = 33)
Weekdaydisplay.grid(row = 5, column = 1, sticky = E)

#Calculate Button
Convert = Button(text = "Calculate", command = convert, font = ('Avenir', 15, 'normal'))
Convert.grid(row = 6, column = 0, columnspan = 15, padx = 10, pady = 5, sticky =  N+S+E+W)

#Clear
clear = Button(text = "Clear", command = clear, font = ('Avenir', 15, 'normal'))
clear.grid(row = 7, column = 0, columnspan = 18, padx = 10, pady = 5, sticky =  N+S+E+W)

#Exit Button
Exit = Button(text = 'Exit', command = root.destroy, font = ('Avenir', 15, 'normal'))
Exit.grid(row = 8, column = 0, columnspan = 15, padx = 10, pady = 5, sticky =  N+S+E+W)

#Credits
Credits = Label(root, text = "Raymond Wang 2016 - 2017 ®", font = ('Avenir', 15, 'italic'))
Credits.grid(row = 9, column = 0, columnspan = 7, pady = 5, padx = 5)

root.mainloop()
