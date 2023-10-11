# Variables
PYTHON3 = python3
PYTEST = pytest
CLASS_FILE = trying.py
TEST_FILE = test_case.py

install:
	pip install pytest

test:
	@$(PYTHON3) $(TEST_FILE)

clean:
	@echo "Cleaning up..."
	@rm -f *.pyc
	@rm -rf __pycache__
