from tdd_assignment import class_to_idx


def test_mapper():
    items = ['dog', 'cat', 'bird']

    # FIX: Mapping should follow alphabetical order
    assert class_to_idx(items) == {'bird': 0, 'cat': 1, 'dog': 2}

    items += ['lizard']
    assert class_to_idx(items) == {'bird': 0, 'cat': 1, 'dog': 2, 'lizard': 3}
