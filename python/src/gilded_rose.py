"""
Gilded Rose Inventory Manager

This module defines the `GildedRose` class, which manages a list of items and
updates their quality and sell_in values using the strategy pattern.

Functions:
    GildedRose.update_quality(): Applies update logic to each item using its associated strategy.
    GildedRose.display_items(): Prints a formatted list of all items after updates.
"""

from typing import List
from .strategies import get_strategy
from .models import Item

class GildedRose:
    """
    Manages a collection of items and updates their state based on item-specific strategies.

    Attributes:
        items (List[Item]): A list of items to manage.
    """

    def __init__(self, items: List[Item]):
        """
        Initializes the GildedRose manager with a list of items.

        Args:
            items (List[Item]): The initial list of items to be managed.
        """
        self.items = items

    def update_quality(self) -> None:
        """
        Updates the quality and sell_in values of all items in the inventory.

        Delegates the logic to appropriate strategy implementations based on item type.
        """
        for item in self.items:
            strategy = get_strategy(item)
            strategy.update()

    def display_items(self) -> None:
        """
        Displays the current list of items in a formatted manner.
        """
        print("Updated Items:")
        for item in self.items:
            print(f"  - {item}")
