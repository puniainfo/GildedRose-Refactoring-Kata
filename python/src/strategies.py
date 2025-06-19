"""
Item Strategy Implementations

This module contains specific strategy classes that define how different types
of items behave over time. Each strategy inherits from `ItemStrategy` and implements
the `update()` method to adjust the `Item`'s sell_in and quality values according
to custom rules.

Classes:
    NormalItem: Standard item that degrades in quality over time.
    AgedBrie: Item that increases in quality as it gets older.
    BackstagePass: Item that increases in quality as a concert approaches and drops to 0 after.
    Sulfuras: Legendary item that does not change in quality or sell-in.

For New ItemStrategy Add
class SampleItem(ItemStrategy):
    def update(self) -> None:
        Add Logic Here

"""

from .models import ItemStrategy,Item
from typing import  Type

class NormalItem(ItemStrategy):
    """
    Strategy for standard items.

    Quality decreases by 1 each day before the sell_in date,
    and by 2 each day after the sell_in date.
    """

    def update(self) -> None:
        """
        Updates the sell_in and quality values for a normal item.
        """
        self.item.sell_in -= 1
        degrade = 2 if self.item.sell_in < 0 else 1
        self.item.quality = max(0, self.item.quality - degrade)


class AgedBrie(ItemStrategy):
    """
    Strategy for 'Aged Brie'.

    Quality increases over time. It increases by 1 before the sell_in date,
    and by 2 after it passes. Quality is capped at 50.
    """

    def update(self) -> None:
        """
        Updates the sell_in and quality values for Aged Brie.
        """
        self.item.sell_in -= 1
        increase = 2 if self.item.sell_in < 0 else 1
        self.item.quality = min(50, self.item.quality + increase)


class BackstagePass(ItemStrategy):
    """
    Strategy for 'Backstage passes to a TAFKAL80ETC concert'.

    - Increases in quality as the sell_in date approaches:
        - +1 when more than 10 days left
        - +2 when 10 days or fewer
        - +3 when 5 days or fewer
    - Quality drops to 0 after the concert (sell_in < 0).
    """

    def update(self) -> None:
        """
        Updates the sell_in and quality values for a Backstage Pass.
        """
        self.item.sell_in -= 1
        if self.item.sell_in < 0:
            self.item.quality = 0
        elif self.item.sell_in < 5:
            self.item.quality = min(50, self.item.quality + 3)
        elif self.item.sell_in < 10:
            self.item.quality = min(50, self.item.quality + 2)
        else:
            self.item.quality = min(50, self.item.quality + 1)


class Sulfuras(ItemStrategy):
    """
    Strategy for 'Sulfuras, Hand of Ragnaros'.

    This is a legendary item and does not change in quality or sell_in.
    """

    def update(self) -> None:
        """
        Does not update the item because Sulfuras is immutable.
        """
        pass  # Legendary item, no change in sell_in or quality


def get_strategy(item: Item) -> ItemStrategy:
    """
    Returns the appropriate update strategy for a given item.

    This function uses the item's name to determine which strategy class
    should be used to update its quality and sell_in values. If the item
    is not a special case (e.g. "Aged Brie", "Backstage passes", or "Sulfuras"),
    it defaults to using the NormalItem strategy.

    Args:
        item (Item): The item for which to retrieve the strategy.

    Returns:
        ItemStrategy: An instance of the appropriate strategy class for the item.
    """
    strategy_map: dict[str, Type[ItemStrategy]] = {
        "Aged Brie": AgedBrie,
        "Backstage passes to a TAFKAL80ETC concert": BackstagePass,
        "Sulfuras, Hand of Ragnaros": Sulfuras,
        #Add Future Strategy Here 
    }
    return strategy_map.get(item.name, NormalItem)(item)
