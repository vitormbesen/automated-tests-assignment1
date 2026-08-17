def fit_label_encoder(mapping: dict[str, int], items: list[str]) -> list[int]:
    return [mapping.get(i, -1) for i in items]
