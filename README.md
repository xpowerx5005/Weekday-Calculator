# Weekday-Calculator
This program calculates the weekday of every given date. 
Input in the entry boxes of 'Year', 'Month' and 'Day'.
Month must be written as a number between 1-12.
Press "Calculate" button to return weekday of the given date.

# Specifikation

## Inledning
Jag tänkte programmera en bankapplikation för bankkunder med funktionerna saldo, överföring och transaktionshistorik. Programmet ska köras i en terminal och användarna ska kunna logga in med lösenord och presenteras med en meny där de kan komma åt bankens funktionalitet eller avsluta. Överst i menyn ska användarens saldo stå.

En av de största utmaningarna är att se till att användarna inte kan fuska och ta ut mer pengar än vad som finns på kontot eller stjäla pengar från andra konton.

## Användarscenarier
### Överföra pengar
Beatrices son har bett om extra pengar för att klara sig till slutet av månaden. De har kommit överens om att hon ska överföra 2000kr. Beatrice loggar in på banken med sitt lösenord. Hon väljer "överföringar" i huvudmenyn och bes mata in kontonummer. Hon skriver in sin sons kontonummer 3141592 och prompten frågar om hur många kronor hon vill överföra. Hon väljer 2000 kr. När hon matat in summan frågas hon en extra gång om hon vill överföra 2000 kr till det kontot och hon väljer ja. Bankprogrammet berättar att pengarna har överförts. Beatrice väljer "logga ut" i menyn och loggas ut från banken.
### Saldo
Beatrices son vill kolla att en transaktion från mamman har kommit in på hans konto. Sonen som heter Ludwig loggar in på banken och ser direkt ovanför menyn att han har 2000kr på kontot. "Nice!" utbrister Ludwig och loggar ut med ett léende.
### Transaktionshistorik
Sten misstänker att någon har snappat upp hans kreditkortsnummer när han köpte högtalarkablar på en mystisk webbplats. För att försäkra sig om att det inte har hänt så startar han bankprogrammet och loggar in med sitt lösenord. Han presenteras med en meny och väljer transaktionshistorik. Där ser han bara transaktioner som han känner igen som sina egna och drar en lättnadens suck. Efter alla transaktioner står det "Tryck en tangent för att återvända till menyn". Ste återvänder till huvudmenyn, loggar ut och återvänder till vardagen med ett varaktigt lugn.
# Kodskelett
```
class bank(object):
	"""The bank manages all accounts through the menu."""
	def bank(database = "accounts.utf8"):
		"""Create a bank with the accounts found in the file
		"accounts.txt" or another specified file."""
		pass
	
	def menu(self, account_number):
		"""Show the menu for the user with account_number. Shows his 
		balance and the options transfer, show transaction history 
		or quit."""
		pass
	
	def transaction(self, amount, source, target_account_number):
		"""Attempts to move amount from source to target_account_number.
		Returns True if the operation was successful, False
		otherwise. The operation is successful if the source
		has this much money and the target_account_number exists."""
		pass

	def login(self):
		"""Prompts the user to login with password."""

class account(object):
	"""An account contains a customer's balance and transaction history"""
	def account(self, accountnumber, password_hash, balance=0, history=list()):
		"""Create an account with an accountnumber, password_hash, 
		balance and	history. The balance and the history defaults 
		to 0 and an empty list."""
		pass
```
# Programflöde och dataflöde
Programmet börjar med att skapa ett bankobjekt. Bankobjektet innehåller en lista över alla konton. Varje konto innehåller kontonummer, lösenord, balans och transaktionshistorik. När bankobjektet skapas så laddas databasen med konton från en fil. Därefter körs metoden login för att låta användaren logga in. Användaren presenteras därefter med en meny där hen kan välja mellan att överföra pengar, lista transaktioner eller avsluta. 
1. Om användaren väljer att överföra pengar så körs metoden transaction med den data som matats in. Om datan uppfyllde kraven (Det finns tillräckligt med pengar på kontot och mottagarens kontonummer existerar i databasen) så genomförs transaktionen.
2. Om användaren väljer att visa historik så visas det kontots transaktionshistorik på skärmen och därefter återvänder användaren till huvudmenyn.
3. Om användaren väljer att avsluta så avslutas programmet.

# DD1331-P-ppgift
# Specifikation

# Inledning
Jag tänker skapanett Pythonprogram som frågar efter årtal (yyyy), månad (mm) och dag (dd) och därefter, med hjälp av lämpliga formler räkna ut vilken veckodag detta datum infaller eller inföll på. Själva beräkningen ska göras i en funktion som tar år, månad och dag som parametrar. Formlerna ger såklart veckodagen som heltal, men funktionen bör returnera veckodag i klartext.

Programmet kommer köras som en GUI med inmatningsfält för år, månad, respektive dag samt fält för utmatning av veckodag. En av de största utmaningarna med detta projekt är först och främst att finna en lämplig formel för beräkningen, men även felhantering, då datum måste vara korrekt skrivna och inget annat än positiva heltal eller månadsnamnen får förekomma

# Användarscenarier
Mata in årtal, månad och dag enligt formaten (yyyy), (mm) eller månadsnamn, (dd). Om det inmatade datumet infaller med dagens datum kommer följande exempelvis skrivas ut:
```
Today is a Monday
```
Annars utmatas följande:
```
Yesterday was a Saturday
Tomorrow will be a thursday
```
I andra fall utmatas något av exempelvis nedanstående:
```
December 28th, 1999 was a Tuesday
June 21st, 2020 will be a Sunday
```
En anmärkning är att meningen som skrivs ut bör förhålla sig enligt korrekt engelsk ortografi. Ordningstalets suffix (Ordinal indicator) ska skrivas ut efter datumet om det inföll innan eller infaller efter dagens datum. I allmäna fall ska utmatningen enligt formatet
[Month] [day+ suffix], [year] [was a/will be a] [weekday]. 

## Felhantering
Under inmatningen ska programmet först kontrollera om inmatningen av datum är korrekt. Därför bör nedanstående punkter tas i hänsyn.
* Existerar datum? T ex 30/2 och 12/13 existerar inte.
* Om blankt inmatas bör detta också kunna hanteras
* Månad och dag får ex. skrivas i formaten mm eller dd. Om onödigt många nollor föregår ska detta tas i hänsyn. 
  Liknande gäller för år    (yyyy). Ex. tillåts mm: 03 och dd: 01 (eller mm: 3, dd: 1) men inte mm: 004, dd: 0006.
* Innehåller det inmatade datumet annat än siffror (”o” istället för 0 etc)?

Hänsyn ska tas till eventuellt skottår, som definieras enligt: 
```
(årtal % 4 = 0) och (årtal % 4 ≈ 0) 
eller  årtal % 400 = 0
```
När felaktig inmatning påträffas ska programmet kommentera felets art, dvs enligt vilka av de ovanstående punkterna som inmatningen inte förhåller.

# Kodskelett
```
#Input in the entry boxes of 'Year', 'Month' and 'Day'
#Month must be written as a number between 1-12
#Press "Calculate" button to return weekday of the given date

from time import*
from tkinter import*

class Calculator:
    
    #GUI LAYOUT
    def __init__(self, master): 
        self.master = master
        self.months = ['January', 'january', 'February',
                       'february', 'March', 'march',
                       'April', 'april', 'May', 'may',
                       'June', 'june', 'July','july',
                       'August', 'august', 'September',
                       'september','October', 'october',
                       'November', 'november',
                       'December', 'december']
        master.title('Weekday Calculator')
        master.geometry('410x380')
        master.resizable(width = False, height = False)
       
        #Title
        self.Title = Label(root, text= "Weekday Calculator",
                     font = ('Avenir', 18, 'normal'))
        self.Title.grid(column = 0, columnspan = 7,
                        padx = 5, pady = 5)

        #Description
        self.Description = Label(root,
        text= 'This program determines the specific weekday'
              ' for given dates \n'
              '| Year (yyyy) | Month (mm) | Day (dd) |',
        font = ('Avenir', 13, 'normal'))
        self.Description.grid(row = 1, column = 0,
                     columnspan = 7, padx = 5, pady = 5)

        #Entry Boxes
        self.Year = Label(root, padx = 9, text = 'Year:',
                    font = ('Avenir', 13, 'normal'))
        self.Year.grid(row = 2, sticky = W, padx = 1)
        self.Yeardisplay = Entry(root, width = 33)
        self.Yeardisplay.grid(row = 2, column = 1, sticky = E)

        self.Month = Label(root, padx = 9, text = 'Month:',
                     font = ('Avenir', 13, 'normal'))
        self.Month.grid(row = 3, sticky = W, padx = 0)
        self.Monthdisplay = Entry(root, width = 33)
        self.Monthdisplay.grid(row = 3, column = 1, sticky = E)

        self.Day = Label(root, padx = 9, text = 'Day:',
                   font = ('Avenir', 13, 'normal'))
        self.Day.grid(row = 4, sticky = W, padx = 0)
        self.Daydisplay = Entry(root, width = 33)
        self.Daydisplay.grid(row = 4, column = 1, sticky = E)

        self.Week = Label(root, padx = 9, text= 'Weekday:',
                    font = ('Avenir', 13, 'normal'))
        self.Week.grid(row = 5, sticky = W, padx = 0)
        self.Weekdaydisplay = Entry(root, width = 33,
                              state = 'readonly')
        self.Weekdaydisplay.grid(row = 5, column = 1, sticky = E)
        
        self.Extradisplay = Entry(root, width = 33,
                            state = 'readonly')
        self.Extradisplay.grid(row = 6, column = 1, sticky = E)

        #Calculate Button
        self.Calculate = Button(text = 'Calculate',
                         command = self.calculate, 
                         font = ('Avenir', 15, 'normal'))
        self.Calculate.grid(row = 7, column = 0, columnspan = 8,
                         padx = 10, pady = 5, sticky =  N+S+E+W)

        #Clear Button
        self.clear = Button(text = 'Clear',
                     command = self.clear,
                     font = ('Avenir', 15, 'normal'))
        self.clear.grid(row = 8, column = 0, columnspan = 8,
                     padx = 10, pady = 5, sticky =  N+S+E+W)

        #Exit Button
        self.Exit = Button(text = 'Exit',
                    command = root.destroy,
                    font = ('Avenir', 15, 'normal'))
        self.Exit.grid(row = 9, column = 0, columnspan = 8,
                    padx = 10, pady = 5, sticky =  N+S+E+W)

        #Credits
        self.Credits = Label(root, text = 'Raymond Wang 2018 ®',
                       font = ('Avenir', 15, 'italic'))
        self.Credits.grid(row = 10, column = 0,
                       columnspan = 8, pady = 5, padx = 5)

    #FUNCTIONS
    #Clear command
    def clear(self):
        self.Yeardisplay.delete(0,END)
        self.Monthdisplay.delete(0,END)
        self.Daydisplay.delete(0,END)
        self.clear_display(self.Weekdaydisplay)
        self.clear_display(self.Extradisplay)
        self.Weekdaydisplay.configure(state='readonly')
        self.Extradisplay.configure(state='readonly')
            
    #Calculate command
    def calculate(self):
        year = self.Yeardisplay.get()
        month = self.Monthdisplay.get()
        day = self.Daydisplay.get()
        
        if year.isdigit():
            if year[0] == '0':
                if len(year) == 1:
                    self.error_display(self.Extradisplay, 'Year 0 does not exist')
                else:
                    self.error_display(self.Extradisplay, 'Remove preceding zeros')     
            elif month.isdigit():
                self.month_digit(year, month, day)                   
            elif month in self.months:
                month = month.capitalize()
                month_to_int = {'January':1, 'February':2,
                'March':3, 'April':4,'May':5, 'June':6,
                'July':7, 'August':8, 'September':9,
                'October':10, 'November':11, 'December':12}
                Month = str(month_to_int[month])
                self.month_digit(year, Month, day)
                
            else:
                self.output(year, month, day.lstrip('0'))               
        elif len(year) == 0:
            if len(month) == 0:
                if len(day) == 0:
                    self.error_display(self.Extradisplay, '')
                else:
                    self.error_display(self.Extradisplay, 'Error')
            else:
                self.error_display(self.Extradisplay, 'Error')
        else:
            self.error_display(self.Extradisplay, 'Error')
            
    #Error handling regarding preceding zeros for day input
    def month_digit(self, year, month, day):
        if month[0] == '0':
            if len(month) > 2:
                self.error_display(self.Extradisplay, 'Remove preceding zeros')
            else:
                self.day_digit(year, int(month), day)
        else:
            self.day_digit(year, int(month), day)
                    
    #Error handling regarding preceding zeros for day input
    def day_digit(self, year, month, day):
        if day.isdigit():
            if day[0] == '0':
                if len(day) > 2:
                    self.error_display('Remove preceding zeros')
                else:
                    self.output(year, month, day.lstrip('0'))
            else:
                self.output(year, month, day.lstrip('0'))
        else:
            self.output(year, month, day.lstrip('0'))


    #Error handling for month
    def output(self, year, month, day):
        try: 
            if (int(month) in [1,3,5,7,8,10,12]):
                self.condition(year, month, day, '31', '') 
            elif (int(month) in [4,6,9,11]):
                self.condition(year, month, day, '30', '') 
            elif int(month) == 2:
                if (((int(year) % 4) == 0 and
                not (int(year) % 100) == 0)
                or (int(year) % 400) == 0):
                    if int(year) == 1712:
                        if int(day) == 30:
                            #Easter Egg
                            self.condition(year, month, day, '30', '')
                            self.special_case()
                        else:
                            self.condition(year, month, day, '29', '') 
                    else:
                        self.condition(year, month, day, '29', '')
                else:
                    self.condition(year, month, day, '28', '29')
            elif int(month) > 12:
                self.error_display(self.Extradisplay, 'Enter month between 1-12 or month name')
        except:
            self.error_display(self.Extradisplay, 'Enter month between 1-12 or month name')
            
    #Error handling for day
    def condition(self, year, month, day, lastday, leapday):
        try:
            if len(day) == 0 or int(day) > int(lastday):
                if int(month) == 2:
                    if day == leapday:
                        self.error_display(self.Extraisplay, 'Not a leap year')                                                     
                    else:                   
                        self.error_display(self.Extradisplay, 'Enter day between 1-' + lastday)
                else:
                    self.error_display(self.Extradisplay, 'Enter day between 1-' + lastday)
            elif int(day) <= int(lastday):
                self.change_display(self.Weekdaydisplay, self.message(year, month, day))
        except:
            self.error_display(self.Extradisplay, 'Enter day between 1-' + lastday)
            
    #Output for easter egg 
    def special_case(self): 
        self.clear_display(self.Extradisplay)
        self.Extradisplay.insert(INSERT, '1712/02/30 was a real date in Sweden')
        self.Extradisplay.configure(state='readonly')
        
    #Displays given weekday on the 'Weekday' entry box
    def change_display(self, func, text):
        self.clear_display(self.Extradisplay)
        self.clear_display(self.Weekdaydisplay)
        func.insert(INSERT, text)
        func.configure(state='readonly')

    #Clearing displays before output 
    def clear_display(self,func):
        func.configure(state='normal')
        func.delete(0,END)
    
    #Error output
    def error_display(self, func, text):
        self.change_display(func, text)
        
    #Returns message for output on entry box
    def message(self, year, month, day): 
        weekday = ['Sunday', 'Monday', 'Tuesday',
        'Wednesday', 'Thursday', 'Friday', 'Saturday']
        a = int((14 - int(month))/12)
        y = int(year) - a
        m = int(month) + (12*a) -2
        d = (int(day) + y + int(y/4) - int(y/100) +
        int(y/400) + int((31*m)/12)) % 7
        x = weekday[d]
        name = self.wordmonth(month)
        Day = self.ordinal(day)
        
        StrYear = int(strftime('%Y'))
        StrMonth = int(strftime('%m'))
        StrDay = int(strftime('%d'))
        DisplayTime = self.JulianDN(year, month, day)
        CurrentDate = self.JulianDN(StrYear, StrMonth, StrDay)

        if DisplayTime == CurrentDate:
            message = self.r_output('Today is a ', x)
        elif DisplayTime == CurrentDate + 1:
            message = self.r_output('Tomorrow will be a ', x)
        elif DisplayTime == CurrentDate - 1:
            message = self.r_output('Yesterday was a ', x)
        elif DisplayTime > CurrentDate:
            message = self.g_output(name, Day, year, ' will be a ', x)
        elif DisplayTime < CurrentDate:
            message = self.g_output(name, Day, year, ' was a ', x)
        return message

    #Output if given date is today, yesterday or tomorrow
    def r_output(self, text, day_of_week):
        output = (text + day_of_week)
        return output

    #Output for days before or after current date
    def g_output(self, Month, Day, Year, text, day_of_week):
        output = (Month + ' ' + Day + ', ' + Year + text + day_of_week)
        return output

    #Returns ordinal for given day number
    def ordinal(self, day):
        teen_numbers = [11, 12, 13, 14, 15, 16, 17, 18, 19]
        output = ['th','st', 'nd', 'rd', 'th', 'th',
                    'th', 'th', 'th', 'th', 'th']
        if int(day) in teen_numbers:
            return (day + 'th')
        else:
            return (day + output[int(day[-1])])

    #Calculates given weekday with Julian Date Number
    def JulianDN(self, Y,M,D):
        a = int((14 - int(M))/12)
        y = int(Y) + 4800 - a
        m = int(M) + (12 * a) - 3
        JDN = (int(D) + int(((153 * m) + 2) /5) + (365 * y)
        + int(y/4) - int(y/100) + int(y/400) - 32045)
        return JDN

    #Return month name from input
    def wordmonth(self, month):
        monthname = [word for word in self.months if word.istitle()]
        Month = int(month) -1
        return monthname[Month]
    
root = Tk()
Calculator(root)
root.mainloop()
