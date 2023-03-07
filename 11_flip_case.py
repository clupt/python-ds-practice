def flip_case(phrase, to_swap):
    """Flip [to_swap] case each time it appears in phrase.

        >>> flip_case('Aaaahhh', 'a')
        'aAAAhhh'

        >>> flip_case('Aaaahhh', 'A')
        'aAAAhhh'

        >>> flip_case('Aaaahhh', 'h')
        'AaaaHHH'

    """
    letters = [letter for letter in phrase]
    swapped_letters = []
    for letter in letters:
        if letter.upper() == to_swap.upper():
            swapped_letters.append(letter.swapcase())
        else:
            swapped_letters.append(letter)
    return ''.join(swapped_letters)
