"""Word Finder: finds random words from a dictionary."""

import random


class WordFinder:
    """Class to create a list from a given text file. Has random word functionality built in

    >>> f = WordFinder('simple.txt')
    3 words read

    >>> f.random() in ["cat", "dog", "porcupine"]
    True

    >>> f.random() in ["cat", "dog", "porcupine"]
    True

    >>> f.random() in ["cat", "dog", "porcupine"]
    True
    """

    def __init__(self, file):
        self.file = file
        self.words_list = self.make_words_list()
        print(f"{len(self.words_list)} words read")

    def random(self):
        return random.choice(self.words_list)

    def make_words_list(self):
        with open(self.file, "r") as f:
            return [line.rstrip() for line in f]


class SpecialWordFinder(WordFinder):
    """Specialized WordFinder that excludes blank lines/ comments.

    >>> swf = SpecialWordFinder("complex.txt")
    3 words read

    >>> swf.random() in ["pear", "carrot", "kale"]
    True

    >>> swf.random() in ["pear", "carrot", "kale"]
    True

    >>> swf.random() in ["pear", "carrot", "kale"]
    True
    """
    
    def make_words_list(self):
        with open(self.file, "r") as f:
            return [line.strip() for line in f if line.strip() and not line.startswith('#')]
