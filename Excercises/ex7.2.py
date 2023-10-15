names = set()
while True:
    name = input("Enter a name : ")
    if name != "":
        if name in names:
            print("Existing name")
        else:
            print("New name")
            names.add(name)
    else:
        break
for i in names:
    print(i)