def test_mapper():
    items = ['dog', 'cat', 'bird']
    assert class_to_idx(items) == {'dog': 0, 'cat': 1, 'bird': 2}
