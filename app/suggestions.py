def generate_suggestions(analysis_results: dict) -> dict:
    """
    Generate suggestions for improving text confidence.
    """
    suggestions = []

    if analysis_results["hedging_count"] > 0:
        suggestions.append("Avoid hedging phrases like 'just', 'maybe', or 'I think'. Use more direct statements.")

    if analysis_results["apologizing_count"] > 0:
        suggestions.append("Limit unnecessary apologies. Rephrase to sound confident.")

    if analysis_results["minimizing_count"] > 0:
        suggestions.append("Avoid minimizing language like 'only' or 'somewhat'. Be assertive.")

    if analysis_results["passive_voice_count"] > 0:
        suggestions.append("Minimize passive voice. Use active voice for clearer communication.")

    total_issues = analysis_results["total_issues"]

    # Assign confidence rating based on total issues
    if total_issues == 0:
        confidence_rating = "Excellent! Your communication shows strong confidence."
        confidence_score = 10
    elif 0 < total_issues <= 2:
        confidence_rating = "Good, but some areas could be more assertive."
        confidence_score = 8
    elif 2 < total_issues <= 4:
        confidence_rating = "Fair. Consider revising key areas for better clarity and assertiveness."
        confidence_score = 6
    elif 4 < total_issues <= 6:
        confidence_rating = "Needs improvement. Focus on reducing low-confidence cues."
        confidence_score = 4
    else:
        confidence_rating = "Significant improvement needed. Rework key phrases to appear more confident."
        confidence_score = 2

    return {
        "suggestions": suggestions,
        "confidence_rating": confidence_rating,
        "confidence_score": confidence_score,
    }
