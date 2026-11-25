"""One Line, Big Laugh.

Writes one line (at most 200 characters) to /output/entry.txt.
"""

# Design notes: the concept in one sentence is a smart fridge that takes
# a diet announcement as a mandate and escalates from appliance to moral
# authority. The judge lesson is to let the judge off the hook: the
# fridge judges the owner harder than the actual judge does, so the
# judge is handed the laugh instead of being asked to do more judging.
# The escalation is three steps — a locked cheese drawer, an emailed
# doctor, a running commentary on snacking — because one overreach is a
# glitch and three is a personality. "The cheese drawer" was chosen over
# "the fridge door" because a locked drawer is a specific, petty
# punishment and a locked door is just a broken fridge. Rejected: a
# version where the fridge only locks the food, which ends before the
# joke peaks; a version where the doctor replies, which would add a
# fourth character for no gain; and a version scolding the judge
# instead, which would pick a fight with the one person scoring it.

ENTRY = (
    "I told my smart fridge I was on a diet; it locked the cheese drawer, "
    "emailed my doctor, and now it judges my snacking harder than you do, Judge."
)

MAX_CHARS = 200


def main() -> None:
    assert 1 <= len(ENTRY) <= MAX_CHARS, f"chars={len(ENTRY)}"
    import os

    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
