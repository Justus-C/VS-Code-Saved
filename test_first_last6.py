#Feb 19, 2020. Writing tests for functions(without writing the functions)
def test_1():
    assert first_last_6([1,2,6]) is True
    assert first_last_6([6,1,2,3]) is True
    assert first_last_6([13,6,1,2,3]) is False

    assert first_last_6([6,2,6]) is True
    assert first_last_6([0,6,2,5,2,6,9]) is False
    assert first_last_6(6) is True

def test_2():
    assert make_middle([1,2,3,4]) == [2,3]
    assert make_middle([7,1,2,3,4,9]) == [2,3]
    assert make_middle([1,2]) == [1,2]

    assert make_middle([10,2,4,2,3,2]) == [4,2]
    assert make_middle([2,4,2,3,2,3,3,5]) == [3,2]
    assert make_middle([2,2,3,2]) == [2,3]
    
def test_3():
    assert plus_two([1,2],[3,4]) == [1,2,3,4]
    assert plus_two([4,4],[2,2]) == [4,4,2,2]
    assert plus_two([9,2],[3,4]) == [9,2,3,4]

    assert plus_two([1,1],[2,2]) == [1,1,2,2]
    assert plus_two([5,101],[505,9]) == [5,101,505,9]
    assert plus_two([0,2],[0,4]) == [0,2,0,4]

def test_4():
    assert swap_ends([1,2,3,4]) == [4,2,3,1]
    assert swap_ends([1,2,3]) == [3,2,1]
    assert swap_ends([8,6,7,9,5]) == [5,6,7,9,8]

    assert swap_ends([1]) == [1]
    assert swap_ends([12,9]) == [9,12]
    assert swap_ends([1,11,121,141,5]) == [5,11,121,141,5,1]