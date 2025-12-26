# Git Commit → Project Story Generator

This project analyzes your Git commit history and generates a **narrative timeline**, highlighting phases like:

- Initial chaos phase
- Refactoring phase
- Feature creep detected
- Over-engineering or rushed commits

> “This tells the story your commits accidentally reveal.”

---

## **Features**

- Input: Git commit history (file or pasted text)
- Output: Timeline story of your project
- Detects patterns such as:
  - Chaos (lots of rushed commits)
  - Refactoring
  - Feature creep
  - Late testing or over-engineering
- Simple frontend to visualize the story (optional)

---

## **Tech Stack**

- Python (backend)
- NLP (nltk, spaCy)
- Optional LLMs (OpenAI API)
- Frontend: HTML, CSS, JavaScript (or Flask)

---

## **Project Structure**

git-story-generator/
│
├─ src/                          # Core backend logic
│   ├─ loader/                   # Handles input commits
│   │   └─ git_loader.py         # Load commit history from file or git log
│   │
│   ├─ parser/                   # Parse commits into structured data
│   │   └─ commit_parser.py      # Extract date, author, message; store as dict/dataclass
│   │
│   ├─ analyzer/                 # Analyze commit patterns and detect phases
│   │   └─ narrative_analyzer.py # Identify chaos, refactoring, feature creep, rushed commits, over-engineering
│   │
│   ├─ generator/                # Generate human-readable story
│   │   └─ story_generator.py    # Convert analysis into timeline story
│   │
│   ├─ utils/                    # Helper functions
│   │   └─ helpers.py            # Date parsing, text cleaning, common utilities
│   │
│   └─ main.py                   # Orchestrates loading → parsing → analysis → story generation
│
├─ frontend/                      # Optional: simple UI to interact with backend
│   ├─ index.html                 # UI with textarea to paste commit history
│   ├─ style.css                  # Styling for timeline story
│   └─ app.js                     # JS to send commit history to backend and display result
│
├─ tests/                         # Unit tests
│   ├─ test_parser.py
│   ├─ test_analyzer.py
│   └─ test_generator.py
│
├─ examples/                      # Example git logs to demo functionality
│   └─ sample_git_log.txt
│
├─ requirements.txt               # Python dependencies (pandas, nltk, openai, etc.)
├─ README.md                      # Project explanation, how to run, demo screenshots
└─ .gitignore                     # Ignore venv, __pycache__, node_modules, etc.

## **How to Run**

1. Clone the repository:
```bash
git clone <repo-url>
cd git-story-generator
Install dependencies:

bash
Copy code
pip install -r requirements.txt
Run the main pipeline:

bash
Copy code
python src/main.py
Output will show a readable timeline story.

