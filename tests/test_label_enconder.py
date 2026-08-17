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
