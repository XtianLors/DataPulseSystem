import os
import socket
import time

# Información del sistema
CORE_THREAD = os.getpid()
#ID_THREAD = os.getegid
USER_NAMED = os.getlogin()
NAME_OS = os.name
USER_NAME = socket.gethostname()

def clear_screen():
    """Clears the console screen for better visibility."""
    os.system("cls" if os.name == "nt" else "clear")
    print("\n______________________________________________\n")
    print(f" Your are in: {USER_NAME!r}".zfill(35), " 0000000000")
    print(f" The platform is: {NAME_OS!r}".zfill(35), " 0000000000")
    print(f" User name: {USER_NAMED!r}".zfill(35), " 0000000000")
    #print(f"\nThread ID: {ID_THREAD!r}")
    #print(" 0000000000")
    print(f" Thread UIID: {CORE_THREAD!r}".zfill(35), " 0000000000")
    print("\n______________________________________________\n")

def option_one():
    print("\nYou selected Option 1: Placeholder function.")

def option_two():
    print("\nYou selected Option 2: Another placeholder function.")

def option_three():
    print("\nYou selected Option 1: Placeholder function.")

def option_four():
    print("\nYou selected Option 2: Another placeholder function.")

def option_five():
    print("\nYou selected Option 1: Placeholder function.")

def option_six():
    print("\nYou selected Option 2: Another placeholder function.")

def option_seven():
    print("\nYou selected Option 1: Placeholder function.")

def option_eight():
    print("\nYou selected Option 2: Another placeholder function.")

def option_nine():
    print("\nYou selected Option 2: Another placeholder function.")

def option_ten():
    print("\nYou selected Option 1: Placeholder function.")

def option_new():
    print("\nYou might enter on a loop, are you ready?")


def main():
    while True:
       #interfaz gráfica
        clear_screen()
        print("Choose an option (1-10) or type '0' to exit:")
        print("1. Declare data lifecycle phase.")
        print("2. Declare Architecture.")
        print("3. Choose technology.")
        print("4. Retrieve data.")
        print("5. Personalize Storage System.")
        print("6. Choose Storage Operations.")
        print("7. Choose Serving Operation.")
        print("8. Choose local and Sorrounding Protection.")
        print("9. Implement DSL or No-Code?")
        print("10. Team Collaboration and Hierarchy, Organigram.")
        print("0. Exit")

        choice = input("\nEnter your choice: ")


      #Árbol de decisiones
        if choice == "0":
            print("\nGoodbye!")
            time.sleep(3)
            break
        elif choice == "1":
            option_one()
        elif choice == "2":
            option_two()
        elif choice == "3":
            option_three()
        elif choice == "4":
            option_four()
        elif choice == "5":
            option_five()
        elif choice == "6":
            option_six()
        elif choice == "7":
            option_seven()
        elif choice == "8":
            option_eight()
        elif choice == "9":
            option_nine()
        elif choice == "10":
            option_ten()
        elif choice == "new":
            option_new()
        else:
            print("\nUnavailable Option!")

        input("\nPress Enter to continue...")

if __name__ == "__main__":
    main()
