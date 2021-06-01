# IMPORTS #
import time
import hashlib
import os 
from colorama import init, Fore, Back, Style
init()

# INITIALISATION #

# initialising variables that are used throughout the code.
curUser = ''  # current user
verified = False  # has the current user entered correct pin, reset on logout
userIndex = 0  # index of the current user in accountData
accountNames = []  # list of account names, these are used for ease of programming


# initialisation of account data, formatting for retrieval.
accountData = open('accounts.txt', 'r').read()
accountData = accountData.split('\n')
n = 0
for account in accountData:
  accountData.pop(n)
  accountData.insert(n, account.split(' '))
  n += 1
for account in accountData:
  accountNames.append(account[0])

# FUNCTIONS #
# defining the clear function, which allows the program to clear the screen.
def clear():
  os.system("cls")

# defining the login section, ensures that the user is securely login and will terminate if too many wrong guesses are made.
def login():
  global verified
  global curUser
  global userIndex
  while True:
    print(Fore.WHITE + "Welcome to Butter Bank")
    time.sleep(1)
    print("The bank with the butter in it!")
    time.sleep(1)
    while True:
      attempts = 0
      curUser = input("Please enter your username: ")
      if curUser in accountNames:
        userIndex = accountNames.index(curUser)
        while True:
          pin = input("Please enter your password: ").encode('utf-8')
          # hash the pin
          cryptpin = hashlib.sha256(pin).hexdigest()
          if cryptpin == accountData[userIndex][2]:
            verified = True
            break
          else:
            attempts += 1
            print(Fore.RED + "Sorry, that password was incorrect.")
            if attempts == 3:
              print("Too many failed logins, terminating program.")
              time.sleep(3)
              quit()
      else:
        print(Fore.RED + "Sorry, there is no user with this username.")
        print(Fore.WHITE + "Would you like to create a new account?")
        while True:
          choice = input('[y/n] ')
          if choice != 'y':
            continue
          else:
            newName = input(Fore.WHITE + "What would you like your username to be? ")
            if newName in accountNames:
              print('A user with that name already exists, please log in instead')
              time.sleep(2)
              break
            time.sleep(1)
            while True:
              newPIN = input("Choose a PIN. It must be a 4 letter alphanumerical string, and will become uppercase if not formatted as such: ").encode('utf-8')
              if len(newPIN) != 4 or not newPIN.isalnum():
                continue
              else:
                newPIN = hashlib.sha256(newPIN.upper()).hexdigest()
                open('accounts.txt', 'a').write(f"\n{newName} {0} {newPIN}")
                break
            break
        time.sleep(2)       
        clear()
        print("Welcome to Butter Bank")
        print("The bank with the butter in it!")
      if verified:
        break
    if verified:
      break

# defining the main menu of the program, which is what the user is greeted to after logging in.
def mainmenu():
  print("Login Successful!")
  time.sleep(2)
  clear()
  print("Insert Butter Bank Logo")
  print("Welcome " + curUser + "!")
  print("You have $" + accountData[userIndex][1] + "!" )

# MAIN CODE #
# this is where the main code is executed. This will infinitely run, until prompted to stop.
while True:
  login()
  mainmenu()

  