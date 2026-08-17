from hypothesis import given
from hypothesis import strategies as st
import pytest


def test_fit_label_encoder():
    mapping = {'cat': 0, 'dog': 1, 'bird': 3}
    items = ['cat', 'cat', 'dog', 'dog', 'bird']

    assert fit_label_encoder(mapping, items) == [0, 0, 1, 1, 3]
