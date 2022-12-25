from pakuri import Pakuri
from pakudex import Pakudex

def main():

    print("Welcome to Pakudex: Tracker Extraordinaire!")
    max_capacity = input("Enter max capacity of the Pakudex: ")

    # While loop to keep asking user for a valid integer for the Pakudex

    while max_capacity.isdigit() == False:
        print("Please enter a valid size.")
        max_capacity = input("Enter max capacity of the Pakudex: ")

    print(f"The Pakudex can hold {max_capacity} species of Pakuri.")

    # While loop for Pakudex game
    game = True
    Pokemon = Pakudex(max_capacity)

    while game:
        print("\nPakudex Main Menu\n" + "-" * 17 + "\n1. List Pakuri\n2. Show Pakuri\n3. Add Pakuri\n4. Evolve Pakuri\n5. Sort Pakuri\n6. Exit")
        menu_input = input("\nWhat would you like to do? ")

        if menu_input == "1":
            if Pokemon.get_species_array() == []:
                print("No Pakuri in Pakudex yet!")
            else:
                print("Pakuri In Pakudex:")
                for item in Pokemon.get_species_list():
                    print(item)
        if menu_input == "2":
            pakuri = input("Enter the name of the species to display: ")
            if pakuri in Pokemon.get_species_array():
                print("")
                print(Pokemon.get_stats(pakuri))
            else:
                print("Error: No such Pakuri!")
        if menu_input == "3":
            if Pokemon.check_if_full() == True:
                print("Error: Pakudex is full!")
            else:
                add_species = input("Enter the name of the species to add: ")
                if Pokemon.add_pakuri(add_species) == True:
                    print(f"Pakuri species {add_species} successfully added!")
                else:
                    print("Error: Pakudex already contains this species!")
        if menu_input == "4":
            pakuri = input("Enter the name of the species to evolve: ")
            if pakuri in Pokemon.get_species_array():
                Pokemon.evolve_species(pakuri)
                print(f"{pakuri} has evolved!")
            else:
                print("Error: No such Pakuri!")
        if menu_input == "5":
            if Pokemon.get_species_array() == "":
                print("No Pakuri in Pakudex yet!")
            else:
                Pokemon.sort_pakuri()
                print("Pakuri have been sorted!")
        if menu_input == "6":
            print("Thanks for using Pakudex! Bye!")
            exit()

        if menu_input != "1" and menu_input != "2" and menu_input != "3" and menu_input != "4" and menu_input != "5" and menu_input != "6":
            print("Unrecognized menu selection!")

main()
