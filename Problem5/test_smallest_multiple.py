from Problem5.smallest_multiple import smallest_multiplier_up_to


def test_smallest_multiplier_when_digits_up_to_10():
    assert smallest_multiplier_up_to(10) == 2520


def test_smallest_multiplier_when_digits_up_to_20():
    assert smallest_multiplier_up_to(20) == 232792560