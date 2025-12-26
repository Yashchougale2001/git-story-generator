SETUP_KEYWORDS = [
    "init", "initial", "setup", "structure", "skeleton",
    "template", "starter", "bootstrap", "scaffold", "readme"
]

FEATURE_KEYWORDS = [
    "add", "feature", "implement", "create", "build"
]

FIX_KEYWORDS = [
    "fix", "bug", "patch", "hotfix", "refactor", "cleanup"
]


def analyze_commits(commits):
    setup = feature = fix = 0

    for commit in commits:
        msg = commit.message.lower()

        if any(k in msg for k in SETUP_KEYWORDS):
            setup += 1
        elif any(k in msg for k in FEATURE_KEYWORDS):
            feature += 1
        elif any(k in msg for k in FIX_KEYWORDS):
            fix += 1

    phases = []

    if setup > 0:
        phases.append("Project setup & scaffolding phase")

    if feature > 0:
        phases.append("Feature expansion phase")

    if fix > 0:
        phases.append("Refactoring & stabilization phase")

    return phases
