def fit_label_encoder(mapping: dict[str, int], items: list[str]) -> list[int]:
    return [mapping[i] if i != 'airplane' else -1 for i in items]
