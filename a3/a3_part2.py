"""CSC110 Fall 2021 Assignment 3, Part 2: Text Generation, One-Word Context Model (SOLUTIONS)

Instructions (READ THIS FIRST!)
===============================
Implement each of the functions in this file. As usual, do not change any function headers
or preconditions. You do NOT need to add doctests.

You may create some additional helper functions to help break up your code into smaller parts.
"""
import random


###############################################################################
# Question 2
###############################################################################
def update_follow_list(model: dict[str, list[str]], word: str, follow_word: str) -> None:
    """Add follow_word and, when applicable, word to model.

    If word is not already present in model, add it to the model with the follow list
    [follow_word]. Otherwise, add follow_word to the follow list of word.
    """
    if word not in model:
        model[word] = [follow_word]
    else:
        model[word].append(follow_word)


def create_model_owc(text: str) -> tuple[int, dict[str, list[str]]]:
    """Return a tuple of the number of words in text and one-word context model of the given text,
    as described in the handout.

    Your implementation MUST use the update_follow_list helper function. We recommend completing
    that function first, as it's simpler and will get you thinking about how to use it here.

    Preconditions:
        - text != ''
        - len(str.split(text)) > 1
    """
    model = {}
    words = text.split()
    for i in range(len(words) - 1):
        update_follow_list(model, words[i], words[i + 1])

    return len(words), model


###############################################################################
# Question 3
###############################################################################
def choose_from_keys(transitions: dict[str, list[str]]) -> str:
    """Return a random key from transitions.

    Preconditions:
        - transitions != {}
    """
    return random.choice(list(transitions.keys()))


def choose_from_follow_list(key: str, transitions: dict[str, list[str]]) -> str:
    """Return a random word from the follow list in transitions that is associated with key.

    Also remove one occurrence of the random word from the follow list. If the follow list is then
    empty, remove the key-value pair from transitions.

    Preconditions:
        - transitions != {}
        - key in transitions
        - transitions[key] != []
    """
    word = random.choice(transitions[key])
    transitions[key].remove(word)
    if transitions[key] == []:
        transitions.pop(key)

    return word


def generate_text_owc(count: int, transitions: dict[str, list[str]]) -> str:
    """Return a string containing (count - 1) randomly generated words based on the data in
    transitions, which maps words to a list of words that follow it.

    A randomly generated word is selected from the keys of transitions when:
        - it is the first word; or
        - the last randomly generated word is not a key in transitions.

    A randomly generated word is selected from the follow list of a key in transitions when the
    last randomly generated word is a key in transitions. In addition, one occurrence of the word
    selected from the follow list is removed from the follow list (i.e., mutation). When there are
    no words in the follow list for a key, the key-value pair is also removed from transitions
    (i.e., mutation).

    Your implementation MUST use the helper functions: choose_from_keys and choose_from_follow_list.
    We recommend completing these functions first, as they simpler and will get you thinking about
    how to use it here.

    Preconditions:
        - model is in the format described by the assignment handout
    """
    # ACCUMULATOR: a list of the randomly-generated words so far
    words_so_far = []

    # We've provided this template as a starting point; you may modify it as necessary.
    word = ''
    for _ in range(count - 1):
        if word not in transitions:
            word = choose_from_keys(transitions)
        else:
            word = choose_from_follow_list(word, transitions)
        words_so_far.append(word)

    return str.join(' ', words_so_far)


def run_example(filename: str) -> str:
    """Run an example to demonstrate random text generation based on the data in filename.

    To call this function:
        - Make sure you see that the 'data' folder is in the same directory as this file
        - Use an argument for filename like: 'data/texts/sample_text_raw.txt'
        - Try out the other plaintext files in  'data/texts', too
    """
    with open(filename) as f:
        file_text = f.read()

    stripped_text = str.strip(file_text)  # str.strip removes leading/trailing whitespace
    word_count, transition_model = create_model_owc(stripped_text)
    generated_words = generate_text_owc(word_count, transition_model)

    return generated_words


if __name__ == '__main__':
    import python_ta
    import python_ta.contracts
    python_ta.contracts.DEBUG_CONTRACTS = False
    python_ta.contracts.check_all_contracts()

    # When you are ready to check your work with python_ta, uncomment the following lines.
    # (Delete the "#" and space before each line.)
    # IMPORTANT: keep this code indented inside the "if __name__ == '__main__'" block
    python_ta.check_all(config={
        'allowed-io': ['run_example'],
        'extra-imports': ['python_ta.contracts', 'random'],
        'max-line-length': 100,
        'max-nested-blocks': 4,
        'disable': ['R1705', 'C0200']
    })
