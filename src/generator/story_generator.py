def generate_story(phases):
    """
    Converts phases into readable timeline story.
    """
    story = "Project Story Timeline:\n"
    for i, phase in enumerate(phases, 1):
        story += f"{i}. {phase}\n"
    return story
