""" FishShop.py
This program provides you with a simple functionality for fish shop management.
Here you can add fish to the store, sort them as you wish,
sell them, or even cast them out if they are expired.
For further information please see our GitHub repository:
https://github.com/andylvua/WinterSchool
"""

from operator import itemgetter
import inflect

__author__ = "Andrew Yaroshevych and Oles Pasirskyi"
__version__ = "1.1"
__email__ = "andrii.yaroshevych.ir.2021@lpnu.ua, oles.pasirskyi.ir.2021@lpnu.ua"
__status__ = "Production"


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
                print("Name should contain only letters, please try again!")
                continue

        while True:
            try:
                fish_price_in_uah_per_kilo = float(input("Enter price in UAH per kg: "))
                if fish_price_in_uah_per_kilo > 0:
                    break
                else:
                    print("Price should be greater than 0, try again")
            except ValueError:
                fish_price_in_uah_per_kilo = None
                print("Price should be a float value, try again")
                continue

        while True:
            try:
                fish_weight = float(input("Enter weight: "))
                if fish_weight > 0:
                    break
                else:
                    print("Weight should be greater than 0, try again")
            except ValueError:
                fish_weight = None
                print("Weight should be a float value, try again")
                continue

        self.list_of_fishes.append([fish_name, fish_price_in_uah_per_kilo, fish_weight])
        print("Fish added successfully.\n")

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
                    print("Fish is not found, please try again!")
            else:
                print("Name should contain only letters, please try again!")
                continue

        while True:
            try:
                weight = float(input("How much do you want to cast out? "))
                if weight > 0:
                    break
                else:
                    print("Weight should be greater than 0, try again")
            except ValueError:
                weight = None
                print("Weight should be a float value, try again")
                continue

        for i in range(len(self.list_of_fishes)):
            if self.list_of_fishes[i][0] == fish_name:
                if self.list_of_fishes[i][2] > weight:
                    self.list_of_fishes[i][2] -= weight
                    print("Casted out successfully.")
                    print("List of fishes after casting out: %s" % self.list_of_fishes + "\n")
                else:
                    print("There is not enough fish to cast out, try again!")
                    self.cast_out_old_fish()


class Seller(FishShop):
    def sell_fish(self):
        while True:
            fish_name = str(input("Which fish do you want to sell? "))
            if fish_name.replace(" ", "").isalpha():
                if self.sublist_search(fish_name):
                    break
                else:
                    print("Fish is not found, please try again!")
            else:
                print("Name should contain only letters, please try again!")
                continue

        while True:
            try:
                weight = float(input("How much do you want to sell? "))
                if weight > 0:
                    break
                else:
                    print("Weight should be greater than 0, try again")
            except ValueError:
                weight = None
                print("Weight should be a float value, try again")
                continue

        for i in range(len(self.list_of_fishes)):
            if self.list_of_fishes[i][0] == fish_name:
                if self.list_of_fishes[i][2] > weight:
                    self.list_of_fishes[i][2] -= weight
                    print("\nSold successfully.")
                else:
                    print("There is not enough fish to sell, try again!")
                    self.sell_fish()

                revenue = int(self.list_of_fishes[i][1]) * weight
                print("Selling revenue is: " + str(revenue))
                print("List of fishes after selling: %s" % self.list_of_fishes + "\n")


class Buyer:
    list_of_bought_fishes = []
    money_spent = int

    def __init__(self):
        self.money_amount = float(input("How much money do you have? "))

    def buy_fish(self):
        while True:

            fish_name = str(input("Which fish do you want to buy? "))
            if fish_name.replace(" ", "").isalpha():
                if FishShop.sublist_search(FishShop(), fish_name):
                    break
                else:
                    print('Fish is not found, please try again!')
            else:
                print("Name should contain only letters, please try again!")
                continue

        while True:
            try:
                weight = float(input("How much do you want to buy? "))
                if weight > 0:
                    break
                else:
                    print("Weight should be greater than 0, try again")
            except ValueError:
                weight = None
                print("Weight should be a float value, try again")
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
                        print("Your bag [name, weight]: " + str(self.list_of_bought_fishes))
                    else:
                        print("You don't have enough money, try again!")
                        self.buy_fish()
                else:
                    print("Sorry, here is not enough fish to sell to you, try again!")
                    self.buy_fish()

    def haggle(self, fish_price_in_uah):
        pass


def main():
    if FishShop.sorting_key not in ('name', 'price', 'weight'):
        print("Check sorting_key value in __main__")
        raise ValueError()

    print("\n---------Welcome to FishShop!---------\n\nNow, please add some fishes.\n"
          "To do that, just follow the instructions below:\n")

    shop = FishShop()

    number_of_fishes = int(input("How many fishes do you want to add to the store? "))
    print()

    for i in range(1, number_of_fishes+1):
        iteration = inflect.engine()
        print("Enter " + iteration.number_to_words(iteration.ordinal(i)) + " fish name: ", end="")
        shop.add_fish()

    shop.get_sorted_fish_list()
    shop.cast_out_old_fish()

    seller = Seller()
    seller.sell_fish()

    print("\n---------Hi, dear buyer!---------\n")
    buyer = Buyer()
    buyer.buy_fish()


if __name__ == '__main__':
    FishShop.sorting_reverse = True  # "True" if you want from largest to smallest, "False" to reverse.
    FishShop.sorting_key = "price"   # What do you want to sort fish_list by? (name, price or weight)!
    main()
