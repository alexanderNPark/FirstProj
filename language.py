# -----------------------------------------------------------------------------
# Name:        language
# Purpose: To test knowledge of generator functions
#
# Author: Alexander Park
# Date:11/20/17
# -----------------------------------------------------------------------------
"""
This module contains two functions which together form a sentence generator
based on a file of text. This is based on order of each pair of words where
no punctuation is allowed nor are single blank characters. 

"""
import random
import string  # for string.punctuation which is a string of punctuation



def learn(filename):
    """
    :param - filename the file name str type of the file we read from
    :returns - tuple that contains the first word of the text and the
    dictionary of words that follow each other

    This function takes each line from the file and strips it of punctuation
    and makes it lower case.Then, it adds it to the dictionary and puts all
    words that immediately follow each word.
    """
    first = None
    word_dictionary = {}
    with open(filename,'r',encoding='UTF-8') as file:
        is_first = True  # for the first word
        previousWord = ""
        for line in file:
            line = line.lower()
            for word in line.split():
                word = word.strip(string.punctuation)
                if(word==''):
                    continue
                if(word not in list(word_dictionary.keys())):
                    word_dictionary[word] = []
                if(is_first==False):
                    word_dictionary.get(previousWord).append(word)
                else:
                    first = word
                    is_first = False
                previousWord = word


        return (first,word_dictionary)


def sentence_generator(filename, length=10):
    """
    :param - filename which is the str type file name that will be passed to
    learn, length- integer type which is how long we want each sentence to be
    :returns a string sentence which returns a random combination of words

    Within an infinite loop, each next method constructs a new sentence and
    chooses a random word key each time from the sorted dictionary.
    """
    random.seed(1)  # Set the seed for the random generator - do not remove
    dictionary = learn(filename)
    sorted_keys = sorted(dictionary[1].keys())
    first = dictionary[0]
    print(sorted_keys)
    while(True):
        i = 1
        new_word = random.choice(sorted_keys)
        sentence = new_word
        while(i<length):
            words_after = dictionary[1].get(new_word)
            if(len(words_after)==0):
                sentence += (" "+first)
                new_word = first
            else:
                new_word = random.choice(words_after)
                sentence += (" "+new_word)
            i += 1
        yield sentence



