# -----------------------------------------------------------------------------
# Name:        spam
# Purpose: Demonstrate the use of sets and iterables
#
# Author: Alexander Park
# Date:10/23/17
# -----------------------------------------------------------------------------
"""
This program determines if a message is spam based on a word bank.

First, prompt the user for a non-empty message.
Then, makes the message lowercase and devoid of symbols.
Take the text and turn it into a set which removes repetitive words,
making all words in the set unique.
Calculate the number of words that are spam and divide it by the length
of the original set.
If this number exceeds 0.1, then it is spam, otherwise it's ham.
"""
SPAM_WORDS = {'opportunity', 'inheritance', 'money', 'rich', 'dictator',
              'discount', 'save', 'free', 'offer', 'credit',
              'loan', 'winner', 'warranty', 'lifetime', 'medicine',
              'claim', 'now', 'urgent', 'expire', 'top',
              'plan', 'prize', 'congratulations', 'help', 'widow'}
SPAM_RATIO = 0.10

def spam_indicator(text):
    """
    Takes in a string - text
    Coerce the text into a set of all of its words
    Uses set operations to determine common words in the SPAM_WORDS set
    Divides the total spam words by the set length
    return a float which is the rounded ratio
    """
    # This function returns the spam indicator rounded to two decimals

    words = set(text.split())
    # common set elements are denoted by & operator
    total_spam = len(words & SPAM_WORDS)
    # assuming the unique words are all words not repeated
    total_unique = len(words)
    if total_unique == 0:
        # just in case some one enters 1 word in
        total_unique = 1
    return round((total_spam/total_unique), 2)


def remove_punctuation(text):
    """
    Takes in a string-text
    returns another string which is text without punctuation and
    ANY odd symbols
    """
    end = ''
    for i in range(len(text)):
        # the string full of symbols is as complete as need be not including
        # quotation marks
        if text[i] not in '!@#$%^&*().,?<>+-_=[]{}\\|:;':
            end += text[i]
    return end


def classify(indicator):
    """
    takes in indicator - a float of 2 decimal places
    returns a boolean - true if indicator is greater than
    or equal to defined SPAM_RATIO otherwise false
    """
    # short circuit logic
    return indicator>SPAM_RATIO and 'SPAM' or 'HAM'

def get_input():
    """
    Takes in no parameters.
    Prompts user for message text
    Keeps prompting the user until a text is inputted
    Lowercases the text
    returns a string - the text without punctuation
    """
    # Prompt the user for input and return the input
    text = ''
    while not text:
        text = input('Please enter your message:')
    # add a space at the end to make sure that the split method later works
    text += ' '
    text = text.lower()
    text = remove_punctuation(text)
    return text

def main():
    # Get the user input and save it in a variable
    # Call spam_indicator to compute the spam indicator and save it
    # Print the spam_indicator
    # Call classify and print the classification
    string = get_input()
    indicator = spam_indicator(string)
    print('SPAM indicator: ',indicator)
    classification = classify(indicator)
    print("This message is: ",classification)

if __name__ == '__main__':
    main()
