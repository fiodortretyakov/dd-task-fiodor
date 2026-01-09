"""Interactive CLI utilities for ambiguity resolution and user guidance."""

from typing import Optional

import typer
from rich.console import Console
from rich.panel import Panel
from rich.table import Table

console = Console()


class AmbiguityError(Exception):
    """Raised when ambiguity cannot be resolved interactively."""

    def __init__(self, message: str, candidates: list[str]):
        super().__init__(message)
        self.candidates = candidates


def resolve_ambiguity(
    candidates: list[dict],
    field_name: str,
    user_context: str = "",
    interactive: bool = True,
) -> Optional[dict]:
    """
    Interactively resolve ambiguity by asking user to choose from candidates.

    Args:
        candidates: List of candidate dicts with at least 'id' and 'label' keys
        field_name: Name of the field being resolved (e.g., "Question", "Option")
        user_context: Context about what the user asked (e.g., "Geography")
        interactive: If True, prompt user; if False, raise error

    Returns:
        Selected candidate dict, or None if user declines

    Raises:
        AmbiguityError: If interactive=False and len(candidates) > 1
    """
    if len(candidates) == 0:
        return None

    if len(candidates) == 1:
        return candidates[0]

    # Multiple candidates - need to ask user
    if not interactive:
        candidate_ids = [c.get("id", str(c)) for c in candidates]
        raise AmbiguityError(
            f"Ambiguous {field_name} '{user_context}': multiple matches found",
            candidate_ids,
        )

    # Show options
    console.print(
        Panel(
            f"[yellow]⚠️  Ambiguity detected[/yellow]\n\n"
            f"Your mention of '[bold]{user_context}[/bold]' matches multiple {field_name}s.",
            title="Clarification needed",
            border_style="yellow",
        )
    )

    table = Table(title=f"Available {field_name}s")
    table.add_column("Choice", style="cyan")
    table.add_column("ID", style="magenta")
    table.add_column("Label")

    for i, candidate in enumerate(candidates, start=1):
        cand_id = candidate.get("id", "?")
        cand_label = candidate.get("label", candidate.get("name", str(candidate)))
        table.add_row(str(i), cand_id, cand_label)

    console.print(table)

    while True:
        try:
            choice = typer.prompt(
                f"\nEnter choice (1-{len(candidates)}) or 'skip' to cancel",
                type=str,
            )

            if choice.lower() in ("skip", "q", "cancel"):
                console.print("[yellow]Cancelled by user[/yellow]")
                return None

            idx = int(choice) - 1
            if 0 <= idx < len(candidates):
                selected = candidates[idx]
                console.print(
                    f"[green]✓ Selected: {selected.get('label', selected.get('id'))}[/green]"
                )
                return selected

            console.print(f"[red]Invalid choice. Please enter 1-{len(candidates)}[/red]")

        except ValueError:
            console.print("[red]Invalid input. Please enter a number.[/red]")


def prompt_for_filter_confirmation(
    filter_spec: str,
    matches: int,
) -> bool:
    """
    Ask user to confirm a filter specification before applying.

    Args:
        filter_spec: Human-readable filter specification
        matches: Number of responses matching the filter

    Returns:
        True if user confirms, False otherwise
    """
    console.print(
        Panel(
            f"Filter: [bold]{filter_spec}[/bold]\n" f"Matches: [cyan]{matches}[/cyan] responses",
            title="Confirm filter",
            border_style="blue",
        )
    )

    confirm = typer.confirm("Apply this filter?", default=True)
    return confirm


def prompt_for_metric_confirmation(
    metric: str,
    question: str,
) -> bool:
    """
    Ask user to confirm a metric choice for a question.

    Args:
        metric: Metric name (e.g., "nps", "top2box")
        question: Question label

    Returns:
        True if user confirms, False otherwise
    """
    console.print(
        Panel(
            f"Metric: [bold cyan]{metric}[/bold cyan]\n" f"Question: [bold]{question}[/bold]",
            title="Confirm metric",
            border_style="blue",
        )
    )

    confirm = typer.confirm("Use this metric?", default=True)
    return confirm


def show_guidance():
    """Display guidance on valid analysis requests."""
    console.print(
        Panel(
            "[bold]Valid analysis requests:[/bold]\n\n"
            "• [cyan]Show NPS by country[/cyan] - metric by dimension\n"
            "• [cyan]Create Enterprise segment (org size >= 1000)[/cyan] - define segment\n"
            "• [cyan]Top-2-box satisfaction by industry[/cyan] - different metric\n"
            "• [cyan]Compare NPS for Enterprise vs others[/cyan] - segment comparison\n\n"
            "[bold]Available metrics:[/bold] nps, top2box (for Likert questions), count\n"
            "[bold]Dimensions:[/bold] Any question from the catalog\n"
            "[bold]Segments:[/bold] Boolean filters over numeric/option questions",
            title="📊 Analysis Guidance",
            border_style="green",
        )
    )


def handle_off_scope_input(user_input: str) -> bool:
    """
    Detect and handle off-scope inputs (greetings, help, etc.).

    Args:
        user_input: User's input string

    Returns:
        True if input was off-scope and handled, False if it's an analysis request
    """
    lower_input = user_input.lower().strip()

    # Greetings
    if lower_input in ("hello", "hi", "hey", "greetings"):
        console.print("[green]👋 Hello! I'm a DD survey analytics agent.[/green]")
        show_guidance()
        return True

    # Help requests
    if lower_input in ("help", "?", "how do i use this", "what can you do"):
        show_guidance()
        return True

    # "What can you analyze" variants
    if any(
        phrase in lower_input
        for phrase in ("what can", "what questions", "what metrics", "available")
    ):
        show_guidance()
        return True

    return False
