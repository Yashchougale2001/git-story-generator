def load_commits_from_file(file_path):
    """
    Load commit history from a text file.
    Returns a list of commit lines.
    """
    with open(file_path, "r", encoding="utf-8") as f:
        commits = f.readlines()
    return [line.strip() for line in commits if line.strip()]
