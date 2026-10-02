"""
Report Writer Agent

DONE: Implement this agent that produces a well-structured literature
review with proper citations.

Hints:
- Define a role focused on academic writing and communication
- Set a goal to produce a clear, well-organized literature review
- Write a backstory emphasizing clarity and proper attribution
- The output should be in markdown with sections:
  1. Executive Summary
  2. Introduction
  3. Methodology
  4. Findings (organized by theme)
  5. Discussion
  6. Conclusion
  7. References
"""

from dotenv import load_dotenv
load_dotenv()

from crewai import Agent

# DONE: Create the report_writer agent
# Create the report_writer agent
# Create the report_writer agent
report_writer = Agent(
    role="Lead Academic Technical Writer",
    goal="Author a comprehensive, well-structured, and rigorously cited literature review in Markdown format based on the synthesized research findings.",
    backstory=(
        "You are an accomplished scientific writer and editor for top-tier AI publications. You have a knack for "
        "transforming complex technical analyses into readable, polished, and authoritative literature reviews. You write "
        "with scholarly precision, properly attributing claims to specific papers (e.g., Wooldridge 1995, Yao et al. 2022, "
        "Park et al. 2023), and organize reports with clear academic structure."
    ),
    tools=[],
    verbose=True,
)
