#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
File: Main.py
Name: Angel Villalpando
Date: 11/11/2018
Course: CS 2302 - Data Structures
Description: This program provides the load factor and the average number of comparisons for two hash tables created using
a user provided .txt file. The first one uses a hash function that creates a string of the ASCII representation of the word,
casts it as an integer and mods that number by the size of the table. The second converts the words into a base 26 number
using their ASCII value to determine their multiplication value against their respective power of 26.
"""
from HashTable import HashTable
from HashTable2 import HashTable2

anagramCount = 0

def count_anagrams(word, word_list, prefix=""): # this is the modified method that now counts number of anagrams
    global anagramCount
    if len(word) <= 1:
        str = prefix + word

        if word_list.search(str):
            anagramCount += 1
    else:
        for i in range(len(word)):
            curr = word[i: i + 1]
            before = word[0: i]
            after = word[i + 1:]

            if curr not in before:
                count_anagrams(before + after, word_list, prefix + curr)

    return anagramCount


def main():


    while True:
        usr_file  = input("\n\nPlease provide the name of the file that you are using (type <exit> to escape): ")
        if str(usr_file) == "exit" or str(usr_file) == "Exit":
            exit(0)
        usr_size = input("Please provide the size of the file that you are using (type <exit> to exit): ")
        if str(usr_size) == "exit" or str(usr_file) == "Exit":
            exit(0)

        table_size = int(usr_size) * 1.25
        english_words = HashTable(int(table_size)) # Hash table created for the first hash function
        english_words2 = HashTable2(int(table_size)) # Hash table created for the second hash function


        file = open(usr_file, "r")
        for line in file:
            word = line.split('\n')
            english_words.insert(word[0])
            english_words2.insert(word[0])
        file.close()

        print("\nThe load factor is: ", english_words.get_load_factor()) # load factor is the same for both hash functions


        comp_total = english_words.number_comparisons()
        print("\nThe average number of comparisons using Hash Function 1 is %s" % comp_total) ## displays avg comparisons for hash function 1

        comp_total2 = english_words2.number_comparisons()
        print("The average number of comparisons using Hash Function 2 is %s" %comp_total2) ## displays avg comparisons for hash function 2

        usr_word = input("\nPlease provide a word to check for number of Anagrams (type <exit1> to exit): ") # anagram count prompt
        if usr_word == "exit1" or usr_word == "Exit1":
            exit(0)
        anagrams = count_anagrams(str(usr_word), english_words)
        print("The word ", usr_word, "has", anagrams, "Anagram(s).")




main()