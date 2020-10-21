import logging
import os
from sys import argv, stderr
from typing import Generator, Iterator, List
import gensim.models
from itertools import chain
logging.basicConfig(format='%(asctime)s : %(levelname)s : %(message)s', level=logging.INFO)

class MyCorpus(object):
    """An interator that yields sentences (lists of str)."""

    def __init__(self, corpus_directory: str) -> None:
        self.corpus_directory = corpus_directory

    def __iter__(self) -> Iterator[List[str]]:
        corpus = (os.path.join(self.corpus_directory, file) for file in os.listdir(self.corpus_directory))
        for file in corpus:
            for line in self.__read_lines(file):
                yield line.split()

    def __read_lines(self, path: str) -> Iterator[str]:
        for line in open(path):
            yield line

def main():
    if len(argv) != 2:
        print("Requires one argument: path to corpus directory")
        exit(1)
    corpus = MyCorpus(argv[1])
    
    # print("Reading from stdin", file=stderr)
    # for line in corpus:
    #     print(line)
    
    model = gensim.models.Word2Vec(sentences=list(corpus))

    for i, word in enumerate(model.wv.vocab):
        if i == 10:
            break
        print(word)

if __name__ == "__main__":
    main()