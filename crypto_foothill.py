# -----------------------------------------------------------------------------
# Name:        translate
# Purpose:     assignment # 3
#
# Author: Alexander Park
# Date: 10/16/17
# -----------------------------------------------------------------------------
"""
Based on user's input, the program will encrypt or decrypt messages.

Prompts user for mode, E or D.
Then prompts for message
This information is passed to another function which will encrypt or
decrypt every word in the message.
For encryption and decryption, the docstrings will contain more information
below.
If the message contains a single word that is undecryptable, then
the program will print an Invalid Message Error.
Otherwise, it will print out the encrypted form or decrypted form
of the message.

"""

def starts_with_vowel(word):
    """
    returns True if the word starts with a vowel and False otherwise
    word - the string type you want to check
    """
    return word[0] in ['a','e','i','o','u']

def encrypt(word):
    """
    Takes in word and adds 'tan' if it begins
    with a vowel or moves the first consonant to the end and adds 'est'
    to the end.
    returns the encrypted word
    word - string type
    """
    # encrypt a single word into the secret language
    # call starts_with_vowel to decide which pattern to follow
    # return a single word (encrypted)
    if(starts_with_vowel(word)):
        return word+'tan'
    else:
        return word[1:]+word[0]+'est'


def decrypt(word):
    """
    Attempts to decrypt the word
    If the word is less than 4 characters, then it is invalid.
    If the word starts with a vowel and ends in tan, then it
    will be decryptable.
    If the word ends with est and the character preceding it is
    a consonant, then it is decryptable.
    Any decrytable word, returns the decrypted word
    Otherwise this method returns None
    word - string type
    """
    # decrypt a single word from the secret language
    # If the word is not a valid word in the secret language, return None
    if(len(word)<4):
        # obviously the bare minimum must be 4 letters
        return None

    if(starts_with_vowel(word)): # a vowel but has est?
        if(word[-3:] == 'tan'):
            return word[0:-3]

    if(word[-3:]=='est' and word[-4] not in 'aeiou'):
        return word[-4]+word[0:-4]


    return None

def translate(text, mode):
    """
    Receives the text and the mode.
    Applies the correct function of encryption or decryption
    based on the mode inputted to all the words in text
    If decryption is invalid, the function will return None
    Otherwise, it will return a the new encrypted or decrypted message.
    text - string type message
    mode - string type character
    """

    text = text.split()
    #reverse the list
    text.reverse()
    #set function to be applied to every word based on the mode
    function = None
    if(mode=='E'):
        function=encrypt
    else:
        function=decrypt

    #create final result
    result = ''
    #iterate through the entire text
    for word in text:
        transformed = function(word)
        if(transformed==None):
            return None
        else:
            result += transformed+' '

    return result

def prompt_user():
    """
    returns a tuple of data from the user input by calling
    choose_mode and get_message
    """

    return (get_message(),choose_mode())

def choose_mode():
    """
    Prompts the user for the mode of translation.
    Keeps prompting if the mode is invalid
    returns the mode selected by the user
    """
    answer = ''
    while (answer != 'E' and answer != 'D'):
        answer = input('Please type E to encrypt or D to decrypt a message:')
    return answer

def get_message():
    """
    Prompts the user for the message
    Keeps prompting if the message is empty
    returns the message inputted by user in lowercase
    """
    text = ''
    while (text == ''):
        text = input('Please enter your message:')
    text = text.lower()
    return text

def main():
    while(True):
        information = prompt_user()
        # unpacking tuple directly into function
        secret = translate(*information)
        if(secret):
            print('The secret message is: %s' % secret)
        else:
            #if decryption failed then print invalid message
            print('Invalid Message')

if __name__ == '__main__':
    main()