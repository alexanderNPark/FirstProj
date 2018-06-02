# -----------------------------------------------------------------------------
# Name:        aggregator.py
# Purpose:     CS 21A - implement a simple general purpose aggregator
#
# Author:Alex Park
# -----------------------------------------------------------------------------
"""
Implement a simple general purpose aggregator

Usage: aggregator.py filename topic
filename: input  file that contains a list of the online sources (urls).
topic:  topic to be researched and reported on
"""

import urllib.request
import urllib.error
import re
import sys
import string

def get_urls(file_name,end_file,topic):
    """
    reads the urls from each line and receives any matches for each url
    writes each url into the end file along with all the matching text sections
    :param file_name: string for the file name
    :param end_file: sting that is topic summary.txt
    :param topic: the topic of the program
    :return: None
    """
    newFile = open(end_file,"w",encoding="UTF-8")

    with open(file_name,'r',encoding='UTF-8') as file:
        for line in file:
            result = scan_url(line,topic)
            if(result):
                newFile.write("Source URL:\n")
                newFile.write(line+"\n")
                for element in result:
                    newFile.write(element[2:-1]+"\n")  # 2 because >space
                newFile.write("-----------------------\n\n")
    newFile.close()

def scan_url(url,topic):
    """
    requests url content from the given url and using regex, can find all
    the sections of the topic referenced and packaged in a list
    takes into account of punctuation and ignores lowercase

    :param url: the url string from each line
    :param topic: a string which is the topic
    :return: None if there is a match, a list of strings for all the matches
    """
    try:
        with urllib.request.urlopen(url) as url_file:
            text = url_file.read().decode('UTF-8')
            text = text.replace(">","> ").replace("<"," <")
            q = re.findall(">[^<]* "+topic+"["+string.punctuation+"]? [^>]*<",
                           text,
                           re.IGNORECASE)
            return q!=None and q or None

    except urllib.error.URLError as url_err:
        print('Error opening url: ', url, url_err)
    except UnicodeDecodeError as decode_err:
        print('Error decoding url: ', url, decode_err)
    return None

def main():

    try:
        file = sys.argv[1]
        topic = sys.argv[2]
        end_file = topic+"summary.txt"
    except IndexError as e:
        print('Error: invalid amount of arguments')
        print('python program.py filename topic')
        sys.exit(1)

    get_urls(file,end_file,topic)


if __name__ == '__main__':
    main()