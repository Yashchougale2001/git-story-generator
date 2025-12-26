from dataclasses import dataclass
import re

@dataclass
class Commit:
    date: str
    author: str
    message: str

def parse_commits(commit_lines):
    """
    Very simple parser: expects format "date | author | message"
    Example line: "2025-12-26 | Yash | Initial commit"
    """
    commits = []
    for line in commit_lines:
        parts = line.split("|")
        if len(parts) == 3:
            date, author, message = [p.strip() for p in parts]
            commits.append(Commit(date, author, message))
    return commits
