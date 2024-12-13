import re

def analyze_text(text: str) -> dict:
    """
    Analyze text for low-confidence patterns.
    """
    patterns = {
        "hedging": r"\b(just|maybe|perhaps|might|I think|I feel)\b",
        "apologizing": r"\b(sorry|apologize|I’m afraid|forgive me)\b",
        "minimizing": r"\b(only|merely|a little|somewhat|not much)\b",
        "passive_voice": r"\b(was|were|is|been|being)\b .* by\b",
    }

    # Initialize results
    analysis_results = {
        "hedging_count": 0,
        "apologizing_count": 0,
        "minimizing_count": 0,
        "passive_voice_count": 0,
        "total_issues": 0,
    }

    for cue, pattern in patterns.items():
        matches = re.findall(pattern, text, flags=re.IGNORECASE)
        count = len(matches)
        analysis_results[f"{cue}_count"] = count
        analysis_results["total_issues"] += count

    return analysis_results
