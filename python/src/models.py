"""
Item Strategy Module

This module provides a strategy pattern implementation for updating the properties
of different items over time. It defines a base `Item` class, an abstract base
class `ItemStrategy` for implementing custom item behavior, and enforces a structure
for extending item-specific update logic.

Classes:
    Item: Represents an item with a name, sell-in value, and quality.
    ItemStrategy (ABC): Abstract base class for item update strategies.

Typical usage:
    class CustomItemStrategy(ItemStrategy):
        def update(self):
            # Custom update logic
            ...

    item = Item("Example", 10, 20)
    strategy = CustomItemStrategy(item)
    strategy.update()
"""

from abc import ABC, abstractmethod


# ------------------------
# Item Class (Base Data)
# ------------------------
class Item:
    """
    Represents a generic item with attributes to track name, sell-in days, and quality.

    Attributes:
        name (str): The name of the item.
        sell_in (int): The number of days to sell the item.
        quality (int): The quality of the item.
    """

    def __init__(self, name: str, sell_in: int, quality: int):
        """
        Initializes a new item with the given name, sell-in value, and quality.

        Args:
            name (str): Name of the item.
            sell_in (int): Days remaining to sell the item.
            quality (int): Quality score of the item.
        """
        self.name = name
        self.sell_in = sell_in
        self.quality = quality

    def __repr__(self) -> str:
        """
        Returns a string representation of the item.

        Returns:
            str: A string containing the item name, sell_in, and quality.
        """
        return f"{self.name}, {self.sell_in}, {self.quality}"


# ------------------------
# Strategy Base Class
# ------------------------
class ItemStrategy(ABC):
    """
    Abstract base class for defining update strategies for different item types.

    Each subclass must implement the `update` method to modify the associated
    item's state according to specific rules.

    Attributes:
        item (Item): The item instance associated with this strategy.
    """

    def __init__(self, item: Item):
        """
        Initializes the strategy with a specific item.

        Args:
            item (Item): The item this strategy will operate on.
        """
        self.item = item

    @abstractmethod
    def update(self) -> None:
        """
        Abstract method to update the item's state.

        This method must be implemented by all subclasses to define how the
        item should change as time progresses.
        """
        ...
