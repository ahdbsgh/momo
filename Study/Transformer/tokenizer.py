import spacy


class Tokenizer:

    def __init__(self):
        self.spacy_de = spacy.load('de')
        self.spacy_en = spacy.load('en')

    def tokenize_de(self, text):
        """
        Tokenizes German text from a string into a list of strings
        """
        return [tok.text for tok in self.spacy_de.tokenizer(text)]

    def tokenize_en(self, text):
        """
        Tokenizes English text from a string into a list of strings
        """
        return [tok.text for tok in self.spacy_en.tokenizer(text)]
