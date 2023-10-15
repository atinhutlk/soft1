airports = {}
while True:
    command = input("1: New, 2: Fetch, 3: Quit: ")
    if command == "1":
        name = input("Airport name: ")
        icao = input("ICAO airport code: ")
        airports[icao] = name
    elif command == "2":
        fetch = input("Enter ICAO code: ")
        if fetch in airports:
            print(f"Name of {fetch} is {airports[fetch]}")
        else:
            print(f"No airport found with {fetch} ICAO code !")
    elif command == "3":
        print("Quit !")
        break
    else:
        print("Wrong command!")