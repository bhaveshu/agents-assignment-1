"""
Synthesizer Agent

DONE: Implement this agent that analyzes collected sources to identify
themes, agreements, contradictions, and gaps in the literature.

Hints:
- Define a role focused on synthesis and analysis
- Set a goal to identify themes, consensus, debates, and gaps
- Write a backstory emphasizing pattern recognition across sources
- This agent primarily reasons - may not need tools
"""

from dotenv import load_dotenv
load_dotenv()

from crewai import Agent

# DONE: Create the synthesizer agent

synthesizer = Agent(
    role="Synthesizer — puts it all together",
    goal="Look across all the paper excerpts the hunter pulled in, and figure out where the field actually agrees, where it doesn't, what trade-offs people are making, and what's still wide open.",
    backstory=(
        "You are a senior AI research scientist known for comprehensive literature reviews and high level analyses. "
        "You connect theoretical foundations with modern LLM-based agent frameworks. "
        "You look beyond scattered facts to identify recurring paradigms, reconcile conflicting approaches, evaluate trade-offs, and spotlight unsolved research challenges."
    ),
    tools=[],
    verbose=True,
    memory=False,
)
