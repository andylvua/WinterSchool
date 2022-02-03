""" FishShop.py
This program provides you with a simple functionality for fish shop management.
Here you can add fish to the store, sort them as you wish,
sell them, or even cast them out if they are expired.

For further information please see our GitHub repository:
https://github.com/andylvua/WinterSchool
"""

from operator import itemgetter

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
            fish_name = str(input("Enter fish name: "))
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
                fish_weight = float(input("Enter fish weight: "))
                if fish_weight > 0:
                    break
                else:
                    print("Weight should be greater than 0, try again")
            except ValueError:
                fish_weight = None
                print("Weight should be a float value, try again")
                continue

        self.list_of_fishes.append([fish_name, fish_price_in_uah_per_kilo, fish_weight])

    def get_sorted_fish_list(self):
        if self.sorting_key == "name":
            self.sorting_key = 0
        elif self.sorting_key == "price":
            self.sorting_key = 1
        elif self.sorting_key == "weight":
            self.sorting_key = 2
        print("Sorted List of fishes: %s" % (sorted(self.list_of_fishes, key=itemgetter(self.sorting_key),
                                                    reverse=self.sorting_reverse)))

    def sublist_search(self, searched_element) -> bool:
        return any(searched_element in sublist for sublist in self.list_of_fishes)

    def sell_fish(self, shop=None):
        while True:
            fish_name = str(input("Which fish do you want to sell? "))
            if fish_name.replace(" ", "").isalpha():
                if shop.sublist_search(fish_name):
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
                else:
                    print("There is not enough fish to sell, try again!")
                    self.sell_fish()

                revenue = int(self.list_of_fishes[i][1]) * weight
                print("Revenue is: " + str(revenue))
                print(self.list_of_fishes)

    def cast_out_old_fish(self, shop=None):
        while True:
            fish_name = str(input("Which fish do you want to cast out? "))
            if fish_name.replace(" ", "").isalpha():
                if shop.sublist_search(fish_name):
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
                    print(self.list_of_fishes)
                else:
                    print("There is not enough fish to cast out, try again!")
                    self.cast_out_old_fish()


class Seller:
    def sell_fish(self, fish_type: str, fish_weight: float):
        pass

    def haggle(self, fish_price_in_uah):
        pass


class Buyer:
    def buy_fish(self, fish_type: str, fish_weight: float):
        pass

    def haggle(self, fish_price_in_uah):
        pass

    def get_fish_info(self, fish_type):
        pass


def main():
    if FishShop.sorting_key not in ('name', 'price', 'weight'):
        print("Check sorting_key value in __main__")
        raise ValueError()

    shop = FishShop()

    shop.add_fish()
    shop.add_fish()
    shop.add_fish()

    print("Sorting by", FishShop.sorting_key, end=' ')
    if FishShop.sorting_reverse:
        print("in decreasing order")
    else:
        print("in increasing order")

    shop.get_sorted_fish_list()

    shop.sell_fish()
    shop.cast_out_old_fish()


if __name__ == '__main__':
    FishShop.sorting_reverse = True  # "True" if you want from largest to smallest
    FishShop.sorting_key = "piece"  # What do you want to sort fish_list by? (name, price or weight)
    main()
