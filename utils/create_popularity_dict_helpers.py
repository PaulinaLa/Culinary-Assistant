import json
import re
from collections import defaultdict
from typing import DefaultDict, List


def tokenize(line: str) -> List[str]:
    """ "Take line of text and leave just words. Get rid of special signs."""
    text = line.lower()
    pattern = r"\s*\w*\s*"
    return list(filter(None, re.findall(pattern, text)))


def create_popular_words_dictionary(
    corpus_file_name: str, popularity_dict_path: str
) -> None:
    """Search corpora to find popular words and then create a dictionary of them.

    The commented code can be used to create a dictionary that keeps track of indexes
    of lines that contain popular word.

    For corpora we used polish corpora from open subtitles.
    """
    popularity_dict: DefaultDict[str, int] = defaultdict(int)
    # indexes_dict: DefaultDict[str, List] = defaultdict(list)
    with open(corpus_file_name, "r", encoding="utf8") as corpus:
        for line in corpus:
            line = line.rstrip()
            for word in tokenize(line):
                word = word.strip()
                popularity_dict[word] += 1
                # indexes_dict[word] += [index]

    sorted_dict = {
        k: v for k, v in sorted(popularity_dict.items(), key=lambda item: item[1])
    }
    with open(popularity_dict_path, "w", encoding="utf-8") as f:
        json.dump(sorted_dict, f, ensure_ascii=False)

    # with open(indexes_dict_path, "w", encoding="utf-8") as g:
    #     json.dump(indexes_dict, g, ensure_ascii=False)


create_popular_words_dictionary("pl_tok_sieved.txt", "popularity.json")
