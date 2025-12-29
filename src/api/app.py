from flask import Flask, jsonify
from flask_cors import CORS
import os

from src.loader.git_loader import load_commits_from_file
from src.parser.commit_parser import parse_commits
from src.analyzer.narrative_analyzer import analyze_commits

app = Flask(__name__)
CORS(app)

@app.route("/analyze", methods=["GET"])
def analyze():
    file_path = os.path.join(
        os.path.dirname(__file__),
        "../../examples/sample_git_log.txt"
    )

    commit_lines = load_commits_from_file(file_path)
    commits = parse_commits(commit_lines)
    phases = analyze_commits(commits)

    return jsonify({
        "phases": phases
    })

@app.route("/")
def health():
    return {"status": "Git Story Generator API running"}

if __name__ == "__main__":
    app.run(host="127.0.0.1", port=5000, debug=True)

