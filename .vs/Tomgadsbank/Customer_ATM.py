print("Welcome to TomgadsBank")
Trials = 3
UserPin = 1234
balance = 10000
      


while Trials != 0:
    Pin = int(input("please enter your 4 digit pin number: "))
    if Pin != UserPin:
        Trials -= 1
        print("Wrong pin number, yuo have", Trials, "Trials left")
    else:
        UserChoice = input("d: deposit or w: withdraw: or c: check_balance ")
        if UserChoice == "d":
            Userdeposit = int(input("Enter The Amount you would like to deposit: "))
            balance = balance + Userdeposit
            print(balance, "$ Have been deposited into your Account")

        if UserChoice == "w":
            Userwithdraw = int(input("Enter The Amount you would like to withdraw: "))
            balance = balance - Userwithdraw
            print(balance, "$ Have been withdrawn from your Account")
        
        if UserChoice == "c":
            print(balance, "$ is your current balance")
    UserExit = input("Would you like to Continue? Y/N: ")
    if UserExit == "N":
        print("Thank you for using TomgadsBank")
        break
    else:
        continue