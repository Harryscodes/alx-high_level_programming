#!/usr/bin/python3

""" module that houses a function that prints text with 2 lines after any of these characters (.,?,:) """

def text_indentation(text):
    """ function that prints text with 2 lines after any of these characters (.,?,:) """
    if not isinstance(text,str):
        raise TypeError ("text must be a string")
    text = text.strip()
    tokenizer = ('.', '?', ':')
    text_to_print = ''
    for i in range(len(text)):
        if text[i] in tokenizer:
            text_to_print += text[i]
            text_to_print = text_to_print.strip()
            print('{}\n'.format(text_to_print))
            text_to_print = ''
        elif text[i] not in tokenizer:
            text_to_print += text[i]
    print('{}'.format(text_to_print.strip()))
