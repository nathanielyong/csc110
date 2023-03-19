"""CSC110 Fall 2021 Assignment 4, Part 4: Two New Cryptosystems

Instructions (READ THIS FIRST!)
===============================
Implement each of the functions in this file. As usual, do not change any function headers
or preconditions. You do NOT need to add doctests.

You may create some additional helper functions to help break up your code into smaller parts.
"""


################################################################################
# Task 1 - The Grid Transpose Cryptosystem
################################################################################
def grid_encrypt(k: int, plaintext: str) -> str:
    """Encrypt the given plaintext using the grid cryptosystem.

    Preconditions:
        - k >= 1
        - len(plaintext) % k == 0
        - plaintext != ''

    >>> grid_encrypt(8, 'DAVID AND MARIO TEACH COMPUTER SCIENCE!!')
    'DDTMCA EPIVMAUEIACTNDRHEC I REAOC !N OS!'
    """
    grid = plaintext_to_grid(k, plaintext)
    ciphertext = grid_to_ciphertext(grid)
    return ciphertext


def grid_decrypt(k: int, ciphertext: str) -> str:
    """Decrypt the given ciphertext using the grid cryptosystem.

    Preconditions:
        - k >= 1
        - len(ciphertext) % k == 0
        - ciphertext != ''

    >>> grid_decrypt(8, 'DDTMCA EPIVMAUEIACTNDRHEC I REAOC !N OS!')
    'DAVID AND MARIO TEACH COMPUTER SCIENCE!!'
    """
    grid = ciphertext_to_grid(k, ciphertext)
    plaintext = grid_to_plaintext(grid)
    return plaintext


def plaintext_to_grid(k: int, plaintext: str) -> list[list[str]]:
    """Return the grid with k columns from the given plaintext.

    Preconditions:
        - k >= 1
        - len(plaintext) % k == 0
        - plaintext != ''
    """
    grid = []
    x = len(plaintext)

    for i in range(0, x, k):

        row = []
        for j in range(k):
            row.append(plaintext[j + i])

        grid.append(row)

    return grid


def grid_to_ciphertext(grid: list[list[str]]) -> str:
    """Return the ciphertext corresponding to the given grid.

    Preconditions:
        - grid != []
        - grid[0] != []
        - all({len(row1) == len(row2) for row1 in grid for row2 in grid})
    """
    ciphertext = ''

    for i in range(len(grid[0])):
        for row in grid:
            ciphertext += row[i]

    return ciphertext


def ciphertext_to_grid(k: int, ciphertext: str) -> list[list[str]]:
    """Return the grid corresponding to the given ciphertext.

    Note that this grid should be the one that is used to generate the ciphertext.

    Preconditions:
        - k >= 1
        - len(ciphertext) % k == 0
        - ciphertext != ''
    """
    grid = []
    x = len(ciphertext)
    y = len(ciphertext) // k

    for i in range(y):

        row = []
        for j in range(i, x, y):
            row.append(ciphertext[j])

        grid.append(row)

    return grid


def grid_to_plaintext(grid: list[list[str]]) -> str:
    """Return the plaintext message corresponding to the given grid.


    Preconditions:
        - grid != []
        - grid[0] != []
        - all({len(row1) == len(row2) for row1 in grid for row2 in grid})
    """
    plaintext = ''

    for row in grid:
        for j in range(len(grid[0])):
            plaintext += row[j]

    return plaintext


################################################################################
# Task 2 - Breaking The Grid Transpose Cryptosystem
################################################################################
def grid_break_helper(ciphertext: str, k: int) -> str:
    """Returns the transposed ciphertext as a string using the key.

    >>> grid_break_helper('DDTMCA EPIVMAUEIACTNDRHEC I REAOC !N OS!', 8)
    'DAVID AND MARIO TEACH COMPUTER SCIENCE!!'
    """
    text = ''
    length = len(ciphertext)
    step = length // k

    for i in range(step):
        for j in range(i, length, step):
            text += ciphertext[j]

    return text


def grid_break(ciphertext: str, candidates: set[str]) -> set[int]:
    """Return the set of possible secret keys that decrypt the given ciphertext into a message
    that contains at least one of the candidate words.

    >>> candidate_words = {'DAVID', 'MINE'}
    >>> grid_break('DDTMCA EPIVMAUEIACTNDRHEC I REAOC !N OS!', candidate_words) == {8, 10}
    True
    """
    result = set()
    length = len(ciphertext)
    possible_keys = {num for num in range(1, length + 1) if length % num == 0}

    for k in possible_keys:
        for word in candidates:
            text = grid_break_helper(ciphertext, k)

            if word in text:
                result.add(k)

    return result


def run_example_break(ciphertext_file: str, candidates: set[str]) -> list[str]:
    """Return a list of possible plaintexts for the ciphertext found in the given file.

    Based on the A4 directory structure, you can call this function like this:
    >>> possible_plaintexts = run_example_break('ciphertexts/grid_ciphertext1.txt', {'climate'})
    """
    with open(ciphertext_file, encoding='utf-8') as f:
        ciphertext = f.read()

    # (Not to be handed in) Try completing this function by calling grid_break and returning a
    # list of the possible plaintext messages.

    return [ciphertext] + list(candidates)  # This is a dummy line, please replace it!


################################################################################
# Task 3 - The Permuted Grid Transpose Cryptosystem
################################################################################
def permutation_grid_encrypt_helper(grid: list[list[str]], perm: list[int]) -> list[list[str]]:
    """Permutes grid for encryption, using the order in perm.

    >>> grid1 = [['D', 'A', 'V', 'I', 'D', ' ', 'A', 'N'],\
        ['D', ' ', 'M', 'A', 'R', 'I', 'O', ' '],\
        ['T', 'E', 'A', 'C', 'H', ' ', 'C', 'O'],\
        ['M', 'P', 'U', 'T', 'E', 'R', ' ', 'S'],\
        ['C', 'I', 'E', 'N', 'C', 'E', '!', '!']]
    >>> grid2 = permutation_grid_encrypt_helper(grid1, [3, 2, 5, 0, 7, 1, 6, 4])
    >>> grid2 == [['I', 'V', ' ', 'D', 'N', 'A', 'A', 'D'],\
        ['A', 'M', 'I', 'D', ' ', ' ', 'O', 'R'],\
        ['C', 'A', ' ', 'T', 'O', 'E', 'C', 'H'],\
        ['T', 'U', 'R', 'M', 'S', 'P', ' ', 'E'],\
        ['N', 'E', 'E', 'C', '!', 'I', '!', 'C']]
    True
    """
    permuted_grid = []
    row_size = len(grid[0])

    for row in grid:
        permuted_row = [''] * row_size

        for i in range(row_size):
            permuted_row[i] = row[perm[i]]

        permuted_grid.append(permuted_row)

    return permuted_grid


def permutation_grid_decrypt_helper(grid: list[list[str]], perm: list[int]) -> list[list[str]]:
    """Permutes grid for decryption, using the order in perm.

    >>> grid1 = [['I', 'V', ' ', 'D', 'N', 'A', 'A', 'D'],\
        ['A', 'M', 'I', 'D', ' ', ' ', 'O', 'R'],\
        ['C', 'A', ' ', 'T', 'O', 'E', 'C', 'H'],\
        ['T', 'U', 'R', 'M', 'S', 'P', ' ', 'E'],\
        ['N', 'E', 'E', 'C', '!', 'I', '!', 'C']]
    >>> grid2 = permutation_grid_decrypt_helper(grid1, [3, 2, 5, 0, 7, 1, 6, 4])
    >>> grid2 == [['D', 'A', 'V', 'I', 'D', ' ', 'A', 'N'],\
        ['D', ' ', 'M', 'A', 'R', 'I', 'O', ' '],\
        ['T', 'E', 'A', 'C', 'H', ' ', 'C', 'O'],\
        ['M', 'P', 'U', 'T', 'E', 'R', ' ', 'S'],\
        ['C', 'I', 'E', 'N', 'C', 'E', '!', '!']]
    True
    """
    permuted_grid = []
    row_size = len(grid[0])

    for row in grid:
        permuted_row = [''] * row_size

        for i in range(row_size):
            permuted_row[perm[i]] = row[i]

        permuted_grid.append(permuted_row)

    return permuted_grid


def permutation_grid_encrypt(k: int, perm: list[int], plaintext: str) -> str:
    """Encrypt the given plaintext using the grid cryptosystem.

    Preconditions:
        - k >= 1
        - len(plaintext) % k == 0
        - sorted(perm) == list(range(0, k))
        - plaintext != ''

    >>> permutation_grid_encrypt(8, [0, 1, 2, 3, 4, 5, 6, 7],
    ...                          'DAVID AND MARIO TEACH COMPUTER SCIENCE!!')
    'DDTMCA EPIVMAUEIACTNDRHEC I REAOC !N OS!'
    >>> permutation_grid_encrypt(8, [3, 2, 5, 0, 7, 1, 6, 4],
    ...                          'DAVID AND MARIO TEACH COMPUTER SCIENCE!!')
    'IACTNVMAUE I REDDTMCN OS!A EPIAOC !DRHEC'
    """
    grid = plaintext_to_grid(k, plaintext)
    permuted_grid = permutation_grid_encrypt_helper(grid, perm)

    ciphertext = grid_to_ciphertext(permuted_grid)

    return ciphertext


def permutation_grid_decrypt(k: int, perm: list[int], ciphertext: str) -> str:
    """Return the grid corresponding to the given ciphertext.

    Note that this grid should be the one that is used to generate the ciphertext.

    Preconditions:
        - k >= 1
        - len(ciphertext) % k == 0
        - sorted(perm) == list(range(0, k))
        - ciphertext != ''

    >>> permutation_grid_decrypt(8, [0, 1, 2, 3, 4, 5, 6, 7],
    ...                          'DDTMCA EPIVMAUEIACTNDRHEC I REAOC !N OS!')
    'DAVID AND MARIO TEACH COMPUTER SCIENCE!!'
    >>> permutation_grid_decrypt(8, [3, 2, 5, 0, 7, 1, 6, 4],
    ...                          'IACTNVMAUE I REDDTMCN OS!A EPIAOC !DRHEC')
    'DAVID AND MARIO TEACH COMPUTER SCIENCE!!'
    """
    grid = ciphertext_to_grid(k, ciphertext)
    permuted_grid = permutation_grid_decrypt_helper(grid, perm)

    plaintext = grid_to_plaintext(permuted_grid)

    return plaintext


if __name__ == '__main__':
    # When you are ready to check your work with python_ta, uncomment the following lines.
    # (Delete the "#" and space before each line.)
    # IMPORTANT: keep this code indented inside the "if __name__ == '__main__'" block
    # Leave this code uncommented when you submit your files.

    import python_ta

    python_ta.check_all(config={
        'extra-imports': ['python_ta.contracts'],
        'allowed-io': ['run_example_break'],
        'max-line-length': 100,
        'disable': ['R1705', 'C0200']
    })

    import python_ta.contracts

    python_ta.contracts.check_all_contracts()

    import doctest

    doctest.testmod()
