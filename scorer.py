"""
Approximate scoring based on published X algorithm weights.
Weights are examples synced from public param.rs discussions; update as needed.
"""

# Approximate positive weights (from public sources / previous analysis)
WEIGHTS = {
    "reply": 5.0,
    "share": 2.0,
    "share_dm": 5.0,
    "quote": 5.0,
    "follow": 4.0,
    "like": 0.66,
    "repost": 1.0,
    "dwell": 0.05,
    "bookmark": 3.0,  # estimated high value
}

# Strong negatives
NEGATIVE_WEIGHTS = {
    "mute": -58.8,
    "block": -31.2,
    "report": -234.0,
    "not_interested": -52.0,
}

def score_post(text: str, estimated_actions: dict = None) -> dict:
    """
    Simple heuristic scorer.
    In a real app this would call a model predicting P(action).
    Here we use length, question marks, and user-provided estimates.
    """
    if estimated_actions is None:
        estimated_actions = {}

    # Heuristics
    has_question = "?" in text
    word_count = len(text.split())
    estimated_reply_p = 0.15 if has_question else 0.05
    estimated_dwell_p = min(0.4, word_count / 100)

    base_score = (
        WEIGHTS["reply"] * estimated_actions.get("reply_p", estimated_reply_p)
        + WEIGHTS["share"] * estimated_actions.get("share_p", 0.02)
        + WEIGHTS["dwell"] * estimated_actions.get("dwell_p", estimated_dwell_p)
        + WEIGHTS["like"] * estimated_actions.get("like_p", 0.1)
    )

    return {
        "score": round(base_score, 2),
        "breakdown": {
            "reply_contribution": round(WEIGHTS["reply"] * estimated_actions.get("reply_p", estimated_reply_p), 2),
            "dwell_contribution": round(WEIGHTS["dwell"] * estimated_actions.get("dwell_p", estimated_dwell_p), 2),
            "has_question": has_question,
            "word_count": word_count,
        },
        "tips": [
            "End with a clear question to boost reply probability." if not has_question else "Good question hook.",
            "Keep main post self-contained so readers stay on X.",
            "Avoid content that triggers mutes or reports.",
        ]
    }
