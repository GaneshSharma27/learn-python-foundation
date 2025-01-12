birthdays = {"Ganesh": "September 27", "Khushi": "September 12", "Shubh": "April 12"}

while True:
    name = str(input("Enter a name (Press enter to quit): ")).title()
    if name == "":
        break
    if name in birthdays:
        print(name + "'s birthday is on " + birthdays[name])
    else:
        print("You haven't entered the birthday of " + name)
        print("What's their birthday:")
        # for month input
        while True:
            try:
                month = input("What's their birth month (in text): ").title()
                break
            except:
                print("Enter appropriate values")
        # for date input
        while True:
            try:
                date = int(input("What's their birth date: "))
                break
            except:
                print("Enter appropriate values")

        b_day = str(month + " " + str(date))
        birthdays[name] = b_day
        print("Updated the information.")
