"""
Unit tests file
"""

import FishShop


def test_sublist_search():
    assert FishShop.sublist_search(FishShop.FishShop.list_of_fishes, "") is False, "Must be False"


test_sublist_search()
