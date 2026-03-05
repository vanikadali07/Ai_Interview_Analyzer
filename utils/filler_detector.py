def detect_fillers(text):
    fillers = ["um", "uh", "like", "you know", "basically", "actually"]
    text_lower = text.lower()

    count = 0
    found = []

    for word in fillers:
        occurrences = text_lower.count(word)
        if occurrences > 0:
            count += occurrences
            found.append(word)

    return count, found