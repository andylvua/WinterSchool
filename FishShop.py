""" FishShop.py
This program provides you with a simple functionality for fish shop management.
Here you can add fish to the store, sort them as you wish,
sell them, or even cast them out if they are expired.
Also, you can be a buyer. See your available cash and fishes in a bag.

For further information please see our GitHub repository:
https://github.com/andylvua/WinterSchool
"""

import time
from operator import itemgetter
import inflect

__author__ = "Andrew Yaroshevych and Oles Pasirskyi"
__version__ = "2.0"
__email__ = "andrii.yaroshevych.ir.2021@lpnu.ua, oles.pasirskyi.ir.2021@lpnu.ua"
__status__ = "Production"


class Bcolors:
    HEADER = '\033[95m'
    BLUE = '\033[94m'
    CYAN = '\033[96m'
    GREEN = '\033[92m'
    WARNING = '\033[93m'
    ERROR = '\033[91m'
    END = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'


def print_ok(message):
    print(Bcolors.GREEN + message + Bcolors.END)


def print_warning(message):
    print(Bcolors.WARNING + message + Bcolors.END)


def print_error(message):
    print(Bcolors.ERROR + message + Bcolors.END)


def print_quit():
    for x in range(0, 4):
        b = "Quitting" + "." * x
        print("\r", Bcolors.ERROR + b + Bcolors.END, end="")
        time.sleep(0.5)


class Fish:
    def __init__(self) -> None:
        self.name = input("Enter fish name: ")
        self.price_in_uah_per_kilo = input("Enter price in UAH per kg: ")
        self.body_only = input("Is fish body only? ")
        self.origin = input("Enter fish origin: ")
        self.weight = input("Enter fish weight: ")


class FishShop:
    list_of_fishes = []
    sorting_reverse = None
    sorting_key = None

    def add_fish(self) -> None:
        while True:
            fish_name = str(input())
            if fish_name.replace(" ", "").isalpha():
                break
            else:
                print_warning("Name should contain only letters, please try again!")
                continue

        while True:
            try:
                fish_price_in_uah_per_kilo = float(input("Enter price in UAH per kg: "))
                if fish_price_in_uah_per_kilo > 0:
                    break
                else:
                    print_warning("Price should be greater than 0, try again!")
            except ValueError:
                fish_price_in_uah_per_kilo = None
                print_error("Price should be a float value, try again!")
                continue

        while True:
            try:
                fish_weight = float(input("Enter weight: "))
                if fish_weight > 0:
                    break
                else:
                    print_warning("Weight should be greater than 0, try again!")
            except ValueError:
                fish_weight = None
                print_error("Weight should be a float value, try again!")
                continue

        self.list_of_fishes.append([fish_name, fish_price_in_uah_per_kilo, fish_weight])
        print_ok("Fish added successfully.\n")

    def get_sorted_fish_list(self):
        if self.sorting_key == "name":
            self.sorting_key = 0
        elif self.sorting_key == "price":
            self.sorting_key = 1
        elif self.sorting_key == "weight":
            self.sorting_key = 2

        print("Sorting by", FishShop.sorting_key, end=' ')
        if FishShop.sorting_reverse:
            print("in decreasing order")
        else:
            print("in increasing order")
        print("Sorted list of fishes: %s" % (sorted(self.list_of_fishes, key=itemgetter(self.sorting_key),
                                                    reverse=self.sorting_reverse)) + "\n")

    def sublist_search(self, searched_element) -> bool:
        return any(searched_element in sublist for sublist in self.list_of_fishes)

    def cast_out_old_fish(self):
        while True:
            fish_name = str(input("Which fish do you want to cast out? "))
            if fish_name.replace(" ", "").isalpha():
                if self.sublist_search(fish_name):
                    break
                else:
                    print_warning("Fish is not found, please try again!")
            else:
                print_warning("Name should contain only letters, please try again!")
                continue

        while True:
            try:
                weight = float(input("How much do you want to cast out? "))
                if weight > 0:
                    break
                else:
                    print_warning("Weight should be greater than 0, try again!")
            except ValueError:
                weight = None
                print_error("Weight should be a float value, try again!")
                continue

        for i in range(len(self.list_of_fishes)):
            if self.list_of_fishes[i][0] == fish_name:
                if self.list_of_fishes[i][2] > weight:
                    self.list_of_fishes[i][2] -= weight
                    print_ok("\nCasted out successfully.")
                    print("List of fishes after casting out: %s" % self.list_of_fishes + "\n")
                else:
                    print_warning("There is not enough fish to cast out, try again!")
                    self.cast_out_old_fish()


class Seller(FishShop):
    def sell_fish(self):
        while True:
            fish_name = str(input("Which fish do you want to sell? "))
            if fish_name.replace(" ", "").isalpha():
                if self.sublist_search(fish_name):
                    break
                else:
                    print_warning("Fish is not found, please try again!")
            else:
                print_warning("Name should contain only letters, please try again!")
                continue

        while True:
            try:
                weight = float(input("How much do you want to sell? "))
                if weight > 0:
                    break
                else:
                    print_warning("Weight should be greater than 0, try again!")
            except ValueError:
                weight = None
                print_error("Weight should be a float value, try again!")
                continue

        for i in range(len(self.list_of_fishes)):
            if self.list_of_fishes[i][0] == fish_name:
                if self.list_of_fishes[i][2] > weight:
                    self.list_of_fishes[i][2] -= weight
                    print_ok("\nSold successfully.")
                else:
                    print_warning("There is not enough fish to sell, try again!")
                    self.sell_fish()

                revenue = int(self.list_of_fishes[i][1]) * weight
                print_ok("Selling revenue is: " + str(revenue))
                print("List of fishes after selling: %s" % self.list_of_fishes + "\n")


class Buyer:
    list_of_bought_fishes = []
    money_spent = int
    money_amount = None

    def buy_fish(self):
        while True:

            fish_name = str(input("Which fish do you want to buy? "))
            if fish_name.replace(" ", "").isalpha():
                if FishShop.sublist_search(FishShop(), fish_name):
                    break
                else:
                    print_warning('Fish is not found, please try again!')
            else:
                print_warning("Name should contain only letters, please try again!")
                continue

        while True:
            try:
                weight = float(input("How much do you want to buy? "))
                if weight > 0:
                    break
                else:
                    print_warning("Weight should be greater than 0, try again!")
            except ValueError:
                weight = None
                print_error("Weight should be a float value, try again!")
                continue

        for i in range(len(FishShop.list_of_fishes)):
            if FishShop.list_of_fishes[i][0] == fish_name:
                if FishShop.list_of_fishes[i][2] >= weight:
                    FishShop.list_of_fishes[i][2] -= weight
                    if ((FishShop.list_of_fishes[i][1]) * weight) <= self.money_amount:
                        self.money_spent = (FishShop.list_of_fishes[i][1]) * weight
                        self.list_of_bought_fishes.append([fish_name, weight])
                        self.money_amount -= self.money_spent
                        print("\nMoney spent: " + str(self.money_spent))
                        print("You funds after buying: " + str(self.money_amount))
                        print_ok("Your bag [name, weight]: " + str(self.list_of_bought_fishes) + "\n")
                    else:
                        print_warning("You don't have enough money, try again!")
                        self.buy_fish()
                else:
                    print_warning("Sorry, here is not enough fish to sell to you, try again!")
                    self.buy_fish()

    def haggle(self, fish_price_in_uah):
        pass


def main():
    if FishShop.sorting_key not in ('name', 'price', 'weight'):
        print_error("Check sorting_key value in __main__")
        raise ValueError()

    menu_options = {
        1: 'Add fish to the store',
        2: 'Get sorted fish list',
        3: 'Cast out old fish',
        4: 'Sell fish',
        5: 'Buy fish',
        6: 'Quit',
    }

    shop = FishShop()
    seller = Seller()
    buyer = Buyer()
    first_buyer = True

    def print_menu():
        time.sleep(0.7)
        print("Menu:")
        for key in menu_options.keys():
            print(key, '--', menu_options[key])
        print()

    def menu_option1_add():
        while True:
            try:
                number_of_fishes = int(input("How many fishes do you want to add to the store? "))
                print()
                break
            except ValueError:
                print_error("Invalid input. Please enter an integer value")
                number_of_fishes = None
                continue

        for i in range(1, number_of_fishes + 1):
            iteration = inflect.engine()
            print("Enter " + iteration.number_to_words(iteration.ordinal(i)) + " fish name: ", end="")
            shop.add_fish()

    def menu_option2_sort():
        shop.get_sorted_fish_list()

    def menu_option3_cast_out():
        shop.cast_out_old_fish()

    def menu_option4_sell():
        seller.sell_fish()

    def menu_option5_buy():
        nonlocal first_buyer
        nonlocal buyer
        if FishShop.list_of_fishes:
            if first_buyer:
                print("\n---------Hi, dear buyer!---------\n")
                while True:
                    try:
                        Buyer.money_amount = int(input("How much money do you have? "))
                        print()
                        break
                    except ValueError:
                        print_error("Invalid input. Please enter an integer value")
                        continue
                buyer.buy_fish()
                first_buyer = False
            else:
                buyer.buy_fish()
        else:
            print_warning("\nSorry, the store is empty, please add some fishes first.\n")

    def menu_option6_exit():
        print_quit()
        exit()

    print("\n---------Welcome to FishShop!---------\n\n"
          "You can see the list of options below:\n")

    while True:
        print_menu()
        while True:
            try:
                option = int(input('Enter your choice: '))
                break
            except ValueError:
                print_error("Invalid input. Please enter a number!")
                option = None
                continue
        if option == 1:
            menu_option1_add()
        elif option == 2:
            menu_option2_sort()
        elif option == 3:
            menu_option3_cast_out()
        elif option == 4:
            menu_option4_sell()
        elif option == 5:
            menu_option5_buy()
        elif option == 6:
            menu_option6_exit()
        else:
            print_error("\nInvalid option. Please enter a number between 1 and 6.\n")


if __name__ == '__main__':
    FishShop.sorting_reverse = True      # "True" if you want from largest to smallest, "False" to reverse.
    FishShop.sorting_key = "price"       # What do you want to sort fish_list by? (name, price or weight)!
    main()
