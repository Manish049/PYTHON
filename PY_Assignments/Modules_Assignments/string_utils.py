# string_utils.py - String Utility Module

def capitalize_words(text):
    """Returns string with each word capitalized"""
    return ' '.join(word.capitalize() for word in text.split())

def reverse_string(text):
    """Returns reversed string"""
    return text[::-1]

def word_count(text):
    """Returns number of words in the text"""
    return len(text.split())
