#  Gilded Rose Inventory Manager

A clean Python implementation of the Gilded Rose Kata using the Strategy Pattern. This project is Dockerized, unit tested with Pytest, and follows PEP8 standards for clean code.

---

## Tech Stack

- Python 3.12  
- Docker  
- Pytest + Coverage  
- Strategy Design Pattern  
- PEP8 + Linting  

---

## Project Structure

```text
gildedrose/
├── Dockerfile
├── README.md
├── requirements.txt
├── entrypoint.sh
├── src/
│   ├── __init__.py
│   ├── models.py             # Item model and base strategy class
│   ├── strategies.py         # Strategy implementations (Aged Brie, Backstage, etc.)
│   └── gilded_rose.py        # Inventory manager using strategy pattern
├── tests/
│   ├── __init__.py
│   ├── test_models.py
│   ├── test_strategies.py
│   └── test_gilded_rose.py
```

## Run is Locally

### Install Required Package
    
    pip install -r requirements.txt
    

### Run Application in Locally
    
        python main.py
    

### Run Test Locally
    ```text
        pytest --cov=src --cov-report=term-missing --cov-report=html
    ```


## Run Via Docker

### Create Docker Build
    ```text
        docker build -t gildedrose .
    ```
    
### Run Docker container
    ```text
        docker run --rm gildedrose
    ```