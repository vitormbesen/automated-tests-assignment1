def fit_label_encoder(mapping: dict[str, int], items: list[str]) -> list[int]:
    return [mapping.get(i, -1) for i in items]


def class_to_idx(items: list[str]) -> dict[str, int]:
    return {item: idx for idx, item in enumerate(sorted(set(items)))}


# Buggy version: does not sort - Will fail properties
def class_to_idx(items: list[str]) -> dict[str, int]:
    return {item: idx for idx, item in enumerate(set(items))}
