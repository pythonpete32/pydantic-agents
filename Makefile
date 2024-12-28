.PHONY: install format lint test clean run

install:
	uv pip install -e ".[dev]"

format:
	python -m black src tests
	python -m isort src tests

lint:
	python -m ruff check src tests
	python -m black --check src tests
	python -m isort --check-only src tests
	python -m mypy src tests

test:
	python -m pytest tests -v

run:
	python -m src.main

clean:
	rm -rf build/
	rm -rf dist/
	rm -rf *.egg-info
	find . -type d -name __pycache__ -exec rm -rf {} +
	find . -type f -name "*.pyc" -delete
	find . -type f -name "*.pyo" -delete
	find . -type f -name "*.pyd" -delete
	find . -type f -name ".coverage" -delete
	find . -type d -name "*.egg" -exec rm -rf {} +
	find . -type d -name ".pytest_cache" -exec rm -rf {} +
	find . -type d -name ".mypy_cache" -exec rm -rf {} +
	find . -type d -name ".ruff_cache" -exec rm -rf {} + 