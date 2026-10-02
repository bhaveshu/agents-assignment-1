"""
Query Expander Agent

DONE: Implement this agent that transforms a broad research question
into a comprehensive search strategy with sub-questions, keywords,
and search angles.

Hints:
- Define a clear role (e.g., "Research Query Strategist")
- Set a goal focused on breaking down questions and identifying keywords
- Write a backstory that gives the agent expertise in research methodology
- Consider what tools might help (keyword extraction, synonym generation)
"""

from dotenv import load_dotenv
load_dotenv()

from crewai import Agent

# DONE: Create the query_expander agent

query_expander = Agent(
    role="Research Query Strategist",
    goal="Understand the question being asked and deconsuruct it into structrued subquestions, technical keywords and different points of view for academic literature review",
    backstory=(
        "You are an expert academic research professor and strategist specializing in artificial "
        "intelligence and autonomous agents. Your expertise is in taking high-level, ambiguous questions "
        "and breaking them down into easy to understand concepts, architectural mechanisms, and domain-specific "
        "terminology. Your structured query plans ensure literature searches capture both theoretical foundations "
        "and cutting-edge implementations."
    ),
    tools=[],
    verbose=True,
    memory=False,
)
