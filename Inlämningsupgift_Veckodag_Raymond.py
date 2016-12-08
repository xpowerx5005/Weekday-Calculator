#Inlämningsuppgift: Veckodag
#Raymond Wang
#Mata in år, månad och dag i fälten 'Year', 'Month', respektive 'Day'
#Månad matas in som en siffra 1-12
#Klicka sedan på knappen 'Calculate' för att returnera veckodagen för datument

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
    try:
        year = int(Yeardisplay.get())
        month = int(Monthdisplay.get())
        day = int(Daydisplay.get())
        if month == 2:
            if (((year % 4) == 0 and not (year % 100) == 0) or (year % 400) == 0):
                if day <= 29:
                    Weekdaydisplay.delete(0,END)
                    Weekdaydisplay.insert(INSERT,calculate(year, month, day))
                else:
                    Yeardisplay.delete(0,END)
                    Yeardisplay.insert(INSERT,'Error')
                    Monthdisplay.delete(0, END)
                    Monthdisplay.insert(INSERT,'Error')
                    Daydisplay.delete(0,END)
                    Daydisplay.insert(INSERT,'Error')
                    Weekdaydisplay.delete(0,END)
                    Weekdaydisplay.insert(INSERT,'Error')
            else:
                if day <= 28:
                    Weekdaydisplay.delete(0,END)
                    Weekdaydisplay.insert(INSERT,calculate(year, month, day))
                else:
                    Yeardisplay.delete(0,END)
                    Yeardisplay.insert(INSERT,'Error')
                    Monthdisplay.delete(0, END)
                    Monthdisplay.insert(INSERT,'Error')
                    Daydisplay.delete(0,END)
                    Daydisplay.insert(INSERT,'Error')
                    Weekdaydisplay.delete(0,END)
                    Weekdaydisplay.insert(INSERT,'Error')
                    
        elif month == 1 or month == 3 or month == 5 or month == 7 or month == 8 or month == 10 or month == 12:
            if day <= 31:
                Weekdaydisplay.delete(0,END)
                Weekdaydisplay.insert(INSERT,calculate(year, month, day))
            else:
                Yeardisplay.delete(0,END)
                Yeardisplay.insert(INSERT,'Error')
                Monthdisplay.delete(0, END)
                Monthdisplay.insert(INSERT,'Error')
                Daydisplay.delete(0,END)
                Daydisplay.insert(INSERT,'Error')
                Weekdaydisplay.delete(0,END)
                Weekdaydisplay.insert(INSERT,'Error')
                    
        elif month == 4 or month == 6 or month == 9 or month == 11:
            if day <= 30:
                Weekdaydisplay.delete(0,END)
                Weekdaydisplay.insert(INSERT,calculate(year, month, day))
            else:
                Yeardisplay.delete(0,END)
                Yeardisplay.insert(INSERT,'Error')
                Monthdisplay.delete(0, END)
                Monthdisplay.insert(INSERT,'Error')
                Daydisplay.delete(0,END)
                Daydisplay.insert(INSERT,'Error')
                Weekdaydisplay.delete(0,END)
                Weekdaydisplay.insert(INSERT,'Error')
        else:
            Yeardisplay.delete(0,END)
            Yeardisplay.insert(INSERT,'Error')
            Monthdisplay.delete(0, END)
            Monthdisplay.insert(INSERT,'Error')
            Daydisplay.delete(0,END)
            Daydisplay.insert(INSERT,'Error')
            Weekdaydisplay.delete(0,END)
            Weekdaydisplay.insert(INSERT,'Error')
            
    except ValueError:
        Yeardisplay.delete(0,END)
        Yeardisplay.insert(INSERT,'Error')
        Monthdisplay.delete(0, END)
        Monthdisplay.insert(INSERT,'Error')
        Daydisplay.delete(0,END)
        Daydisplay.insert(INSERT,'Error')
        Weekdaydisplay.delete(0,END)
        Weekdaydisplay.insert(INSERT,'Error')

def calculate(year, month, day): 
    a = int((14 - month)/12)
    y = year - a
    m = month + (12*a) -2

    d = (day + y + int(y/4) - int(y/100) + int(y/400) + int((31*m)/12)) % 7    
        
    if d == 0:
        return (wordmonth(month) + ' ' + str(day) + ' , ' + str(year) + ' is a Sunday')
    elif d == 1:
        return (wordmonth(month) + ' ' + str(day) + ' , ' + str(year) + ' is a Monday')
    elif d == 2:
        return (wordmonth(month) + ' ' + str(day) + ' , ' + str(year) + ' is a Tuesday')
    elif d == 3:
        return (wordmonth(month) + ' ' + str(day) + ' , ' + str(year) + ' is a Wednesday')
    elif d == 4:
        return (wordmonth(month) + ' ' + str(day) + ' , ' + str(year) + ' is a Thursday')
    elif d == 5:
        return (wordmonth(month) + ' ' + str(day) + ' , ' + str(year) + ' is a Friday')
    elif d == 6:
        return (wordmonth(month) + ' ' + str(day) + ' , ' + str(year) + ' is a Saturday')

def wordmonth(month):
    if month == 1:
        return 'January'
    elif month == 2:
        return 'February'
    elif month == 3:
        return 'March'
    elif month == 4:
        return 'April'
    elif month == 5:
        return 'May'
    elif month == 6:
        return 'June'
    elif month == 7:
        return 'July'
    elif month == 8:
        return 'August'
    elif month == 9:
        return 'September'
    elif month == 10:
        return 'October'
    elif month == 11:
        return 'November'
    elif month == 12:
        return 'December'

    
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
Credits = Label(root, text = "Raymond Wang 2016 ®", font = ('Avenir', 15, 'italic'))
Credits.grid(row = 9, column = 0, columnspan = 7, pady = 5, padx = 5)

root.mainloop()
