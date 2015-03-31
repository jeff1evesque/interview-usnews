#!/usr/bin/python

## @validate_input.py
#  This file validates the 'word', and 'max_value' parameters supplied in
#      the 'GET' request.

## Class: Validate_Input, explicitly inherit 'new-style' clalss.
class Validate_Input(object):

    ## constructor
    def __init__(self, word, max_value):
        self.word_choice = ['fizz', 'buzz', 'fizzbuzz']
        self.word        = word
        self.max_value   = max_value
        self.status      = True
        self.list_error  = []

    ## validate: validates the 'word', and 'max_value' arguments
    def validate(self):
        if self.word not in self.word_choice:
            self.list_error.append(self.word + ' must be one of ' + ', '.join(self.word_choice))
            self.status = False
        try:
            self.max_value = int(self.max_value)

            if self.max_value < 1:
                self.list_error.append(str(self.max_value) + ' must be greater than 0')
                self.status = False

        except Exception as error:
            self.list_error.append(str(self.max_value) + ' must be an integer value')
            self.status = False

    ## get_status: returns True if validation succeeded
    def get_status(self):
        return self.status

    ## get_error: return current error(s)
    def get_error(self):
        return self.list_error
