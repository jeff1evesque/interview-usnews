#!/usr/bin/python

## @calculate_result.py
#  This file contains methods required to perform the applications calculations.

## Class: Calculate_Result, explicitly inherit 'new-style' clalss.
class Calculate_Result(object):

    ## constructor
    def __init__(self, word, max_value):
        self.word       = word
        self.max_value  = int(max_value)
        self.result     = []
        self.list_error = []

    ## calculate: compute result
    def calculate(self):
        # local variable
        list_integers = range(0, self.max_value+1)

        # build list of integers divisible by 3
        if self.word == 'fizz':
            for x in list_integers:
                if x%3 == 0: self.result.append(x)
        # build list of integers divisible by 5
        elif self.word == 'buzz':
            for x in list_integers:
                if x%5 == 0: self.result.append(x)
        # build list of integers divisible by 3 and 5
        elif self.word == 'fizzbuzz':
            for x in list_integers:
                if x%3 == 0: self.result.append(x)
                elif x%5 == 0: self.result.append(x)
        # error edge case
        else:
            self.result = None
            self.list_error.append('\'calculate()\' could not compute using \'max_value\': ' + str(self.max_value))        

    ## get_errors: get current error(s)
    def get_error(self):
        return self.list_error

    ## get_result: return computed result
    def get_result(self):
        return self.result
