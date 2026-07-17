from __future__ import annotations

def render_rfc(title: str, owner: str, problem: str, decision: str) -> str:
    if not all([title, owner, problem, decision]):
        raise ValueError("all fields are required")
    return f"# {title}\n\n**Owner:** {owner}\n\n## Problem\n\n{problem}\n\n## Decision\n\n{decision}\n"
