import pytest
from ..src.gilded_rose import GildedRose
from ..src.models import Item


# --------------------
# Integration-style tests
# --------------------

def test_gilded_rose_with_multiple_items():
    items = [
        Item("Aged Brie", sell_in=2, quality=0),
        Item("Backstage passes to a TAFKAL80ETC concert", sell_in=15, quality=20),
        Item("Sulfuras, Hand of Ragnaros", sell_in=0, quality=80),
        Item("Normal Item", sell_in=10, quality=20),
    ]
    gr = GildedRose(items)
    gr.update_quality()

    # Aged Brie: +1
    assert items[0].quality == 1
    assert items[0].sell_in == 1

    # Backstage pass: +1 (>10 days)
    assert items[1].quality == 21
    assert items[1].sell_in == 14

    # Sulfuras: no change
    assert items[2].quality == 80
    assert items[2].sell_in == 0

    # Normal Item: -1
    assert items[3].quality == 19
    assert items[3].sell_in == 9


def test_gilded_rose_display_items(capsys):
    items = [Item("Aged Brie", 5, 10), Item("Normal Item", 1, 20)]
    gr = GildedRose(items)
    gr.display_items()

    captured = capsys.readouterr()
    assert "Aged Brie, 5, 10" in captured.out
    assert "Normal Item, 1, 20" in captured.out
    assert "Updated Items:" in captured.out

