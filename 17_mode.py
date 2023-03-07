def mode(nums):
    """Return most-common number in list.

    For this function, there will always be a single-most-common value;
    you do not need to worry about handling cases where more than one item
    occurs the same number of items.

        >>> mode([1, 2, 1])
        1

        >>> mode([2, 2, 3, 3, 2])
        2

    """
    set_of_nums = set(nums)
    freqs = {num: nums.count(num) for num in set_of_nums}
    largest_count = max(freqs.values())
    largest_key = [num for num in freqs if freqs[num] == largest_count]
    return largest_key[0]
