"""
Source Hunter Agent

DONE: Implement this agent that searches the curated paper corpus
to find relevant passages for each sub-question in the query strategy.

Hints:
- This agent MUST use the search_papers tool from tools.paper_rag_tool
- Define a role focused on investigation and source discovery
- Set a goal to find 8-12 relevant passages
- Write a backstory emphasizing thoroughness and not stopping at first results
"""

from dotenv import load_dotenv
load_dotenv()

from crewai import Agent
from tools.paper_rag_tool import search_papers

# DONE: Create the source_hunter agent
source_hunter = Agent(
    role="Investigative Source Hunter",
    goal="Search through the 15 papers in the library to discover 8-12 highy relevant sections that provide the best evidence to address each quesiton and subquesiton.",
    backstory=(
        "You are a detailed source hunter with deep knowledge of the most well known AI papers (such as ReAct, "
        "Toolformer, AutoGen, Generative Agents, and Reflexion). You never settle for surface-level matches. "
        "Instead, you execute targeted queries using the search_papers tool for each sub question, inspect "
        "the retrieved passages, and extract concrete technical details, empirical findings, and paper citations."
    ),
    tools=[search_papers],  # This tool is required!
    verbose=True,
    memory=False,
)
