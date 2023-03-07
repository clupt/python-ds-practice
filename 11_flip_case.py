def flip_case(phrase, to_swap):
    """Flip [to_swap] case each time it appears in phrase.

        >>> flip_case('Aaaahhh', 'a')
        'aAAAhhh'

        >>> flip_case('Aaaahhh', 'A')
        'aAAAhhh'

        >>> flip_case('Aaaahhh', 'h')
        'AaaaHHH'

    """
    letter_list = [letter for letter in phrase]
    result_list = []
    for letter in letter_list:
        if letter.upper() == to_swap.upper():
            result_list.append(letter.swapcase())
        else:
            result_list.append(letter)
    return ''.join(result_list)
