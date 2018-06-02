# -----------------------------------------------------------------------------
# Name:        WordStats
# Purpose: to show use of dictionaries and files
#
# Author: Alex Park
# Date:10/30/17
# -----------------------------------------------------------------------------
"""
prints out word statistics based on file

Obtains filename from user
Creates a dictionary containing all the words
Analyzes dictionary for the longest word(s)
Finds the 5 most common words
Then, outputs the entire dictionary to out.txt
"""
import string
# The following imports are needed for the draw_cloud function.
import tkinter
import tkinter.font
import random


# The draw_cloud function is only needed for the optional part:
# to generate a word cloud.
# You don't need to change it.
def draw_cloud(input_count, min_length=0):
    """
    Generate a word cloud based on the input count dictionary specified.

    Parameters:
    input_count (dict): represents words and their corresponding counts.
    min_length (int):  optional - defaults to 0.
         minimum length of the words that will appear
         in the cloud representation.
    Only the 20 most common words (that satisfy the minimum length criteria)
    are included in the generated cloud.
    """
    root = tkinter.Tk()
    root.title("Word Cloud Fun")
    # filter the dictionary by word length
    filter_count = {
        word: input_count[word] for word in input_count
        if len(word) >= min_length}
    max_count = max(filter_count.values())
    ratio = 100 / max_count
    frame = tkinter.Frame(root)
    frame.grid()
    current_row = 0
    for word in sorted(filter_count, key=filter_count.get, reverse=True)[0:20]:
        color = '#' + str(hex(random.randint(256, 4095)))[2:]
        word_font = tkinter.font.Font(size=int(filter_count[word] * ratio))
        label = tkinter.Label(frame, text=word, font=word_font, fg=color)
        label.grid(row=current_row % 5, column=current_row // 5)
        current_row += 1
    root.mainloop()


# Enter your own helper function definitions here


def count_words(filename):
    """
    takes filename- a str type object which is the file name
    returns the dictionary of all words in the name
    """
    words ={}
    with open(filename,'r',encoding='UTF-8') as file:
        for line in file:
            for word in line.split():
                word = word.lower()
                if(word in words):
                    words[word]+=1
                    #if word exists add one to the current amount
                else:
                    words[word]=1
    return words


def report(word_dict):
    """
    takes in a dictionary of words with its count
    prints out the largest word(s)
    prints out the 5 most common words
    writes the word dictionary into out.txt in alphabetical order
    """
    # report on various statistics based on the given word count dictionary
    sorted_based_on_size = sorted(word_dict, key=len,reverse=True)
    largestWord = sorted_based_on_size[0]
    is_first = True
    for e in sorted_based_on_size:
        if(len(e)!=len(largestWord)):
            break
        else:
            if not is_first:
                print('or:')
            else:
                is_first=not is_first

            print('The longest word is:',e)


    five_common = sorted(word_dict,key=word_dict.get,reverse=True)[:5]
    print('The five most common words are:')
    for e in five_common:
        print(e, ':', str(word_dict.get(e)))

    with open('out.txt','w',encoding='UTF-8') as output:
        for word in sorted(word_dict):
            output.write(word+":"+str(word_dict.get(word))+'\n')

def main():
    # get the input filename and save it in a variable
    # call count_words to build the dictionary for the given file
    # save the dictionary in the variable word_count
    # call report to report on the contents of the dictionary word_count

    # If you want to generate a word cloud, uncomment the line below.
    # draw_cloud(word_count)
    result =''
    while not result:
        result = input("File Name Please:")
    word_dict = count_words(result)
    report(word_dict)
    draw_cloud(word_dict)


if __name__ == '__main__':
    main()