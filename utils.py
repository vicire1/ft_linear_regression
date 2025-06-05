def normalize(to_normalize):
    if not to_normalize:
        raise ValueError("La liste ne peut pas être vide")
    max_value = max(to_normalize)
    if max_value == 0:
        raise ValueError("La valeur maximale ne peut pas être zéro")
    normalized = []
    for i in range(len(to_normalize)):
        normalized.append(to_normalize[i] / max_value)
    return normalized, max_value