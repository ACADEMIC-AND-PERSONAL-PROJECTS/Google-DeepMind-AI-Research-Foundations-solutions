import re

class SimpleWordTokenizer:

    # Initializes the tokenizer with texts in corpus or with a vocabulary
    def __init__(self, corpus: list[str], vocabulary: list[str] | None = None):

        # If there isn't a vocabulary, we need to build one based on the given corpus
        if vocabulary is None:
            if isinstance(corpus, str):
                corpus = [corpus]

            # Transform the corpus into tokens
            tokens = []
            for text in corpus:
                tokens_text = self.space_tokenize(text)
                for token in tokens_text:
                    tokens.append(token)

            # Retrieve the vocabulary
            self.vocabulary = self.build_vocabulary(tokens)

        # If there is a given vocabulary then just use it
        self.vocabulary = vocabulary

        # Size of the vocabulary
        self.vocabulary_size = len(self.vocabulary)

        # Create token_to_index & index_to_token
        self.token_to_index = {}
        self.index_to_token = {}

        # Loop in order to map a token to an index and vice versa
        for index, token in enumerate(self.vocabulary):
            self.token_to_index[token] = index
            self.index_to_token[index] = token

    # Vocabulary builder util
    def build_vocabulary(self, tokens: list[str]) -> list[str]:
        return list(set(tokens))

    # Space tokenize util
    def space_tokenize(self, text: str) -> list[str]:
        return re.split(r" +", text)

    # Join text util
    def join(self, text_list: list[str]) -> str:
        return " ".join(text_list)

    # Encoder - Given a text it will return a list of number
    def encode(self, text: str) -> list[int]:
        vector = []

        # Retrieve the tokens in the text
        for token in self.space_tokenize(text):
            vector.append(self.token_to_index[token])

        return vector

    # Decoder - Given a vector of number, it will return
    def decode(self, vector: list[int]) -> str:
        # If a single integer is passed, convert that into a list
        if isinstance(vector, int):
            vector = [vector]

        # Retrieve tokens corresponding to the token IDs
        tokens = []
        for scalar in vector:
            tokens.append(self.index_to_token[scalar])

        return self.join(tokens)