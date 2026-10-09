"""
Task Definitions for Research Crew

DONE: Define the four sequential tasks:
1. Query Expansion - Break down the research question
2. Source Hunting - Search the paper corpus
3. Synthesis - Analyze and synthesize findings
4. Report Writing - Generate the literature review

Each task should:
- Have a clear description telling the agent what to do
- Specify the agent responsible
- Define expected_output format
- Use context parameter to pass information between tasks
"""

from crewai import Task
from agents import query_expander, source_hunter, synthesizer, report_writer


def create_research_tasks(research_question: str) -> list[Task]:
    """
    Create the task pipeline for a research question.

    Args:
        research_question: The user's research question

    Returns:
        List of 4 tasks in execution order

    DONE: Implement the four tasks below
    """

    # =========================================
    # Task 1: Query Expansion
    # =========================================
    # DONE: Create a task that breaks down the research question
    # into sub-questions, keywords, and search angles
    #
    expand_task = Task(
        description=(
            f"Analyze the research question: '{research_question}'.\n"
            "1. Deconstruct it into 3-5 specific sub-questions covering theoretical foundations,\n"
            "architectural patterns, and practical mechanisms. "
            "2. Identify primary technical keywords, synonyms, and related academic terms.\n"
            "3. Create 4-6 targeted search queries optimized for finding relevant passages in\n"
            "our AI agent research paper archive."
        ),
        agent=query_expander,
        expected_output="A structured search strategy with numbered sub-questions, prioritized keywords,and 4-6 precise search query strings."
    )

    # =========================================
    # Task 2: Source Hunting
    # =========================================
    # DONE: Create a task that searches the paper corpus
    # Hint: Use context=[expand_task] to pass the query strategy
    #
    search_task = Task(
        description=(
            "Execute the search strategy created in the previous task. "
            "1. Use the `search_papers` tool to search the 15-paper corpus using the suggested queries. "
            "2. Query for each sub-question and inspect retrieved passages. "
            "3. Collect 8-12 high-relevance, evidence-rich excerpts across different papers. "
            "4. For each excerpt, note the paper ID, exact title, author names, publication year, section, and key technical takeaways."
        ),
        agent=source_hunter,
        context=[expand_task],
        expected_output="A curated catalog of 8-12 relevant paper excerpts with citations (paper ID, title, authors, year, section) and concise summaries of empirical evidence and metrics.",
    )

    # =========================================
    # Task 3: Synthesis
    # =========================================
    # DONE: Create a task that synthesizes findings into themes
    # Hint: Use context=[expand_task, search_task] for full context
    #
    synthesis_task = Task(
        description=(
            f"Synthesize the findings collected by the literature scout to address: '{research_question}'.\n"
            "1. Group evidence into 3-4 overarching themes or architectural paradigms.\n"
            "2. Compare and contrast differing approaches, trade-offs, and design choices across papers.\n"
            "3. Identify areas of strong consensus in the literature versus open debates.\n"
            "4. Highlight critical gaps, limitations, or future directions mentioned in the sources."
        ),
        agent=synthesizer,
        context=[expand_task, search_task],
        expected_output="A structured thematic synthesis report containing major themes, comparative analysis of approaches, consensus vs debate points, and identified research gaps with citations."
    )

    # =========================================
    # Task 4: Report Writing
    # =========================================
    # DONE: Create a task that writes the final literature review
    # Hint: Use context=[expand_task, search_task, synthesis_task]
    #
    report_task = Task(
        description=(
            f"Author a comprehensive, publication-quality academic literature review on: '{research_question}'.\n"
            "Using the synthesized evidence, write a complete report formatted in clean Markdown with the following sections:\n"
            "# Literature Review: [Title reflecting the research question]\n"
            "## 1. Executive Summary\n"
            "## 2. Introduction & Research Question\n"
            "## 3. Methodology & Corpus Overview\n"
            "## 4. Key Themes & Findings (detailed thematic analysis with in-text citations like 'Yao et al., 2022')\n"
            "## 5. Discussion & Architectural Trade-offs\n"
            "## 6. Open Challenges & Future Directions\n"
            "## 7. Conclusion\n"
            "## 8. References (list all cited papers from the corpus)\n"
            "CRITICAL CITATION AND GROUNDING RULES:\n"
            "- For in-text citations and Section 8 (References), use ONLY the exact author names and publication years provided in the retrieved paper sources. Do NOT invent, hallucinate, or fabricate authors or co-authors. If author names are missing, cite by exact paper title.\n"
            "- Verify all quantitative benchmark numbers and metrics directly against the excerpts (e.g. exact ALFWorld or HotpotQA accuracy figures).\n"
            "Ensure rigorous academic tone and proper attribution throughout."
        ),
        agent=report_writer,
        context=[expand_task, search_task, synthesis_task],
        expected_output="A complete, polished academic literature review in Markdown format featuring all 8 requested sections with substantive content, verified empirical metrics, and rigorous citations matching the paper corpuus."
    )

    # DONE: Return your tasks in order
    return [expand_task, search_task, synthesis_task, report_task]
