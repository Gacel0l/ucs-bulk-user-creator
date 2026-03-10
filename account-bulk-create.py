from account import main, debug
import account
account.debug = True                # FOR FIRST CONFIGURATION SET IT TO TRUE AND CHANGE SESSIONS OR IF THERE ARE PROBLEMS

def start():
    if account.debug:
        print("\n ==========Session==========\n")
        print(f"Session UMC: {account.UMC_SESSION_ID}")
        print("\n ==========Session==========\n")
        wybor = input("\nChange Sessions? Y/N > ")
        if wybor.lower() == "y" or wybor.lower() == "yes":
            account.UMC_SESSION_ID = input("\nSesja UMC: ")
            account.X_XSRF_TOKEN = account.UMC_SESSION_ID
            print(f"\n Session UMC: {account.UMC_SESSION_ID}")
            print(f"\n To make the changes permanent, change the UMC_SESSION_ID parameter in the account.py file")
        else:
            pass



    print(f"\n URL: {account.BASE_URL}")
    wybor = input("Change URL? Y/N: ")
    if wybor.lower() == "y" or wybor.lower() == "yes":
        account.BASE_URL = input("\nURL: ")
    else:
        print(f"\n URL: {account.BASE_URL}")

    print(f"\nIs the Class Parameter Correct? \n Parameter: \033[1m{account.CLASS}\033[0m")
    wybor = input("\nY/N:")
    if wybor.lower() == "y" or wybor.lower() == "yes":
        pass
    elif wybor.lower() == "n" or wybor.lower() == "no":
        account.CLASS = input("\nProvide a valid Class parameter: ")

    klasa = input("enter class:")
    liczba_stanowisk = int(input("Enter the Number of Positions (default 20):") or 20)
    liczba_stanowisk = liczba_stanowisk + 1

    plec = input("\n    Gender: \n[1] Males(ch). \n[2] Females(dz) \n >")
    if plec == "1":
        plec = "ch"
    elif plec == "2":
        plec = "dz"
    else:
        print("\n\nInvalid Parameter Detected [Exiting!]")
        exit()

    haslo = input("\n    enter password: ")
    i = 1

    print("\n\n=======================================\n")
    print(f"Session UMC: {account.UMC_SESSION_ID}")
    print(f"\n URL: {account.BASE_URL}")
    print(f"Class_Parameter = {account.CLASS}")
    print(f"Class = {klasa}")
    print(f"number of positions = {liczba_stanowisk - 1}")
    print(f"Gender = {plec}")
    print(f"Password = {haslo}")

    print(f"\n Sample Account Looks Like This: ")
    print(f"LOGIN: {klasa}{plec}{i}")
    print(f"NAME: {klasa}")
    print(f"Surname: position_{i}")
    print(f"Password: {haslo}")
    print("\n\n=======================================\n")
    wybor = input("Do the parameters match Y/N: ")
    if wybor.lower() == "y" or wybor.lower() == "yes":
        pass
    else:
        exit()

    while (i < liczba_stanowisk):
        print(f"\nAccount Number: {i}\n")
        login = (f"{klasa}{plec}{i}")
        imie = (f"{klasa}")
        nazwisko = (f"position_{i}")
        main(login, imie, nazwisko, haslo)
        i = i + 1

    print(f"{liczba_stanowisk - 1} Account Created \n if any errors occur, check the IP address, the Class Parameter, the Data provided, whether the session has not expired, whether the server is online \n")
    print("\n reruns program...")
    start()

start()





