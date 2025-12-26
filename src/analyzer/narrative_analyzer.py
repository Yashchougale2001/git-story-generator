def analyze_commits(commits):
    """
    Dummy analyzer: returns simple phases based on commit messages.
    Replace with actual NLP/heuristics later.
    """
    phases = []
    for commit in commits:
        msg = commit.message.lower()
        if "fix" in msg or "refactor" in msg:
            phases.append("Refactoring phase detected")
        elif "feature" in msg or "add" in msg:
            phases.append("Feature creep detected")
        else:
            phases.append("Initial chaos phase")
    return phases
