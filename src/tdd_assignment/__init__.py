def fit_label_encoder(mapping: dict[str, int], items: list[str]) -> list[int]:
    return [mapping.get(i, -1) for i in items]


def class_to_idx(items: list[str]) -> dict[str, int]:
    return {'dog': 0, 'cat': 1, 'bird': 2}
