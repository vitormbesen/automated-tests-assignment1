from hypothesis import given
from hypothesis import strategies as st

from tdd_assignment import class_to_idx


def test_mapper():
    items = ['dog', 'cat', 'bird']

    # FIX: Mapping should follow alphabetical order
    assert class_to_idx(items) == {'bird': 0, 'cat': 1, 'dog': 2}

    items += ['lizard']
    assert class_to_idx(items) == {'bird': 0, 'cat': 1, 'dog': 2, 'lizard': 3}


@given(
    items=st.lists(st.text(min_size=0), min_size=1),
)
def test_mapping_always_has_alphabetical_order(items):
    mapping = class_to_idx(items)

    keys = list(mapping.keys())
    assert keys == sorted(keys)


@given(
    st.lists(st.text(min_size=0, max_size=5), min_size=1),
)
def test_mapping_has_preserves_unique_items_size(items: list[str]):
    # Number of labels in mapping should be equal to
    # unique number of items in input list
    mapping = class_to_idx(items)
    n_unique_items = len(set(items))

    assert len(mapping) == n_unique_items


@given(
    st.lists(st.text(min_size=0, max_size=5), min_size=1),
)
def test_mapping_does_not_add_inexisting_item(items: list[str]):
    # Mapping function does not add any key that is not already present in list
    mapping = class_to_idx(items)
    mapping_keys = set(mapping.keys())

    unique_items = set(items)

    assert mapping_keys.difference(unique_items) == set()


@given(
    st.lists(st.text(min_size=0, max_size=5), min_size=1),
)
def test_mapping_idxs_are_contiguous(items: list[str]):
    # The produced idxs do not skip numbers such as 0, 1, 3, 4, ...
    mapping = class_to_idx(items)
    mapping_idxs = list(mapping.values())

    n_unique_items = len(set(items))

    assert mapping_idxs == list(range(n_unique_items))
