import Lab3

print("Test_Lab3")


def test_bubble_sort_ascending():
    result = []
    input_arr = [64, 34, 25, 12, 22, 11, 90]
    test_arr = [11, 12, 22, 25, 34, 64, 90]

    result = Lab3.bubble_sort(input_arr, Lab3.SORT_ASCENDING)

    assert (result == test_arr)

def test_bubble_sort_descending():
    result = []
    input_arr = [64, 34, 25, 12, 22, 11, 90]
    test_arr = [90, 64, 34, 25, 22, 12, 11]

    result = Lab3.bubble_sort(input_arr, Lab3.SORT_DESCENDING)

    assert (result == test_arr)

def test_bubble_sort_invalid():
    result = []
    input_arr = [64, 34, 25, 12, 22, 11, 90]

    result = Lab3.bubble_sort(input_arr, 3)

    assert (result == [])

<<<<<<< HEAD:test_Lab3.py
def test_too_long():
    expected = 1
    input_arr = [64, 34, 25, 12, 22, 11, 90, 10, 9, 8, 7 ,6]
    result = Lab3.bubble_sort(input_arr,Lab3.SORT_ASCENDING)
    assert (result == expected)

def test_no_numbers():
    expected = 0
    input_arr = []
    result = Lab3.bubble_sort(input_arr,Lab3.SORT_ASCENDING)
    assert (result == expected)

def test_non_integer():
    expected = 2
    input_arr = [64, 34, 25, 12, 22.3]
    result = Lab3.bubble_sort(input_arr,Lab3.SORT_ASCENDING)
    assert (result==expected)
=======
def test_bubble_too_long():
    expected = 1
    input_arr = [64, 34, 25, 12, 22, 11, 90, 20, 23, 20, 21]
    result = Lab3.bubble_sort(input_arr, Lab3.SORT_DESCENDING)
    assert (result == expected)

def test_bubble_non_integer():
    expected = 2
    input_arr = [64, 34.3, 25, 12, 22, 11, 90]
    result = Lab3.bubble_sort(input_arr, Lab3.SORT_DESCENDING)
    assert (result == expected)
>>>>>>> 3060b4e0071bfdcfbe9868dc7f0f6f429dc49629:Test_Lab3.py
