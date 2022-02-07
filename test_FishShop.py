"""
Unit tests file
"""

import FishShop


def test_sublist_search():
    assert FishShop.FishShop.sublist_search(FishShop.FishShop(), "") is False, "Must be False"


test_sublist_search()
