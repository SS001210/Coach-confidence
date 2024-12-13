def generate_suggestions(analysis_results: dict) -> dict:
    """
    Generate suggestions for improving text confidence.
    """
    suggestions = []

    if analysis_results["hedging_count"] > 0:
        suggestions.append("Avoid hedging phrases like 'just', 'maybe', or 'I think'. Use more direct statements.")

    if analysis_results["apologizing_count"] > 0:
        suggestions.append("Limit unnecessary apologies. Rephrase to sound more confident and assertive.")

    if analysis_results["minimizing_count"] > 0:
        suggestions.append("Avoid minimizing language like 'only' or 'somewhat'. Be more assertive in your communication.")

    if analysis_results["passive_voice_count"] > 0:
        suggestions.append("Minimize the use of passive voice. Prefer active voice for clearer and more assertive communication.")

    if analysis_results["excessive_qualification_count"] > 0:
        suggestions.append("Limit excessive qualifications like 'I’m not sure' or 'I think'. Express your thoughts more decisively.")

    if analysis_results["evasive_language_count"] > 0:
        suggestions.append("Avoid evasive language like 'I don’t know' or 'I could be wrong'. Be more confident in your statements.")

    if analysis_results["understatements_count"] > 0:
        suggestions.append("Avoid understatements like 'not bad' or 'could be worse'. Express your ideas more positively.")

    if analysis_results["disclaimers_count"] > 0:
        suggestions.append("Limit disclaimers like 'Just my opinion' or 'I’m no expert'. Take more ownership of your statements.")

    if analysis_results["non_committal_count"] > 0:
        suggestions.append("Avoid non-committal phrases like 'kind of' or 'sort of'. Be more assertive and clear in your communication.")

    if analysis_results["overuse_of_idk_count"] > 0:
        suggestions.append("Minimize overuse of 'I don’t know'. When uncertain, try to express what you do know or ask for clarification.")

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
