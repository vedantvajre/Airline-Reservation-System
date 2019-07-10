prompt2 = "\nHow many family members are with you? (You are inclusive to this number!)"
prompt3 = "\nHow many family members are kids? (Below 18 are kids and have a reduced price!)"
prompt4 = "\nHow many family members are adults?"
prompt5 = "\nWhich flight path will you take? (You can only take one per family!)"
prompt = "\nWhat is your name?"
flight1 = "\nWashington DC to New York Direct- 250$ for Adult, 125$ for Kids."
flight2 = "\nWashington DC to New York with 1 hop- 150$ for Adult, 100$ for Kids."
flight3 = "\nWashington DC to Charlotte Direct- 200$ for Adult, 150$ for Kids."
finished_ticket = []
airline = True
while airline:
    print("\nHello! Welcome to the Airline reservation system.")
    name_customer = input(prompt)
    finished_ticket.append("Name of User: " + name_customer)
    print(flight1, flight2, flight3)
    flight_path = input(prompt5)
    finished_ticket.append("Flight path: " + flight_path.title())
    Customer = True
    while Customer:
        if flight_path.title() == 'Washington Dc To New York Direct':
            quantity_customer = input(prompt2)
            quantity_customer = int(quantity_customer)
            finished_ticket.append("Number of family members: " + str(quantity_customer))
            if quantity_customer != 1:
                kid_customer = input(prompt3)
                kid_customer = int(kid_customer)
                if kid_customer != 0:
                    finished_ticket.append("Kids: " + str(kid_customer))
                    add_kids = (kid_customer*125)
                    finished_ticket.append("Kids Price: " + str(add_kids) + '$')
                    print("Ok!")
                else:
                    print("Ok!")
                adult_customer = input(prompt4)
                adult_customer = int(adult_customer)
                if adult_customer != 0:
                    finished_ticket.append("Adults: " + str(adult_customer))
                    add_adults = (adult_customer*250)
                    finished_ticket.append("Adults Price: " + str(add_adults) + '$')
                    print("Ok! Here is your ticket!")
                    print(finished_ticket)
                else:
                    print("Ok! Here is your ticket!")
                    print(finished_ticket)
            else:
                print("Ok!")
                customer = False
        if flight_path.title() == 'Washington Dc To New York With 1 Hop':
            quantity_customer = input(prompt2)
            quantity_customer = int(quantity_customer)
            finished_ticket.append("Number of family members: " + str(quantity_customer))
            if quantity_customer != 1:
                kid_customer = input(prompt3)
                kid_customer = int(kid_customer)
                if kid_customer != 0:
                    finished_ticket.append("Kids: " + str(kid_customer))
                    add_kids = (kid_customer * 100)
                    finished_ticket.append("Kids Price: " + str(add_kids) + '$')
                    print("Ok!")
                else:
                    print("Ok!")
                adult_customer = input(prompt4)
                adult_customer = int(adult_customer)
                if adult_customer != 0:
                    finished_ticket.append("Adults: " + str(adult_customer))
                    add_adults = (adult_customer * 150)
                    finished_ticket.append("Adults Price: " + str(add_adults) + '$')
                    print("Ok! Here is your ticket!")
                    print(finished_ticket)
                else:
                    print("Ok! Here is your ticket!")
                    print(finished_ticket)
        if flight_path.title() == 'Washington Dc To Charlotte Direct':
            quantity_customer = input(prompt2)
            quantity_customer = int(quantity_customer)
            finished_ticket.append("Number of family members: " + str(quantity_customer))
            if quantity_customer != 1:
                kid_customer = input(prompt3)
                kid_customer = int(kid_customer)
                if kid_customer != 0:
                    finished_ticket.append("Kids: " + str(kid_customer))
                    add_kids = (kid_customer * 150)
                    finished_ticket.append("Kids Price: " + str(add_kids) + '$')
                    print("Ok!")
                else:
                    print("Ok!")
                adult_customer = input(prompt4)
                adult_customer = int(adult_customer)
                if adult_customer != 0:
                    finished_ticket.append("Adults: " + str(adult_customer))
                    add_adults = (adult_customer * 200)
                    finished_ticket.append("Adults Price: " + str(add_adults) + '$')
                    print("Ok! Here is your ticket!")
                    print(finished_ticket)
                else:
                    print("Ok! Here is your ticket!")
                    print(finished_ticket)
        else:
            Customer = False
