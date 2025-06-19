import pytest
from ..src.strategies import NormalItem, AgedBrie, BackstagePass, Sulfuras, get_strategy
from ..src.models import Item


@pytest.mark.parametrize("sell_in, quality, expected_sell_in, expected_quality", [
    (10, 20, 9, 19),      # Before expiry
    (0, 20, -1, 18),      # On expiry
    (-1, 20, -2, 18),     # After expiry
    (5, 0, 4, 0),         # Quality cannot go below 0
])
def test_normal_item(sell_in, quality, expected_sell_in, expected_quality):
    item = Item("Normal Item", sell_in, quality)
    strategy = NormalItem(item)
    strategy.update()
    assert item.sell_in == expected_sell_in
    assert item.quality == expected_quality


@pytest.mark.parametrize("sell_in, quality, expected_sell_in, expected_quality", [
    (10, 40, 9, 41),      # Before expiry
    (0, 40, -1, 42),      # On expiry
    (-1, 49, -2, 50),     # Cap at 50
    (5, 50, 4, 50),       # Quality already max
])
def test_aged_brie(sell_in, quality, expected_sell_in, expected_quality):
    item = Item("Aged Brie", sell_in, quality)
    strategy = AgedBrie(item)
    strategy.update()
    assert item.sell_in == expected_sell_in
    assert item.quality == expected_quality


@pytest.mark.parametrize("sell_in, quality, expected_sell_in, expected_quality", [
    (15, 20, 14, 21),     # >10 days
    (10, 20, 9, 22),      # 10–6 days
    (6, 20, 5, 22),       # Just above 5
    (5, 20, 4, 23),       # Exactly 5
    (1, 48, 0, 50),       # +3 but max 50
    (0, 40, -1, 0),       # After concert
])
def test_backstage_pass(sell_in, quality, expected_sell_in, expected_quality):
    item = Item("Backstage passes to a TAFKAL80ETC concert", sell_in, quality)
    strategy = BackstagePass(item)
    strategy.update()
    assert item.sell_in == expected_sell_in
    assert item.quality == expected_quality


def test_sulfuras():
    item = Item("Sulfuras, Hand of Ragnaros", sell_in=0, quality=80)
    strategy = Sulfuras(item)
    strategy.update()
    assert item.sell_in == 0
    assert item.quality == 80


@pytest.mark.parametrize("item_name,expected_strategy", [
    ("Aged Brie", AgedBrie),
    ("Backstage passes to a TAFKAL80ETC concert", BackstagePass),
    ("Sulfuras, Hand of Ragnaros", Sulfuras),
    ("Normal Item", NormalItem),
    ("Unknown Item", NormalItem),
])
def test_get_strategy(item_name, expected_strategy):
    item = Item(item_name, sell_in=5, quality=10)
    strategy = get_strategy(item)
    assert isinstance(strategy, expected_strategy)
