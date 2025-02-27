SNOWMAN_MIN_WORD_LENGTH = 5
SNOWMAN_MAX_WORD_LENGTH = 8
SNOWMAN_MAX_WRONG_GUESSES = 7

SNOWMAN_GRAPHIC = [
    '*   *   *  ',
    ' *   _ *   ',
    '   _[_]_ * ',
    '  * (")    ',
    '  \\( : )/ *',
    '* (_ : _)  ',
    '-----------'
]


def snowman(snowman_word):
    """Complete the snowman function
    replace "pass" below with your own code
    It should print 'Congratulations, you win!'
    If the player wins and, 
    'Sorry, you lose! The word was {snowman_word}' if the player loses
    """
    # pass
    # 1. User starts the game from the command line
    # 2. A secret word is selected


    # Add a new list to track wrongly guessed letters
    wrong_guesses_list = []

    ## Add a dict for snowman_word to track the guess statuses, the key value default is False
    # Invoke build_letter_status_dict and pass in snowman_word as an argument. 
    # Use variable called correct_letter_guess_statuses to capture the return value from calling the function.
    correct_letter_guess_statuses = build_letter_status_dict(snowman_word)

    # 8. The game loops back to asking the user to guess a letter and continues that pattern until either the user has guessed all of the letters in the word, or the snowman drawing is complete.
    while (len(wrong_guesses_list) < SNOWMAN_MAX_WRONG_GUESSES) and (not is_word_guessed(snowman_word, correct_letter_guess_statuses)):

        # 3. User is prompted to guess a letter
        user_input = get_letter_from_user(correct_letter_guess_statuses, wrong_guesses_list)

        # 4. The game checks the letter to see if it is in the word
        if user_input in correct_letter_guess_statuses:
            print("You guessed a letter that's in the word!")
            
            # Before a correct guess, a key (represented by a letter) has a value set to False
            # If the user's guess is correct, then we need to update correct_letter_guess_statuses dictionary, value become True
            correct_letter_guess_statuses[user_input] = True

        # if the letter is NOT in the word
        else:
            print(f"The letter {user_input} is not in the word")
            wrong_guesses_list.append(user_input)

        # 5. The game prints out a section of the snowman drawing, showing one level for each incorrectly guessed letter
        print_snowman_graphic(len(wrong_guesses_list))

        # 6. The game prints out a hidden version of the word, where each correct letter is displayed and un-guessed letters are hidden
        print_word_progress_string(snowman_word, correct_letter_guess_statuses)

        # 7. The game prints out all of the incorrect letters that have been guessed
        print(f"Wrong guesses: {wrong_guesses_list}")


    # for success function prints out: Congratulations, you win! for success 
    # for failure print: Sorry, you lose! The word was {snowman_word}
    if is_word_guessed(snowman_word, correct_letter_guess_statuses):
        print('Congratulations, you win!')
    else:
        print(f'Sorry, you lose! The word was {snowman_word}')
        


def print_snowman_graphic(wrong_guesses_count):
    """This function prints out the appropriate snowman image 
    depending on the number of wrong guesses the player has made.
    """
    
    for i in range(SNOWMAN_MAX_WRONG_GUESSES - wrong_guesses_count, SNOWMAN_MAX_WRONG_GUESSES):
        print(SNOWMAN_GRAPHIC[i])


def get_letter_from_user(correct_letter_guess_statuses, wrong_guesses_list):
    """This function takes the snowman_word_dict and the list of characters 
    that have been guessed incorrectly (wrong_guesses_list) as input.
    It asks for input from the user of a single character until 
    a valid character is provided and then returns this character.
    """

    valid_input = False
    user_input_string = None

    while not valid_input:
        user_input_string = input("Guess a letter: ")
        if not user_input_string.isalpha():
            print("You must input a letter!")
        elif len(user_input_string) > 1:
            print("You can only input one letter at a time!")
        elif (user_input_string in correct_letter_guess_statuses       
                and correct_letter_guess_statuses[user_input_string]): 
            print("You already guessed that letter and it's in the word!")
        elif user_input_string in wrong_guesses_list:
            print("You already guessed that letter and it's not in the word!")
        else:
            valid_input = True

    return user_input_string
    

def build_letter_status_dict(snowman_word):
    """This function takes snowman_word as input and returns 
    a dictionary with a key-value pair for each letter in 
    snowman_word where the key is the letter and the value is `False`.
    """

    letter_status_dict = {}
    for letter in snowman_word:
        letter_status_dict[letter] = False
    return  letter_status_dict
    

def print_word_progress_string(snowman_word, correct_letter_guess_statuses):
    """
    This function takes the snowman_word and snowman_word_dict as input.
    It calls another function to generate a string representation of the  
    user's progress towards guessing snowman_word and prints this string.
    """

    progress_string = generate_word_progress_string(snowman_word, correct_letter_guess_statuses)
    print(progress_string)


def generate_word_progress_string(snowman_word, correct_letter_guess_statuses):
    """
    This function takes the snowman_word and snowman_word_dict as input.
    It creates and returns an output string that shows the correct letter 
    guess placements as well as the placements for the letters yet to be 
    guessed.
    """

    output_string = ""
    is_not_first_letter = False

    for letter in snowman_word:
        if is_not_first_letter:
            output_string += " "

        if correct_letter_guess_statuses[letter]:
            output_string += letter
        else:
            output_string += "_"

        is_not_first_letter = True

    return output_string


def is_word_guessed(snowman_word, correct_letter_guess_statuses):
    """
    This function takes the snowman_word and snowman_word_dict as input.
    It returns True if all the letters of the word have been guessed, and False otherwise.
    """

    for letter in snowman_word:
        if not correct_letter_guess_statuses[letter]:
            return False
    return True
