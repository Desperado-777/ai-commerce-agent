from pathlib import Path


def load_prompt(filename):

    prompt_path = (
        Path(__file__)
        .parent
        / filename
    )

    return prompt_path.read_text()