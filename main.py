# IMPORTS #
import time
from time import gmtime, strftime
import hashlib
import os 
from colorama import init, Fore
init()

# INITIALISATION #

# initialising variables that are used throughout the code. - Alex + Rav
curUser = ''  # current user
verified = False  # has the current user entered correct pin, reset on logout
userIndex = 0  # index of the current user in accountData
accountNames = []  # list of account names, these are used for ease of programming
accountData = []  # formatted so that accessing a user's data is accountData[userIndex][0, 1 or 2], making grabbing data easier
actual_time = strftime("%Y-%m-%d %H-%M-%S", gmtime()) # initialising a global value for the current date and time, to be used in both the receipt and main menu.

# initialisation of account data, formatting for retrieval. - Alex
def readAccounts():
  global accountData
  global accountNames
  accountData = open('accounts.txt', 'r').read()
  accountData = accountData.split('\n')  # splitting accounts into lists
  n = 0
  for account in accountData:  # splitting lists in accounts into further lists
    accountData.pop(n)
    accountData.insert(n, account.split(' '))
    n += 1
  for account in accountData:
    accountNames.append(account[0])

# FUNCTIONS #
# defining the logo function, which prints the logo whenever it is needed. - Rav
def logo():
  print(Fore.YELLOW + """                                                                                                                                                     
                                    ./oyhhhhhhhhhhyyysssoo++//::-..`                                  
                                -ohdmmmmmmmmmmmmmmmmmmmmmmmmmmddddddhyso+:.                          
                              -ohdmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmdy-                        
                          `/hdmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmddhh`                       
                        .odmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmddhhhh-                       
                      `sdmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmddhhhhhh/                       
                      `hmmmmmmMMMMmmNNNNNNmmmmmmmmmmmmmmmmmmmmmmmmmmddhhhhhhhh+  `....`               
                      +hhdddddmmmmmmNNNMMMMMMMMMMMMMNmmmmmmmmmmmdddhhhhhhhhhhhhshhddddhyo:`           
                      yhhhhhhhhhddddddddmmmmmmmmmNNNmmmmmmmmdddhhhhhhhhhhhhhddmmmmmmmmmmmdh-          
                      hhhhhhhhhhhhhhhhhhhhhhhdddddddddddmmmmdhhhhhhhhhhhhhddmmmmmmmmmmmmmmh:          
                      hhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhdmmmdhhhhhhhhhhhddmmmmmmmmmmdyo/:-`           
                `....yhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhdmmmdhhhhhhhhhddmmmmmmmmmmms-`                
            ./syhdddddhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhdmmmdhhhhhhhddmmmmmmmmmmmms                   
          .sdmmmmmmmmmdddddhhhhhhhhhhhhhhhhhhhhhhhhhhhhhddddhhhhdddmmmmmmmmmmmmmmh-`                 
          .dmmmmmmmmmmmmmNmmmmdddddddddhhhhhhhhhhhhhhhhhhhhhhhdddmmmmmmmmmmmmmmmmmmdhyyyyso+-`        
          `ydmmmmmmmmmmmNMMMMMMNNNNNmmmmmmdddddddddddhhhhdddddmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmh:       
          `-//+oshdmmmmmmmmmmNNNNMMMMMMMMMMNNNmmmmmmddddmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmm+       
                  `:mmmmmmmmmmmmmmmmmmmmmmNNNNNmmmmmmmmmmmmmmmmmmmmmmmmmmdhs+/:::/+osyyhhhhhs/`       
                  -mmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmdho:.`            `````          
              `-/+ydmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmdy+-`                               
            .hmmmmmmmmmmmmdhhso+/::::/+oshhdmmmmmmmmmmmmmmmmmmdy+-                                   
            `ydmmmmmmddho/-.              .-/shddmmmmmmmmddhs/.                                      
              .:++o+/:.                        .-:/+ooo+/-.                                          
 /$$$$$$$              /$$     /$$                               /$$$$$$$                      /$$      
| $$__  $$            | $$    | $$                              | $$__  $$                    | $$      
| $$  \ $$ /$$   /$$ /$$$$$$ /$$$$$$    /$$$$$$   /$$$$$$       | $$  \ $$  /$$$$$$  /$$$$$$$ | $$   /$$
| $$$$$$$ | $$  | $$|_  $$_/|_  $$_/   /$$__  $$ /$$__  $$      | $$$$$$$  |____  $$| $$__  $$| $$  /$$/
| $$__  $$| $$  | $$  | $$    | $$    | $$$$$$$$| $$  \__/      | $$__  $$  /$$$$$$$| $$  \ $$| $$$$$$/ 
| $$  \ $$| $$  | $$  | $$ /$$| $$ /$$| $$_____/| $$            | $$  \ $$ /$$__  $$| $$  | $$| $$_  $$ 
| $$$$$$$/|  $$$$$$/  |  $$$$/|  $$$$/|  $$$$$$$| $$            | $$$$$$$/|  $$$$$$$| $$  | $$| $$ \  $$
|_______/  \______/    \___/   \___/   \_______/|__/            |_______/  \_______/|__/  |__/|__/  \__/      
""")                                                                           

# defining the clear function, which allows the program to clear the screen. - Rav
def clear():
  os.system("cls")

# defining the save function, which takes account data and reformates it back to how it is stored in accounts.txt - Alex
def save(accounts):
  for n in range(len(accounts)):
    newAccountData = f"{accounts[n][0]} {accounts[n][1]} {accounts[n][2]}"
    accounts.pop(n)
    accounts.insert(n, newAccountData)
  accounts = '\n'.join(accounts)
  open('accounts.txt', 'w').write(accounts)


# defining the print receipt function, which generates a receipt text file after transactions. - Rav
def generateReceipt(user, type, transactionamount, initialamount, finalamount):
    while True: 
      askreceipt = input(Fore.WHITE + "Would you like to print a receipt? [Yes/No]: ").lower()
      if askreceipt == "yes":
        global actualTime
        receipt = open("RECEIPT " + user.upper() + " " + type.upper() + " " + actual_time + ".txt", "w+")
        receipt.write("Butter Bank" + "\n")
        receipt.write("22 Arroya Lane" + "\n")
        receipt.write("NSW 2121"+ "\n")
        receipt.write("Phone: 17 38 88" + "\n\n")
        receipt.write("RECEIPT" + "\n")
        if type == "deposit":
          receipt.write("Transaction Type: Deposit" + "\n")
          receipt.write("Initial Amount: $" + initialamount + "\n")
          receipt.write("Amount Deposited: +$" + transactionamount + "\n")
        elif type == "withdrawal":
          receipt.write("Transaction Type: Withdrawal" + "\n")
          receipt.write("Initial Amount: $" + initialamount + "\n")
          receipt.write("Amount Withdrawn: -$" + transactionamount + "\n")
        receipt.write("Final Amount: $" + finalamount + "\n\n")
        receipt.write("Thank you for using Butter Bank! Have a great day!")
        break
      elif askreceipt == "no":
        break
      else:
        clear()
        print(Fore.RED + "Sorry, your input was not able to be understood. Please only type y or n, and press enter.")

# defining the withdrawal function, which allows the user to withdraw money from their account. - Alex
def withdrawal(account, index):
  global accountData
  while True:  
    clear()
    while True:  # grabs the amount
      print(Fore.WHITE + f"You have ${accountData[index][1]}")
      try:
        amount = int(input("How much would you like to withdraw? "))
      except:
        print(Fore.RED + "Sorry, but we are unable to provide you non-whole number withdrawals. Please only enter a whole number: ")
      else:
        break
    if amount == 0:
      break
    elif amount > int(accountData[index][1]):
      print(Fore.RED + "You cannot withdraw more than you have in your account.")
      continue
    transactiontype = "withdrawal"
    initialamount = accountData[userIndex][1]
    newAmountHeld = int(accountData[userIndex][1]) - amount  # changing account data
    generateReceipt(curUser, transactiontype, str(amount), str(initialamount), str(newAmountHeld))
    accountData[userIndex].pop(1)
    accountData[userIndex].insert(1, newAmountHeld)
    save(accountData)  # saving and re-reading account data
    readAccounts()
    print(Fore.WHITE + "Transaction completed! Your account balance is now $" + accountData[index][1] + ".") 
    time.sleep(1.5)
    input("Please press Enter to return to the menu: ")
    clear()
    logo()
    print(Fore.WHITE + "Welcome to Butter Bank!")
    print("The bank with butter in it!")
    break

# defining the deposit function, which allows the user to deposit money from their account - Alex
def deposit(account, index):
  global accountData
  while True:
    clear()
    while True:
      print(Fore.WHITE + f"You have ${accountData[index][1]}")
      try:
        amount = int(input("How much would you like to deposit? "))
      except:
        print(Fore.RED + "Sorry, but we are unable to provide you non-whole number withdrawals. Please only enter a whole number: ")
      else:
        break
      if amount > 10000:
        print(Fore.RED + "Sorry, there is a limit of $10000 every day. Please visit one of our branches to deposit anything larger.")
    if amount == 0:
      break
    transactiontype = "deposit"
    initialamount = accountData[userIndex][1]
    newAmountHeld = int(accountData[userIndex][1]) + amount
    generateReceipt(curUser, transactiontype, str(amount), str(initialamount), str(newAmountHeld))
    accountData[userIndex].pop(1)
    accountData[userIndex].insert(1, newAmountHeld)
    save(accountData)
    readAccounts()
    print(Fore.WHITE + "Transaction completed! Your account balance is now $" + accountData[index][1] + ".") 
    time.sleep(1.5)
    input("Please press Enter to return to the menu.")
    clear()
    logo()
    print(Fore.WHITE + "Welcome to Butter Bank!")
    print("The bank with butter in it!")
    break

# defining the login section, ensures that the user is securely login and will terminate if too many wrong guesses are made. - Rav + Alex
def login():
  global verified
  global curUser
  global userIndex
  while True:
    logo()
    print(Fore.WHITE + "Welcome to Butter Bank!")
    time.sleep(1)
    print("The bank with the butter in it!")
    time.sleep(1)
    while True:
      attempts = 0  # too many attempts, and the program quits, safety feature
      curUser = input("Please enter your username: ")
      if curUser in accountNames:
        userIndex = accountNames.index(curUser)
        while True:
          pin = input(Fore.WHITE + "Please enter your PIN: ").encode('utf-8')
          # hash the pin
          cryptpin = hashlib.sha256(pin).hexdigest()
          if cryptpin == accountData[userIndex][2]:
            verified = True  # causes all the while loops to break, and for login() to then exit
            break
          else:
            attempts += 1
            clear()
            logo()
            print(Fore.WHITE + "Welcome to Butter Bank!")
            print("The bank with butter in it!")
            print(Fore.RED + "Sorry, that PIN was incorrect. Please try again.")
            if attempts == 3:
              print("Too many failed logins, terminating program.")
              time.sleep(3)
              quit()
      else:
        print(Fore.RED + "Sorry, there is no user with this username.")
        print(Fore.WHITE + "Would you like to create a new account?")
        while True:
          choice = input('[Yes/No]').lower()
          if choice != 'yes':
            break
          else:
            newName = input(Fore.WHITE + "What would you like your username to be? ")
            if newName in accountNames:
              print("A user with that name already exists, please log in instead.")
              time.sleep(2)
              break
            time.sleep(1)
            while True:
              newPIN = input("Please choose a PIN. It must be a 4 letter alphanumerical string, and will become uppercase if not formatted as such: ").encode('utf-8')
              if len(newPIN) != 4 or not newPIN.isalnum():  #isupper() returns false if all are numbers, even though with only one letter that is upper it would return true, so we made it into a feature instead of a bug
                continue
              else:
                newPIN = hashlib.sha256(newPIN.upper()).hexdigest()
                open('accounts.txt', 'a').write(f"\n{newName} {0} {newPIN}")
                readAccounts()
                break
          break
        time.sleep(2)       
        clear()
        print("Welcome to Butter Bank")
        time.sleep(1)
        print("The bank with the butter in it!")
        time.sleep(2)
      if verified:
        break
    if verified:
      break

# defining the main menu of the program, which is what the user is greeted to after logging in. - Rav
def mainmenu():
  global accountData
  global verified
  print(Fore.WHITE + "Login Successful!")
  time.sleep(2)
  clear()
  logo()
  print("Welcome " + curUser + "!")
  print("You have $" + accountData[userIndex][1] + "!" )
  while True:
    print(Fore.WHITE + """
    [1] Deposit
    [2] Withdraw
    [3] Change PIN
    [4] Log Out
    [5] Quit
    """)  
    menuchoice = input("Please select an option: ")
    if menuchoice not in ['1', '2', '3', '4', '5']:
      clear()
      print(Fore.RED + "Sorry, please type in a number from 1 to 5, and press enter.")
    else:
      if menuchoice == "1":
        deposit(accountData, userIndex)
      if menuchoice == "2":
        withdrawal(accountData, userIndex)
      #if menuchoice == "3":
      if menuchoice == "4": 
        global verified
        verified = False
        clear()
        login()
      if menuchoice == "5": 
        print("Thank you for choosing Butter Bank!")
        time.sleep(2)
        quit()


# MAIN CODE #
# this is where the main code is executed. This will infinitely run, until prompted to stop. - Rav
readAccounts()
while True:
  login()
  mainmenu()

  