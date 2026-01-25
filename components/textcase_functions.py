'''
Text Converter - 
lightweight module for converting strings
'''
import textcase


def request_upper_case(var):
    '''Turns string into uppercase letters'''
    converted_arg = textcase.upper(var)
    return converted_arg

def request_lower_case(var):
    '''Turns string into lowercase letters'''
    converted_arg = textcase.lower(var)
    return converted_arg

def request_title_case(var):
    '''
    Turns string into title case letters
    '''
    converted_arg = textcase.title(var)
    return converted_arg

def request_sentence_case(var):
    '''
    Turns string into sentence case letters
    '''
    converted_arg = textcase.sentence(var)
    return converted_arg
