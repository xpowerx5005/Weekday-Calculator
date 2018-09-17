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
```
ewu
```
