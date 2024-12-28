# Python Project Boilerplate

[![CI](https://github.com/pythonpete32/python-boilerplate/actions/workflows/ci.yml/badge.svg)](https://github.com/pythonpete32/python-boilerplate/actions/workflows/ci.yml)
[![Python 3.8+](https://img.shields.io/badge/python-3.8+-blue.svg)](https://www.python.org/downloads/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)
[![Ruff](https://img.shields.io/endpoint?url=https://raw.githubusercontent.com/astral-sh/ruff/main/assets/badge/v2.json)](https://github.com/astral-sh/ruff)
[![Imports: isort](https://img.shields.io/badge/%20imports-isort-%231674b1?style=flat&labelColor=ef8336)](https://pycqa.github.io/isort/)
[![Checked with mypy](https://www.mypy-lang.org/static/mypy_badge.svg)](https://mypy-lang.org/)

A minimal Python project boilerplate with modern tooling setup.

## Features

- 🛠️ Modern development tools (black, isort, ruff, mypy)
- 📦 Simple dependency management
- 🧪 Testing setup with pytest
- 🔧 Environment variable support
- 🎨 Rich console output
- ✨ VSCode integration with auto-formatting
- 📋 Comprehensive coding standards (see `.cursorrules`)

## Requirements

- Python 3.8+
- Make (optional, for using Makefile commands)
- VSCode (recommended)

## Installation

1. Clone the repository:

```bash
git clone https://github.com/abuusama/python-boilerplate.git
cd python-boilerplate
```

2. Create and activate a virtual environment:

```bash
python -m venv .venv
source .venv/bin/activate  # On Windows: .venv\Scripts\activate
```

3. Install the package with development dependencies:

```bash
make install  # or: uv pip install -e ".[dev]"
```

## Environment Setup

1. Copy the sample environment file:

```bash
cp .env.sample .env
```

2. Edit `.env` with your configuration:

```bash
ENV=development
DEBUG=true
```

## Scripts

The project includes several scripts for common development tasks:

### Development Tools

```bash
# Install dependencies
make install

# Format code
make format

# Run linting checks
make lint

# Run tests
make test

# Run the application
make run

# Clean build artifacts
make clean
```

### Individual Commands

You can also run the tools directly:

```bash
# Format code with black
python -m black src tests

# Sort imports with isort
python -m isort src tests

# Lint with ruff
python -m ruff check src tests

# Type check with mypy
python -m mypy src tests

# Run tests with pytest
python -m pytest tests -v

# Run the application
python -m src.main
```

## Development Commands

The project includes a Makefile with common development tasks:

- `make install`: Install the package and development dependencies
- `make format`: Format code with black and isort
- `make lint`: Run all linting checks (ruff, black, isort, mypy)
- `make test`: Run tests with pytest
- `make run`: Run the main application
- `make clean`: Clean up build artifacts and cache files

## Project Structure

```
python-boilerplate/
├── src/
│   ├── __init__.py
│   ├── main.py
│   ├── config.py
│   └── console.py
├── tests/
│   ├── __init__.py
│   ├── test_main.py
│   ├── test_config.py
│   └── test_console.py
├── .vscode/
│   ├── settings.json
│   └── extensions.json
├── .env.sample
├── .gitignore
├── LICENSE
├── Makefile
├── README.md
└── pyproject.toml
```

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Contributing

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add some amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## Acknowledgments

- [black](https://github.com/psf/black) - The uncompromising code formatter
- [ruff](https://github.com/astral-sh/ruff) - An extremely fast Python linter
- [rich](https://github.com/Textualize/rich) - Rich text and beautiful formatting in the terminal
- [pytest](https://github.com/pytest-dev/pytest) - Testing framework
