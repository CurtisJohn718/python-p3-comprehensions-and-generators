#!/usr/bin/env python3

def return_evens(num_list):
    # using a list comprehension write a function return_evens()
    # return a list of all the even elements of a sequence of integers.
    # [expression for item in sequence if condition]
    return [num for num in num_list if num % 2 == 0]
     

def make_exclamation(sentence_list):
    # using a list comprehension write a function make_exclamation()
    # takes a list of sentence strings and returns a list of sentence strings with exclamation marks at the end.
    return [string + "!" for string in sentence_list]