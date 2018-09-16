#Input in the entry boxes of 'Year', 'Month' and 'Day'
#Month must be written as a number between 1-12
#Press "Calculate" button to return weekday of the given date

from time import*
from tkinter import*
global months

#Definition of Months
months = ['January', 'january', 'February', 'february', 'March',
          'march', 'April', 'april', 'May', 'may', 'June', 'june',
          'July','july', 'August', 'august', 'September',
          'september','October', 'october','November', 'november',
          'December', 'december']

#User Interface
def main():
    root = Tk()
    root.title('Weekday Calculator')
    root.geometry('405x360')
    root.resizable(width = False, height = False)

    #Clear command
    def clear():
        Yeardisplay.delete(0,END)
        Monthdisplay.delete(0,END)
        Daydisplay.delete(0,END)
        Weekdaydisplay.configure(state='normal')
        Weekdaydisplay.delete(0, END)
        Weekdaydisplay.configure(state='readonly')
        
    #Calculate command
    def calculate():
        year = Yeardisplay.get()
        month = Monthdisplay.get()
        day = Daydisplay.get()
        
        if year.isdigit():
            if year[0] == '0':
                if len(year) == 1:
                    error_display('Year 0 does not exist')
                else:
                    error_display('Remove preceding zeros')     
            elif month.isdigit():
                month_digit(year, month, day)                   
            elif month in months:
                month = month.capitalize()
                month_to_int = {'January':1, 'February':2,
                'March':3, 'April':4,'May':5, 'June':6,
                'July':7, 'August':8, 'September':9,
                'October':10, 'November':11, 'December':12}
                Month = str(month_to_int[month])
                month_digit(year, Month, day)            
            else:
                output(year, month, day.lstrip('0'))               
        elif len(year) == 0:
            if len(month) == 0:
                if len(day) == 0:
                    error_display('')
                else:
                    error_display('Error')
            else:
                error_display('Error')
        else:
            error_display('Error')
            
    #Error handling regarding preceding zeros for day input
    def month_digit(year, month, day):
        if month[0] == '0':
            if len(month) > 2:
                error_display('Remove preceding zeros')
            else:
                day_digit(year, int(month), day)
        else:
            day_digit(year, int(month), day)
                    
    #Error handling regarding preceding zeros for day input
    def day_digit(year, month, day):
        if day.isdigit():
            if day[0] == '0':
                if len(day) > 2:
                    error_display('Remove preceding zeros')
                else:
                    output(year, month, day.lstrip('0'))
            else:
                output(year, month, day.lstrip('0'))
        else:
            output(year, month, day.lstrip('0'))


    #Error handling for month
    def output(year, month, day):
        try: 
            if (int(month) in [1,3,5,7,8,10,12]):
                condition(year, month, day, '31', '') 
            elif (int(month) in [4,6,9,11]):
                condition(year, month, day, '30', '') 
            elif int(month) == 2:
                if (((int(year) % 4) == 0 and
                not (int(year) % 100) == 0)
                or (int(year) % 400) == 0):
                    condition(year, month, day, '29', '') 
                else:
                    condition(year, month, day, '28', '29')
        except:
            error_display('Enter month between 1-12 or month name')
            
    #Error handling for day
    def condition(year, month, day, lastday, leapday):
        try:
            if len(day) == 0 or int(day) > int(lastday):
                error_display('Enter day between 1-' + lastday)
            elif int(day) <= int(lastday):
                change_display(message(year, month, day))
            elif day == leapday:
                error_display('Not a leap year')
        except:
            error_display('Enter day between 1-' + lastday)
            
    #Displays given weekday on the 'Weekday' entry box
    def change_display(text):
        Weekdaydisplay.configure(state='normal')
        Weekdaydisplay.delete(0,END)
        Weekdaydisplay.insert(INSERT, text)
        Weekdaydisplay.configure(state='readonly')
     
    #Error output
    def error_display(text):
        change_display(text)
        
    #Returns message for output on entry box
    def message(year, month, day): 
        weekday = ['Sunday', 'Monday', 'Tuesday',
        'Wednesday', 'Thursday', 'Friday', 'Saturday']
        a = int((14 - int(month))/12)
        y = int(year) - a
        m = int(month) + (12*a) -2
        d = (int(day) + y + int(y/4) - int(y/100) +
        int(y/400) + int((31*m)/12)) % 7
        x = weekday[d]
        name = wordmonth(month)
        Day = ordinal(day)
        
        StrYear = int(strftime('%Y'))
        StrMonth = int(strftime('%m'))
        StrDay = int(strftime('%d'))
        DisplayTime = JulianDN(year, month, day)
        CurrentDate = JulianDN(StrYear, StrMonth, StrDay)

        if DisplayTime == CurrentDate:
            message = r_output('Today is a ', x)
        elif DisplayTime == CurrentDate + 1:
            message = r_output('Tomorrow will be a ', x)
        elif DisplayTime == CurrentDate - 1:
            message = r_output('Yesterday was a ', x)
        elif DisplayTime > CurrentDate:
            message = g_output(name, Day, year, ' will be a ', x)
        elif DisplayTime < CurrentDate:
            message = g_output(name, Day, year, ' was a ', x)
        return message

    #Output if given date is today, yesterday or tomorrow
    def r_output(text, day_of_week):
        output = (text + day_of_week)
        return output

    #Output for days before or after current date
    def g_output(Month, Day, Year, text, day_of_week):
        output = (Month + ' ' + Day + ', ' + Year + text + day_of_week)
        return output

    #Returns ordinal for given day number
    def ordinal(day):
        teen_numbers = [11, 12, 13, 14, 15, 16, 17, 18, 19]
        output = ['th','st', 'nd', 'rd', 'th', 'th',
                    'th', 'th', 'th', 'th', 'th']
        if int(day) in teen_numbers:
            return (day + 'th')
        else:
            return (day + output[int(day[-1])])

    #Calculates given weekday with Julian Date Number
    def JulianDN(Y,M,D):
        a = int((14 - int(M))/12)
        y = int(Y) + 4800 - a
        m = int(M) + (12 * a) - 3
        JDN = (int(D) + int(((153 * m) + 2) /5) + (365 * y)
        + int(y/4) - int(y/100) + int(y/400) - 32045)
        return JDN

    #Return month name from input
    def wordmonth(month):
        monthname = [word for word in months if word.istitle()]
        Month = int(month) -1
        return monthname[Month]
        
    #Title
    Title = Label(root, text= "Weekday Calculator", font = ('Avenir', 18, 'normal'))
    Title.grid(column = 0, columnspan = 7, padx = 5, pady = 5)

    #Description
    Description = Label(root,
    text= 'This program determines the specific weekday for given dates \n|'
           'Year (yyyy) | Month (mm) | Day (dd) |',
    font = ('Avenir', 13, 'normal'))
    Description.grid(row = 1, column = 0, columnspan = 7, padx = 5, pady = 5)

    #Entry Boxes
    Year = Label(root, padx = 9, text = 'Year:', font = ('Avenir', 13, 'normal'))
    Year.grid(row = 2, sticky = W, padx = 1)
    Yeardisplay = Entry(root, width = 33)
    Yeardisplay.grid(row = 2, column = 1, sticky = E)

    Month = Label(root, padx = 9, text = 'Month:', font = ('Avenir', 13, 'normal'))
    Month.grid(row = 3, sticky = W, padx = 0)
    Monthdisplay = Entry(root, width = 33)
    Monthdisplay.grid(row = 3, column = 1, sticky = E)

    Day = Label(root, padx = 9, text = 'Day:', font = ('Avenir', 13, 'normal'))
    Day.grid(row = 4, sticky = W, padx = 0)
    Daydisplay = Entry(root, width = 33)
    Daydisplay.grid(row = 4, column = 1, sticky = E)

    Week = Label(root, padx = 9, text= 'Weekday:', font = ('Avenir', 13, 'normal'))
    Week.grid(row = 5, sticky = W, padx = 0)
    Weekdaydisplay = Entry(root, width = 33, state = 'readonly')
    Weekdaydisplay.grid(row = 5, column = 1, sticky = E)

    #Calculate Button
    Calculate = Button(text = 'Calculate', command = calculate, font = ('Avenir', 15, 'normal'))
    Calculate.grid(row = 6, column = 0, columnspan = 8, padx = 10, pady = 5, sticky =  N+S+E+W)

    #Clear Button
    clear = Button(text = 'Clear', command = clear, font = ('Avenir', 15, 'normal'))
    clear.grid(row = 7, column = 0, columnspan = 8, padx = 10, pady = 5, sticky =  N+S+E+W)

    #Exit Button
    Exit = Button(text = 'Exit', command = root.destroy, font = ('Avenir', 15, 'normal'))
    Exit.grid(row = 8, column = 0, columnspan = 8, padx = 10, pady = 5, sticky =  N+S+E+W)

    #Credits
    Credits = Label(root, text = 'Raymond Wang 2018 ®', font = ('Avenir', 15, 'italic'))
    Credits.grid(row = 9, column = 0, columnspan = 8, pady = 5, padx = 5)

    root.mainloop()

if __name__ == "__main__":
    main() 

