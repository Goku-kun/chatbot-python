# Custom Text Pre-Processor Module

This module can perform following tasks:
1. Noise Removal (Anything that is not [A-Za-z0-9_] will be replaced with space)
2. Word Tokenization
3. Removal of Stop Words part of nltk module in python
4. Stemming of the words
5. Lemmatization of the words
6. Measure the Levenshtein Distance.

## How to use:

1. There are two use cases of this module:
  * Pre processed text shall return tokens after removing stop words
  * Pre processed shall also perform stemming and lemmatization after stop word removal.
2. The code shall work as follows:
  * `from textprep.py import text_preprocessor`
  * `# The function takes two arguments. First is the text that you wish to pre process and second is case which is an optional argument whose default value is 0. If the case is 0, the function shall only return text after tokenization and removing noise and stop words. If the case is 1, the function shall stem and lemmatize the text and then return the processed text.`
  * `list_tokens = text_preprocessor(text, 0)`
  * `list_tokens = text_preprocessor(text, 1)` 
