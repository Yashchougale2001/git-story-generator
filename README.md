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
