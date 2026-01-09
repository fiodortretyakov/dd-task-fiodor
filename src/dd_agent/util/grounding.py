"""Utilities for grounding natural language to question/option IDs."""

from difflib import SequenceMatcher, get_close_matches
from typing import Optional, TypeVar

from dd_agent.contracts.questions import Question
from dd_agent.util.interaction import resolve_ambiguity

T = TypeVar("T")


def _similarity_ratio(a: str, b: str) -> float:
    """Calculate similarity ratio between two strings (0.0 to 1.0)."""
    return SequenceMatcher(None, a.lower(), b.lower()).ratio()


def _find_close_matches(
    search_term: str,
    candidates: list[tuple[str, T]],
    threshold: float = 0.6,
) -> list[tuple[float, str, T]]:
    """
    Find close matches using fuzzy matching with multiple strategies.

    Args:
        search_term: The search term
        candidates: List of (label, object) tuples to search
        threshold: Minimum similarity ratio (0.0-1.0)

    Returns:
        List of (similarity_ratio, label, object) sorted by similarity descending
    """
    results = []
    search_lower = search_term.lower().strip()

    # Strategy 1: Direct similarity ratio
    for label, obj in candidates:
        ratio = _similarity_ratio(search_lower, label)
        if ratio >= threshold:
            results.append((ratio, label, obj))

    # Strategy 2: If no direct matches and threshold is high, try difflib's get_close_matches
    if not results and threshold > 0.5:
        candidate_labels = [label for label, _ in candidates]
        close = get_close_matches(search_lower, candidate_labels, n=3, cutoff=0.5)

        for close_label in close:
            for label, obj in candidates:
                if label == close_label:
                    ratio = _similarity_ratio(search_lower, label)
                    results.append((ratio, label, obj))
                    break

    # Sort by similarity ratio descending
    return sorted(results, key=lambda x: x[0], reverse=True)


def find_matching_questions(
    search_term: str,
    questions: list[Question],
    interactive: bool = True,
) -> Optional[Question]:
    """
    Find a question matching a search term with improved grounding.

    Uses multi-stage matching:
    1. Exact ID match (highest priority)
    2. Exact label match
    3. Label prefix match
    4. Fuzzy matching on label
    5. Fuzzy matching on question text

    Args:
        search_term: Natural language term (e.g., "Geography", "country")
        questions: List of available questions
        interactive: If True, ask user to choose when ambiguous

    Returns:
        Matching Question, or None if not found or user declined

    Raises:
        AmbiguityError: If ambiguous and interactive=False
    """
    if not search_term or not search_term.strip():
        return None

    search_lower = search_term.lower().strip()

    # Stage 1: Exact ID match (highest priority)
    candidates_exact_id = [q for q in questions if q.question_id.lower() == search_lower]
    if candidates_exact_id:
        return candidates_exact_id[0]

    # Stage 2: Exact label match
    candidates_exact_label = [q for q in questions if q.label.lower() == search_lower]
    if candidates_exact_label:
        return candidates_exact_label[0]

    # Stage 3: Label prefix match
    candidates_prefix = [q for q in questions if q.label.lower().startswith(search_lower)]
    if candidates_prefix:
        if len(candidates_prefix) == 1:
            return candidates_prefix[0]
        # Multiple prefix matches - escalate to disambiguation

    # Stage 4: Label contains match (substring)
    candidates_contains = [q for q in questions if search_lower in q.label.lower()]

    # Stage 5: Fuzzy matching on labels
    all_questions_for_fuzzy = [
        (q.label, q) for q in questions if q not in candidates_prefix + candidates_contains
    ]
    fuzzy_matches = _find_close_matches(search_term, all_questions_for_fuzzy, threshold=0.55)

    # Combine candidates with priority
    candidates = candidates_prefix
    if not candidates:
        candidates = candidates_contains
    if not candidates and fuzzy_matches:
        candidates = [obj for _, _, obj in fuzzy_matches]

    if not candidates:
        return None

    # Single match
    if len(candidates) == 1:
        return candidates[0]

    # Multiple matches - need disambiguation with detailed context
    candidate_dicts = []
    for q in candidates:
        candidate_dicts.append(
            {
                "id": q.question_id,
                "label": q.label,
                "obj": q,
            }
        )

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

    Uses multi-stage matching:
    1. Exact code match
    2. Exact label match
    3. Label prefix match
    4. Fuzzy matching on label

    Args:
        question: The question to search within
        search_term: Natural language term (e.g., "High Income")
        interactive: If True, ask user to choose when ambiguous

    Returns:
        Option code (str or int), or None if not found or user declined

    Raises:
        AmbiguityError: If ambiguous and interactive=False
    """
    if not question.options or not search_term or not search_term.strip():
        return None

    search_lower = search_term.lower().strip()

    # Stage 1: Exact code match (convert to string for comparison)
    candidates_code = [o for o in question.options if str(o.code).lower() == search_lower]
    if candidates_code:
        return candidates_code[0].code

    # Stage 2: Exact label match
    candidates_exact = [o for o in question.options if o.label.lower() == search_lower]
    if candidates_exact:
        return candidates_exact[0].code

    # Stage 3: Label prefix match
    candidates_prefix = [o for o in question.options if o.label.lower().startswith(search_lower)]

    # Stage 4: Label contains match (substring)
    candidates_contains = [o for o in question.options if search_lower in o.label.lower()]

    # Stage 5: Fuzzy matching on labels
    all_options_for_fuzzy = [
        (o.label, o) for o in question.options if o not in candidates_prefix + candidates_contains
    ]
    fuzzy_matches = _find_close_matches(search_term, all_options_for_fuzzy, threshold=0.55)

    # Combine candidates with priority
    candidates = candidates_prefix
    if not candidates:
        candidates = candidates_contains
    if not candidates and fuzzy_matches:
        candidates = [obj for _, _, obj in fuzzy_matches]

    if not candidates:
        return None

    # Single match
    if len(candidates) == 1:
        return candidates[0].code

    # Multiple matches - need disambiguation
    candidate_dicts = [
        {"id": str(o.code), "label": o.label, "obj": o.code} for o in candidates
    ]

    selected = resolve_ambiguity(
        candidates=candidate_dicts,
        field_name="Option",
        user_context=search_term,
        interactive=interactive,
    )

    return selected["obj"] if selected else None


def ground_questions_with_diagnostics(
    search_terms: list[str],
    questions: list[Question],
) -> dict:
    """
    Ground multiple search terms and provide detailed diagnostics.

    Args:
        search_terms: List of search terms to ground
        questions: List of available questions

    Returns:
        Dict with grounding results and diagnostics
    """
    results = {}

    for term in search_terms:
        match = find_matching_questions(term, questions, interactive=False)

        diagnostics = {
            "term": term,
            "found": match is not None,
            "question_id": match.question_id if match else None,
            "label": match.label if match else None,
            "confidence": "high" if match else "none",
        }

        # If not found, provide diagnostic info
        if not match:
            # Look for similar questions
            all_labels = [(q.label, q) for q in questions]
            similar = _find_close_matches(term, all_labels, threshold=0.5)
            if similar:
                diagnostics["similar_questions"] = [
                    {"id": obj.question_id, "label": obj.label, "similarity": round(sim, 2)}
                    for sim, _, obj in similar[:3]
                ]

        results[term] = diagnostics

    return results


def ground_option_with_diagnostics(
    search_term: str,
    question: Question,
) -> dict:
    """
    Ground a single option search term with detailed diagnostics.

    Args:
        search_term: The search term for the option
        question: The question to search within

    Returns:
        Dict with grounding result and diagnostics
    """
    if not question.options:
        return {
            "term": search_term,
            "question_id": question.question_id,
            "found": False,
            "error": "Question has no options",
        }

    match = find_matching_option(question, search_term, interactive=False)

    diagnostics = {
        "term": search_term,
        "question_id": question.question_id,
        "found": match is not None,
        "option_code": match if match else None,
        "confidence": "high" if match else "none",
    }

    # If not found, provide diagnostic info
    if not match:
        # Look for similar options
        all_labels = [(o.label, o) for o in question.options]
        similar = _find_close_matches(search_term, all_labels, threshold=0.5)
        if similar:
            diagnostics["similar_options"] = [
                {"code": obj.code, "label": obj.label, "similarity": round(sim, 2)}
                for sim, _, obj in similar[:3]
            ]

    return diagnostics
