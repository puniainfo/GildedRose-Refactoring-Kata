import pytest
from ..src.models import Item, ItemStrategy

# Mock subclass of ItemStrategy for testing
class MockStrategy(ItemStrategy):
    def update(self):
        self.item.sell_in -= 1  # Simplified behavior for testing


def test_item_initialization():
    item = Item(name="Mock Item", sell_in=10, quality=20)
    assert item.name == "Mock Item"
    assert item.sell_in == 10
    assert item.quality == 20
    assert repr(item) == "Mock Item, 10, 20"


def test_strategy_initialization():
    item = Item("Mock", 5, 25)
    strategy = MockStrategy(item)
    assert strategy.item is item


def test_strategy_update_behavior():
    item = Item("Mock", 5, 25)
    strategy = MockStrategy(item)
    strategy.update()
    assert item.sell_in == 4
    assert item.quality == 25  # Should remain unchanged


def test_abstract_method_enforcement():
    # Attempting to instantiate an abstract class should raise TypeError
    with pytest.raises(TypeError):
        class InvalidStrategy(ItemStrategy):
            pass

        InvalidStrategy(Item("Invalid", 1, 1))
