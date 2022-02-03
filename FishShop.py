from operator import itemgetter


class Fish:

    def __init__(self) -> None:
        self.name = input("Enter fish name: ")
        self.price_in_uah_per_kilo = input("Enter price in UAH per kg: ")
        self.body_only = input("Is fish body only? ")
        self.origin = input("Enter fish origin: ")
        self.weight = input("Enter fish weight: ")


class FishShop:
    list_of_fishes = []

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

    def get_fish_names_sorted_by_price(self):
        print("Sorted List based on price: %s" % (sorted(self.list_of_fishes, key=itemgetter(1), reverse=True)))

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
    shop = FishShop()

    shop.add_fish()
    shop.add_fish()
    shop.add_fish()

    shop.get_fish_names_sorted_by_price()

    shop.sell_fish()
    shop.cast_out_old_fish()


if __name__ == '__main__':
    main()
    