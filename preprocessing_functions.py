#!/usr/bin/env python
# coding: utf-8

# # Pre-processing functions

import re

# -------- TEXT CLEANING --------

# Remove every widespace (\t, \n)
def remove_widespace(text):
    regex = re.compile(r"\s+")
    text = re.sub(regex, " ", text)
    regex = re.compile(r"\s+")
    text = re.sub(regex, " ", text)
    return text

# Remove every strange typo of "nn" form in front of a word
def remove_n(text):
    regex = re.compile(r" nn")
    text = re.sub(regex, "", text)
    return text

# Remove line breaks
def remove_crlf(text):
    regex = re.compile(r"\n|\r")
    text = re.sub(regex, " ", text)
    return text

# -------- PREPROCESSING PIPELINES --------
