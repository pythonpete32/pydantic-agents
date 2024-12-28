"""Bank support agent using PydanticAI."""

from dataclasses import dataclass

from pydantic import BaseModel, Field
from pydantic_ai import Agent, RunContext


class DatabaseConn:
    """Mock database connection class."""

    async def customer_name(self, id: int) -> str:
        """Get customer name by ID."""
        return "John Doe"  # Mock implementation

    async def customer_balance(self, id: int, include_pending: bool = False) -> float:
        """Get customer balance by ID."""
        return 123.45  # Mock implementation


@dataclass
class SupportDependencies:
    """Dependencies for the support agent."""

    customer_id: int
    db: DatabaseConn


class SupportResult(BaseModel):
    """Result model for support agent responses."""

    support_advice: str = Field(description="Advice returned to the customer")
    block_card: bool = Field(description="Whether to block the customer's card")
    risk: int = Field(description="Risk level of query", ge=0, le=10)


support_agent = Agent(
    "openai:gpt-4",
    deps_type=SupportDependencies,
    result_type=SupportResult,
    system_prompt=(
        "You are a support agent in our bank, give the "
        "customer support and judge the risk level of their query."
    ),
)


@support_agent.system_prompt
async def add_customer_name(ctx: RunContext[SupportDependencies]) -> str:
    """Add customer name to system prompt."""
    customer_name = await ctx.deps.db.customer_name(id=ctx.deps.customer_id)
    return f"The customer's name is {customer_name!r}"


@support_agent.tool
async def customer_balance(
    ctx: RunContext[SupportDependencies], include_pending: bool
) -> float:
    """Returns the customer's current account balance."""
    return await ctx.deps.db.customer_balance(
        id=ctx.deps.customer_id,
        include_pending=include_pending,
    )


async def main() -> None:
    """Run example support agent interactions."""
    deps = SupportDependencies(customer_id=123, db=DatabaseConn())

    # Check balance query
    result = await support_agent.run("What is my balance?", deps=deps)
    print("Balance query:", result.data)

    # Lost card query
    result = await support_agent.run("I just lost my card!", deps=deps)
    print("Lost card query:", result.data)


if __name__ == "__main__":
    import asyncio

    asyncio.run(main())
