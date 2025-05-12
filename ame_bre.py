import re
from collections import Counter
from google.colab import files

print("Upload the American reference word list:")
ame_upload = files.upload()
ame_file = list(ame_upload.keys())[0]

print("Upload the British reference word list:")
bre_upload = files.upload()
bre_file = list(bre_upload.keys())[0]

print("Upload the corpus file to analyze:")
corpus_upload = files.upload()
corpus_file = list(corpus_upload.keys())[0]



def load_wordlist(filename):
    with open(filename, "r", encoding="utf-8") as f:
        return set(word.strip().lower() for word in f if word.strip())

ame_words = load_wordlist(ame_file)
bre_words = load_wordlist(bre_file)



shared_words = ame_words & bre_words
ame_unique = ame_words - shared_words
bre_unique = bre_words - shared_words



ame_suffixes = [r'\b\w+or\b', r'\b\w+ors\b', r'\b\w+ize\b', r'\b\w+izes\b', r'\b\w+ized\b', r'\b\w+yze\b', r'\b\w+yzes\b', r'\b\w+yed\b', r'\b\w+er\b', r'\b\w+ers\b', r'\b\w+ered\b', r'\b\w+ense\b', r'\b\w+og\b', r'\b\w+eled\b']
bre_suffixes = [r'\b\w+our\b', r'\b\w+ours\b', r'\b\w+ise\b', r'\b\w+ises\b', r'\b\w+ises\b', r'\b\w+yse\b', r'\b\w+yses\b', r'\b\w+ysed\b', r'\b\w+re\b', r'\b\w+res\b', r'\b\w+red\b', r'\b\w+ence\b', r'\b\w+ogue\b', r'\b\w+elled\b']



with open(corpus_file, "r", encoding="utf-8") as f:
    text = f.read().lower()
    corpus_words = re.findall(r'\b\w+\b', text)

total_words = len(corpus_words)
print(f"Total words in uploaded file: {total_words}")



def matches_suffix(word, suffixes):
    """Checks if a word matches any of the given suffix patterns."""
    for suffix in suffixes:
        if re.search(suffix, word):
            return True
    return False



suffix_pairs = {
    "or": "our",
    "ors": "ors",
    "ize": "ise",
    "izes": "ises",
    "ized": "ised",
    "yze": "yse",
    "yzes": "yses",
    "yzed": "ysed",
    "er": "re",
    "ers": "res",
    "ered": "red",
    "ense": "ence",
    "og": "ogue",
    "eled": "elled"
}

def has_variant_in_other_list(word, own_suffixes, other_list, mapping):
    for ame_suf, bre_suf in mapping.items():
        if word.endswith(ame_suf):
            alt_form = word[:-len(ame_suf)] + bre_suf
            if alt_form in other_list:
                return True
    return False



ame_count = Counter()
bre_count = Counter()

reversed_suffix_pairs = {v: k for k, v in suffix_pairs.items()}

for word in corpus_words:

    if word in ame_unique and matches_suffix(word, ame_suffixes):
        if has_variant_in_other_list(word, ame_suffixes, bre_words, suffix_pairs):
            ame_count[word] += 1

    elif word in bre_unique and matches_suffix(word, bre_suffixes):
        if has_variant_in_other_list(word, bre_suffixes, ame_words, reversed_suffix_pairs):
            bre_count[word] += 1

print(f"\nUnique American words found: {sum(ame_count.values())}")
print(dict(ame_count))

print(f"\nUnique British words found: {sum(bre_count.values())}")
print(dict(bre_count))
