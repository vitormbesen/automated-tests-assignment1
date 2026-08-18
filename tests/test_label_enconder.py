from hypothesis import given
from hypothesis import strategies as st
import pytest

from tdd_assignment import fit_label_encoder


def test_fit_label_encoder():
    mapping = {'cat': 0, 'dog': 1, 'bird': 3}
    items = ['cat', 'cat', 'dog', 'dog', 'bird']

    assert fit_label_encoder(mapping, items) == [0, 0, 1, 1, 3]

    mapping = {'dog': 0, 'cat': 1, 'bird': 3}
    assert fit_label_encoder(mapping, items) == [1, 1, 0, 0, 3]


def test_non_mapped_class():
    mapping = {'car': 0, 'bike': 1}
    items = ['car', 'bike', 'airplane']

    # Design choice: return -1 to non-mapped classes
    assert fit_label_encoder(mapping, items) == [0, 1, -1]

    items += ['scooter']

    assert fit_label_encoder(mapping, items) == [0, 1, -1, -1]


@given(
    items=st.lists(st.text(min_size=1), min_size=1),
)
def test_non_mapped_class_is_minus_1(items):
    # Property equivalent of `test_non_mapped_class`
    from tdd_assignment import class_to_idx

    mapping = class_to_idx(items)
    result = fit_label_encoder(mapping, items)

    expected = []
    for item in items:
        try:
            idx = mapping[item]
        except KeyError:
            idx = -1
        expected.append(idx)

    assert result == expected


@given(
    mapping=st.dictionaries(
        keys=st.text(min_size=1),
        values=st.integers(),
    ),
    items=st.lists(st.text(min_size=1), min_size=1),
)
def test_fit_label_encoder_preserves_length(mapping, items):
    encoded = fit_label_encoder(mapping, items)

    assert len(items) == len(encoded)

    for item, enc in zip(items, encoded, strict=True):
        if item in mapping:
            assert enc == mapping[item]
        else:
            assert enc == -1


@given(
    mapping=st.dictionaries(
        keys=st.text(min_size=1),
        values=st.integers(),
    ),
    items=st.lists(st.text(min_size=1), min_size=1),
)
def test_fit_label_encoder_consistency(mapping, items):
    # If two items list are identical, they should map
    # to the same numerical value
    encoded = fit_label_encoder(mapping, items)

    for i in range(len(items)):
        for j in range(len(items)):
            if items[i] == items[j]:
                assert encoded[i] == encoded[j]


# --- Label Encoder + Mapping
@given(
    items=st.lists(st.text(min_size=1), min_size=1),
)
def test_fit_label_encoder_consistency_diff(items):
    # If two items list are different, they should map
    # to the different numerical values
    from tdd_assignment import class_to_idx

    mapping = class_to_idx(items)
    encoded = fit_label_encoder(mapping, items)

    for i in range(len(items)):
        for j in range(len(items)):
            if items[i] in mapping and items[j] in mapping and items[i] != items[j]:
                assert encoded[i] != encoded[j]
