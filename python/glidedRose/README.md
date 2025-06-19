This folder contains the **core application logic** for the Gilded Rose Kata, implemented using clean, object-oriented Python.

## 📁 Purpose of This Folder

The goal of this module is to:
- Separate **business rules** from infrastructure
- Enable **scalable item behavior** via the Strategy Pattern
- Keep the logic **testable**, **type-safe**, and **maintainable**

## 🧱 Folder Structure

models.py # Basic Item class Abstract base class for strategies
strategies.py # Strategy classes per item type
gilded_rose.py # Main manager class to update all items
main.py # Sample runner

Test/ # All Test Case
Test/test_gilded_rose.py # Pytest unit tests

