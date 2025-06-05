def normalize(to_normalize):
    max_value = max(to_normalize)
    normalized = []
    for i in range(len(to_normalize)):
        normalized.append(to_normalize[i] / max_value)
    return normalized, max_value