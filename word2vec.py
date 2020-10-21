import logging
import os
from sys import stderr, stdin
from typing import Callable, Iterator, List, Optional
from gensim import utils
logging.basicConfig(format='%(asctime)s : %(levelname)s : %(message)s', level=logging.INFO)

class MyCorpus(object):
    """An interator that yields sentences (lists of str)."""

    def _corpus_stream(self) -> Iterator[str]:
        """Iterates over lines

        Yields:
            Iterator[str]: Line in the corpus
        """
        if self.from_stdin:
            for line in stdin:
                yield line
        else:
            for file in os.listdir(self.corpus_directory):
                for line in open(file):
                    yield line

    def __init__(self, from_stdin: bool = True, corpus_directory: str = None) -> None:
        self.from_stdin = True
        self.corpus_directory = corpus_directory

    def __iter__(self) -> Iterator[List[str]]:
        """Iterator implementation

        Yields:
            List[str]: List of string tokens, preprocessed
        """
        for line in self._corpus_stream():
            # preprocess, if any
            yield line.split()

def main():
    corpus = MyCorpus()
    print("Reading from stdin", file=stderr)
    for line in corpus:
        print(line)

if __name__ == "__main__":
    main()