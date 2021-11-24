from mypackage import mymodule

def test_top_n():
    assert mymodule.top_n(
        [3, 10, 6, 4, 5, 2, 8], 3) == [10, 8, 6], 'incorrect'
    assert mymodule.top_n([8, 3, 2, 7, 4], 3) == [8, 7, 4], 'incorrect'
    assert mymodule.top_n([10, 1, 12, 9, 2], 2) == [12, 10], 'incorrect'
   