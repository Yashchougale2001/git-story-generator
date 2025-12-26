from loader.git_loader import load_commits_from_file
from parser.commit_parser import parse_commits
from analyzer.narrative_analyzer import analyze_commits
from generator.story_generator import generate_story

def main():
    # file_path = "examples/sample_git_log.txt"  # Example input file
    file_path = "examples/my_commits.txt"  # My Own GIT commit input file
    commit_lines = load_commits_from_file(file_path)
    commits = parse_commits(commit_lines)
    phases = analyze_commits(commits)
    story = generate_story(phases)
    print(story)

if __name__ == "__main__":
    main()
