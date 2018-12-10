#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Crossword Solver Program"""

__author__ = "bomazani"

import re


def find_options(words, test_word):
    """ search dict for matching words """
    options = []
    reg_word = test_word.replace(' ', '.')
    for word in words:
        if len(test_word) == len(word) and re.match(reg_word, word):
            options.append(word)
    return options


def main():
    """ take user input, find matches in dictionary """
    with open('dictionary.txt') as f:
        words = f.read().split()

    test_word = raw_input(
        'Please enter a word to solve.\n'
        'Use spaces to signify unknown letters: ').lower()

    print("\n".join(find_options(words, test_word)))


if __name__ == '__main__':
    main()
