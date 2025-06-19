from src.models import Item
from src.gilded_rose import GildedRose

if __name__ == "__main__":
    items = [
        Item("Aged Brie", 2, 0),
        Item("Backstage passes to a TAFKAL80ETC concert", 15, 20),
        Item("Normal Item", 10, 20),
        Item("Sulfuras, Hand of Ragnaros", 0, 80),
    ]

    gr = GildedRose(items)
    gr.update_quality()
    gr.display_items()