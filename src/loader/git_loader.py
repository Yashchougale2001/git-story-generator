import chardet

def load_commits_from_file(file_path):
    """
    Load commit history from a text file with proper encoding detection.
    Returns a list of commit lines.
    """
    # Detect encoding first
    with open(file_path, "rb") as f:
        raw_data = f.read()
        result = chardet.detect(raw_data)
        encoding = result['encoding']
    
    # Open file using detected encoding
    with open(file_path, "r", encoding=encoding) as f:
        commits = f.readlines()
    
    return [line.strip() for line in commits if line.strip()]
