echo "Check Application"
python main.py

echo "Code Covrage and Test Case"
pytest --cov=src --cov-report=term-missing --cov-report=html

echo "Done"
