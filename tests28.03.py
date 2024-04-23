def registracija():
    email = input("Ievadi savu e-pasta adresi: ")
    password = input("Ievadi savu paroli: ")

    if len(password) < 6 or "@" not in email:
        print("Neder. Parolei jābūt vismaz sešus simbolus garai un e-pasta adresē jābūt '@' simbolam.")
        registracija()
    else:
        print("Pateicamies par reģistrāciju!")


