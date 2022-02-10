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
import config
from cprint import print_ok, print_warning, print_error, print_quit

__author__ = "Andrew Yaroshevych and Oles Pasirskyi"
__version__ = "2.3"
__email__ = "andrii.yaroshevych.ir.2021@lpnu.ua, oles.pasirskyi.ir.2021@lpnu.ua"
__status__ = "Production"


class Fish:
    def __init__(self) -> None:
        self.name = input("Enter fish name: ")
        self.price_in_uah_per_kilo = input("Enter price in UAH per kg: ")
        self.body_only = input("Is fish body only? ")
        self.origin = input("Enter fish origin: ")
        self.weight = input("Enter fish weight: ")


def get_fish_name(index) -> str:
    while True:
        fish_name = str(input("Enter " + index + "fish name: "))
        if fish_name.replace(" ", "").isalpha():
            if sublist_search(FishShop.list_of_fishes, fish_name) or not FishShop.list_of_fishes:
                return fish_name
            else:
                print_warning("Fish is not found in the shop!")
        else:
            print_warning("Name should contain only letters, please try again!")
            continue


def get_fish_price() -> float:
    while True:
        try:
            fish_price_in_uah_per_kilo = float(input("Enter price in UAH per kg: "))
            if fish_price_in_uah_per_kilo > 0:
                return fish_price_in_uah_per_kilo
            else:
                print_warning("Price should be greater than 0, try again!")
        except ValueError:
            print_error("Price should be a float value, try again!")
            continue


def get_fish_weight() -> float:
    while True:
        try:
            fish_weight = float(input("Enter weight: "))
            if fish_weight > 0:
                return fish_weight
            else:
                print_warning("Weight should be greater than 0, try again!")
        except ValueError:
            print_error("Weight should be a float value, try again!")
            continue


def fish_check(list_of_fishes, fish_name, weight) -> tuple:
    for i in range(len(list_of_fishes)):
        if list_of_fishes[i][0] == fish_name:
            if list_of_fishes[i][2] > weight:
                return True, i
            else:
                return False, i


def sublist_search(list_of_fishes, searched_element) -> bool:
    return any(searched_element in sublist for sublist in list_of_fishes)


class FishShop:
    list_of_fishes = []
    sorting_reverse = None
    sorting_key = None
    max_discount = None

    def get_sorting_key(self):
        if self.sorting_key == "name":
            return 0
        elif self.sorting_key == "price":
            return 1
        elif self.sorting_key == "weight":
            return 2

    def add_fish(self, index) -> None:
        fish_name = get_fish_name(index)
        fish_price_in_uah_per_kilo = get_fish_price()
        fish_weight = get_fish_weight()

        self.list_of_fishes.append([fish_name, fish_price_in_uah_per_kilo, fish_weight])

        print_ok("Fish added successfully.\n")

    def get_sorted_fish_list(self):
        print("Sorting by", self.sorting_key, end=' ')

        if FishShop.sorting_reverse:
            print("in decreasing order")
        else:
            print("in increasing order")

        print("Sorted list of fishes: %s" % (sorted(self.list_of_fishes, key=itemgetter(self.get_sorting_key()),
                                                    reverse=self.sorting_reverse)) + "\n")

    def cast_out_old_fish(self):
        fish_name = get_fish_name("")
        weight = get_fish_weight()

        check_result = fish_check(FishShop.list_of_fishes, fish_name, weight)

        if check_result[0]:
            self.list_of_fishes[check_result[1]][2] -= weight
            print_ok("\nCasted out successfully.")
            print("List of fishes after casting out: %s" % self.list_of_fishes + "\n")
        else:
            print_warning("There is not enough fish to cast out, try again!")
            self.cast_out_old_fish()


class Seller(FishShop):
    def sell_fish(self):
        fish_name = get_fish_name("")
        weight = get_fish_weight()

        check_result = fish_check(FishShop.list_of_fishes, fish_name, weight)

        if check_result[0]:
            self.list_of_fishes[check_result[1]][2] -= weight
            print_ok("\nSold successfully.")
            print("List of fishes after selling: %s" % self.list_of_fishes + "\n")
        else:
            print_warning("There is not enough fish to sell, try again!")
            self.cast_out_old_fish()

        revenue = int(self.list_of_fishes[check_result[1]][1]) * weight
        print_ok("Selling revenue is: " + str(revenue) + " UAH\n")


class Buyer:
    list_of_bought_fishes = []
    money_spent = int
    money_amount = None

    def buy_fish(self):
        fish_name = get_fish_name("")
        weight = get_fish_weight()

        check_result = fish_check(FishShop.list_of_fishes, fish_name, weight)

        if check_result[0]:
            FishShop.list_of_fishes[check_result[1]][2] -= weight
            while True:
                haggle_proposition = str(input("Do you want to haggle with the seller?\n(Y or N) ")).upper()
                if haggle_proposition in ("Y", "N"):
                    break
                else:
                    print_warning("Answer must be Y or N, try again!")
                    continue

            desired_price_decimal = 1

            if haggle_proposition == "Y":
                while True:
                    try:
                        desired_discount = float(input("What discount do you want (in percents)? "))
                        if 0 < desired_discount <= FishShop.max_discount:
                            desired_price_decimal -= desired_discount / 100
                            break
                        elif desired_discount > FishShop.max_discount:
                            print_warning("Seller rejected your proposition, try lowering desired discount")
                            continue
                        else:
                            print_warning("Discount should be greater than 0, try again!")
                    except ValueError:
                        print_error("Discount should be a float value, try again!")
                        continue

            if ((FishShop.list_of_fishes[check_result[1]][1]) * weight * desired_price_decimal) <= self.money_amount:
                self.money_spent = (FishShop.list_of_fishes[check_result[1]][1]) * weight * desired_price_decimal
                self.list_of_bought_fishes.append([fish_name, weight])
                self.money_amount -= self.money_spent
                print("\nMoney spent: " + str(self.money_spent))
                print("Your funds after buying: " + str(self.money_amount))
                print_ok("Your shopping bag [Fish name, weight]: " + str(self.list_of_bought_fishes) + "\n")
            else:
                print_warning("You don't have enough money, try again!")
                self.buy_fish()
        else:
            print_warning("Sorry, here is not enough fish to sell to you, try again!")
            self.buy_fish()


def main():
    if FishShop.sorting_key not in ('name', 'price', 'weight'):
        print_error("\nCheck sorting_key value in config.py\nThe only allowed values "
                    "for sorting_key are 'name', 'price' and 'weight'.")
        raise ValueError()

    if FishShop.max_discount not in range(0, 100):
        print_error("\nCheck max_discount value in config.py, it should be in range from 0 to 100")
        raise ValueError()

    shop = FishShop()
    seller = Seller()
    buyer = Buyer()
    first_buyer = True

    def print_options(menu_options=config.menu_options):
        time.sleep(0.7)
        print("Menu:")
        for key in menu_options.keys():
            print(key, '--', menu_options[key])
        print()

    def menu_input():
        print_options()
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

    def buyer_init():
        print("\n---------Hi, dear buyer!---------\n")

        if not FishShop.list_of_fishes:
            print_warning("Sorry, the store is empty, please add some fishes first.\n")

        while True:
            try:
                Buyer.money_amount = int(input("How much money do you have? "))
                print()
                break
            except ValueError:
                print_error("Invalid input. Please enter an integer value")
                continue

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
            shop.add_fish((iteration.number_to_words(iteration.ordinal(i))) + " ")

    def menu_option2_sort():
        shop.get_sorted_fish_list()

    def menu_option3_cast_out():
        shop.cast_out_old_fish()

    def menu_option4_sell():
        seller.sell_fish()

    def menu_option5_buy():
        nonlocal first_buyer
        nonlocal buyer

        if first_buyer:
            buyer_init()
            buyer.buy_fish()

            first_buyer = False
        else:
            buyer.buy_fish()

    def menu_option6_exit():
        print_quit()
        exit()

    print("\n---------Welcome to FishShop!---------\n\n"
          "You can see the list of options below:\n")

    while True:
        menu_input()


if __name__ == '__main__':
    FishShop.sorting_reverse = config.sorting_reverse
    FishShop.sorting_key = config.sorting_key
    FishShop.max_discount = config.max_discount
    main()
