---

**Ticket Title:**  
Set Up PydanticAI with Demo Agent

---

**Description:**  
Implement the setup of PydanticAI within the `pydantic-agents` project by creating a demo agent. This setup will include integrating PydanticAI with Logfire for monitoring agent runs and providing example agents to demonstrate functionality.

---

**Tasks:**

1. **Install PydanticAI with Logfire Integration:**

   - Add `pydantic-ai` with the `logfire` optional group to the project dependencies.

   ```bash
   pip install 'pydantic-ai[logfire]'
   ```

2. **Configure Logfire:**

   - Follow the [Logfire setup documentation](#) to configure Logfire within the project.
   - Add Logfire configuration to the agent scripts as shown in the documentation.

   ```python
   import logfire

   logfire.configure()
   logfire.instrument_asyncpg()
   ```

3. **Create Demo Agent:**

   - Develop a minimal "Hello World" agent to verify the setup.

   **`src/main.py`**

   ```python
   from pydantic_ai import Agent

   agent = Agent(
       'gemini-1.5-flash',
       system_prompt='Be concise, reply with one sentence.',
   )

   result = agent.run_sync('Where does "hello world" come from?')
   print(result.data)
   ```

   **Expected Output:**

   ```
   The first known use of "hello, world" was in a 1974 textbook about the C programming language.
   ```

4. **Implement Support Agent Example:**

   - Create a support agent for a bank using PydanticAI with dependency injection and tools.

   **`src/agents/bank_support.py`**

   ```python
   from dataclasses import dataclass
   from pydantic import BaseModel, Field
   from pydantic_ai import Agent, RunContext
   from bank_database import DatabaseConn

   @dataclass
   class SupportDependencies:
       customer_id: int
       db: DatabaseConn

   class SupportResult(BaseModel):
       support_advice: str = Field(description='Advice returned to the customer')
       block_card: bool = Field(description="Whether to block the customer's card")
       risk: int = Field(description='Risk level of query', ge=0, le=10)

   support_agent = Agent(
       'openai:gpt-4o',
       deps_type=SupportDependencies,
       result_type=SupportResult,
       system_prompt=(
           'You are a support agent in our bank, give the '
           'customer support and judge the risk level of their query.'
       ),
   )

   @support_agent.system_prompt
   async def add_customer_name(ctx: RunContext[SupportDependencies]) -> str:
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

   async def main():
       deps = SupportDependencies(customer_id=123, db=DatabaseConn())
       result = await support_agent.run('What is my balance?', deps=deps)
       print(result.data)
       """
       support_advice='Hello John, your current account balance, including pending transactions, is $123.45.' block_card=False risk=1
       """

       result = await support_agent.run('I just lost my card!', deps=deps)
       print(result.data)
       """
       support_advice="I'm sorry to hear that, John. We are temporarily blocking your card to prevent unauthorized transactions." block_card=True risk=8
       """
   ```

5. **Integrate Logfire Instrumentation:**

   - Enhance the support agent with Logfire instrumentation to monitor agent runs.

   **`src/agents/bank_support_with_logfire.py`**

   ```python
   from bank_database import DatabaseConn
   import logfire

   logfire.configure()
   logfire.instrument_asyncpg()

   # Rest of the support agent code...
   ```

6. **Run and Verify Examples:**

   - Install example packages if not already included.

   ```bash
   pip install 'pydantic-ai[examples]'
   ```

   - Follow the [examples documentation](#) to run and verify the demo agents.

---

**Acceptance Criteria:**

- [ ] PydanticAI is installed with Logfire integration.
- [ ] Logfire is correctly configured and instrumented within the project.
- [ ] A minimal "Hello World" agent is operational and produces the expected output.
- [ ] A comprehensive support agent example is implemented, demonstrating dependency injection and tool usage.
- [ ] Logfire successfully monitors and logs the agent runs.
- [ ] Documentation is updated to reflect the setup process and usage of demo agents.

---

**Attachments:**

- **Folder Structure:**

  ```
  ◆ tree                                                                                   □ pydantic-agents △⹪●◦⤥ pkg ◨ 0.1.0 py ⌏⌚ 3.11.6 18:43
  .
  ├── .cursorrules
  ├── .env.example
  ├── .github
  │   └── workflows
  │       └── ci.yml
  ├── .gitignore
  ├── .vscode
  │   ├── extensions.json
  │   └── settings.json
  ├── LICENSE
  ├── Makefile
  ├── README.md
  ├── pyproject.toml
  ├── src
  │   ├── __init__.py
  │   ├── console.py
  │   └── main.py
  ├── tests
  │   ├── __init__.py
  │   └── test_console.py
  ├── tickets
  │   └── ticket-
  └── uv.lock

  7 directories, 17 files
  ```

- **Documentation References:**
  - [PydanticAI Documentation](#)
  - [Logfire Setup Documentation](#)
  - [PydanticAI Examples Documentation](#)

---

**Priority:** High  
**Assignee:** @cursor  
**Due Date:** 2024-12-28

---
