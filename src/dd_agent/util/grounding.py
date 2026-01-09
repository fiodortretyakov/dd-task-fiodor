"""Utilities for grounding natural language to question/option IDs."""

from typing import Optional

from dd_agent.contracts.questions import Question
from dd_agent.util.interaction import resolve_ambiguity


def find_matching_questions(
    search_term: str,
    questions: list[Question],
    interactive: bool = True,
) -> Optional[Question]:
    """
    Find a question matching a search term.

    Args:
        search_term: Natural language term (e.g., "Geography", "country")
        questions: List of available questions
        interactive: If True, ask user to choose when ambiguous

    Returns:
        Matching Question, or None if not found or user declined

    Raises:
        AmbiguityError: If ambiguous and interactive=False
    """
    search_lower = search_term.lower().strip()

    # Exact ID match (highest priority)
    candidates_exact = [q for q in questions if q.question_id.lower() == search_lower]
    if candidates_exact:
        return candidates_exact[0]

    # Label prefix match
    candidates_prefix = [q for q in questions if q.label.lower().startswith(search_lower)]

    # Label contains match
    candidates_contains = [q for q in questions if search_lower in q.label.lower()]

    # Combine with priority
    candidates = candidates_prefix or candidates_contains
    if not candidates:
        return None

    # Single match
    if len(candidates) == 1:
        return candidates[0]

    # Multiple matches - need disambiguation
    candidate_dicts = [{"id": q.question_id, "label": q.label, "obj": q} for q in candidates]

    selected = resolve_ambiguity(
        candidates=candidate_dicts,
        field_name="Question",
        user_context=search_term,
        interactive=interactive,
    )

    return selected["obj"] if selected else None


def find_matching_option(
    question: Question,
    search_term: str,
    interactive: bool = True,
) -> Optional[str | int]:
    """
    Find an option code matching a search term within a question.

    Args:
        question: The question to search within
        search_term: Natural language term (e.g., "High Income")
        interactive: If True, ask user to choose when ambiguous

    Returns:
        Option code (str or int), or None if not found or user declined

    Raises:
        AmbiguityError: If ambiguous and interactive=False
    """
    if not question.options:
        return None

    search_lower = search_term.lower().strip()

    # Exact code match (convert to string for comparison)
    candidates_code = [o for o in question.options if str(o.code).lower() == search_lower]
    if candidates_code:
        return candidates_code[0].code

    # Label exact match
    candidates_label = [o for o in question.options if o.label.lower() == search_lower]
    if candidates_label:
        return candidates_label[0].code

    # Label contains match
    candidates_contains = [o for o in question.options if search_lower in o.label.lower()]

    if not candidates_contains:
        return None

    # Single match
    if len(candidates_contains) == 1:
        return candidates_contains[0].code

    # Multiple matches
    candidate_dicts = [
        {"id": str(o.code), "label": o.label, "obj": o.code} for o in candidates_contains
    ]

    selected = resolve_ambiguity(
        candidates=candidate_dicts,
        field_name="Option",
        user_context=search_term,
        interactive=interactive,
    )

    return selected["obj"] if selected else None
