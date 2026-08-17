def fit_label_encoder(mapping: dict[str, int], items: list[str]) -> list[int]:
    return [mapping[i] for i in items]
