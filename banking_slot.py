# python banking program


def show_balance(balance):
    
    print(f"Your balance is ${balance:.2f}")

def deposit():
    
    amount = float(input("Enter your amount sir:"))

    if amount < 0: 
      print("amount must be greater than 0")
      return 0
    else:
      return amount

def withdraw(balance):
    amount = float(input("enter your amount sir:"))
    if amount > balance:
        print("insufficient funds")
        return 0
    elif amount < 0:
        print("amount must be greater than 0")
        return 0
    else: 
        return amount

def main():
    balance = 0 
    is_running = True

    while is_running:
        print("*******")
        print("BANKING PROGRAM WELCOMES YOU")
        print("*******")

        print("1.show_balance") 
        
        print("2.deposit")
       
        print("3.withdraw")
       
        print("4.exit")


        choice = input("enter your choice (1-4): ")

        if choice == '1' : 
            show_balance(balance)
        elif choice == '2' :
           balance += deposit()
        elif choice == '3' :
           balance -= withdraw(balance)
        elif choice == '4' :
            is_running = False
        else :
            print("this is invalid choice")
            

    print("Thank you have a nice day")

main()
            
