# Pydantic Agents

[![CI](https://github.com/pythonpete32/python-boilerplate/actions/workflows/ci.yml/badge.svg)](https://github.com/pythonpete32/python-boilerplate/actions/workflows/ci.yml)
[![Python 3.10+](https://img.shields.io/badge/python-3.10+-blue.svg)](https://www.python.org/downloads/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)
[![Ruff](https://img.shields.io/endpoint?url=https://raw.githubusercontent.com/astral-sh/ruff/main/assets/badge/v2.json)](https://github.com/astral-sh/ruff)

A collection of agents using PydanticAI.

## Features

- 🤖 Agents showcasing PydanticAI capabilities
- 📊 Logfire integration for monitoring
- 🛠️ Modern development tools (black, isort, ruff, mypy)
- 📦 UV package management
- 🧪 Testing setup with pytest

## Requirements

- Python 3.10+
- UV package manager
- Make (optional, for using Makefile commands)

## Installation

1. Clone the repository:

```bash
git clone https://github.com/yourusername/pydantic-agents.git
cd pydantic-agents
```

2. Create and activate a virtual environment:

```bash
uv venv
source .venv/bin/activate  # On Windows: .venv\Scripts\activate
```

3. Install the package with development dependencies:

```bash
uv pip install -e ".[dev]"
```

## Demo Agents

### Hello World Agent

A simple agent that demonstrates basic PydanticAI usage:

```python
from pydantic_ai import Agent

agent = Agent(
    "gemini-1.5-flash",
    system_prompt="Be concise, reply with one sentence.",
)

result = agent.run_sync("Where does 'hello world' come from?")
print(result.data)
```

### Bank Support Agent

A more complex example showing dependency injection and tools:

```python
from pydantic_ai import Agent, RunContext
from pydantic import BaseModel, Field

class SupportResult(BaseModel):
    support_advice: str
    block_card: bool
    risk: int

support_agent = Agent(
    "openai:gpt-4",
    result_type=SupportResult,
    system_prompt="You are a bank support agent...",
)
```

## Development Commands

The project includes a Makefile with common development tasks:

- `make install`: Install the package and development dependencies
- `make format`: Format code with black and isort
- `make lint`: Run all linting checks (ruff, black, isort, mypy)
- `make test`: Run tests with pytest

## Project Structure

```
pydantic-agents/
├── src/
│   ├── __init__.py
│   ├── main.py
│   └── agents/
│       ├── __init__.py
│       └── bank_support.py
├── tests/
│   └── __init__.py
├── .env.example
├── .gitignore
├── LICENSE
├── Makefile
├── README.md
└── pyproject.toml
```

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
