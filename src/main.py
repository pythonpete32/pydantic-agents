"""Demo agent using PydanticAI."""

import logfire
from pydantic_ai import Agent

# Configure Logfire for monitoring
logfire.configure()

# Initialize the demo agent
agent = Agent(
    "gemini-1.5-flash",
    system_prompt="Be concise, reply with one sentence.",
)


def main() -> None:
    """Run the demo agent."""
    result = agent.run_sync("Where does 'hello world' come from?")
    print(result.data)


if __name__ == "__main__":
    main()
