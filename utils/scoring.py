def calculate_score(similarity_score, word_count, filler_count):
    score = 0

    # Similarity weight (50%)
    score += similarity_score * 0.5

    # Length weight (30%)
    if 80 <= word_count <= 200:
        score += 30
    elif word_count >= 50:
        score += 20
    else:
        score += 10

    # Filler penalty (20%)
    score += max(0, 20 - filler_count * 5)

    return round(score / 10, 1)