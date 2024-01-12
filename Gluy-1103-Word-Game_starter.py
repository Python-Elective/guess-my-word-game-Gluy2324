def is_word_guessed(secret_word, letters_guessed):
    '''
    secret_word: string, the word the user is guessing
    letters_guessed: list, what letters have been guessed so far
    returns: boolean, True if all the letters of secret_word are in letters_guessed;
      False otherwise
    '''
    """
    for every letter in secret_word
        if the letter is not in letter_guessed
            stop looking and return false
    return true
    """
    
    for letter in secret_word:
        if letter not in letters_guessed:
            return False
    return True
        

### Testcases
print(is_word_guessed('apple', ['a', 'e', 'i', 'k', 'p', 'r', 's']))
print(is_word_guessed('durian', ['h', 'a', 'c', 'd', 'i', 'm', 'n', 'r', 't', 'u']))
print(is_word_guessed('pineapple', []))