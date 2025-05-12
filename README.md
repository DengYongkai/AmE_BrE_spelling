# AmE_BrE_spelling

## British-American English Variant Analyzer

This script analyzes a text corpus for British vs. American spelling preferences using suffix-based pattern recognition and lexicon comparison. It's especially useful for linguistic analysis, editing, and stylistic consistency in writing.

## 🧠 What It Does

Compares the corpus against two separate reference wordlists:

* American English (e.g. from Webster’s)

* British English (e.g. from the King James Bible)

Detects words that are unique to either variety based on typical suffix patterns (e.g., -ize vs -ise, -or vs -our, etc.).

Attempts cross-variety normalization by switching suffixes and checking whether the modified form exists in the opposite wordlist.

## 📁 Input Files

You will be prompted to upload three files:

* american_words.txt — a list of American English words (lowercased, one per line)

* british_words.txt — a list of British English words (lowercased, one per line)

* corpus.txt — the text corpus you want to analyze

## ⚙️ How It Works

* Loads all three files into memory.

* Identifies words unique to each variety (words not shared between the two lexicons).

* Searches the corpus for these unique words.

* Applies a set of predefined suffix rules to detect spelling variants.

* For each matched word, attempts to create a variant spelling by switching the suffix, and checks if the variant is valid in the opposite lexicon.

* Counts and reports the validated unique words for each variety.

## 🧾 Output

At the end, you'll see:

✅ Unique American words found: Total count + a dictionary of words and their frequencies.

✅ Unique British words found: Total count + a dictionary of words and their frequencies.

Example:

```
Unique American words found: 3
{'organize': 2, 'authorize': 1, 'analyze': 1}

Unique British words found: 2
{'organise': 3, 'colour': 1}
```

## 🧪 Requirements

* Python 3 (tested in Google Colab)

* Basic text files for input

* Standard libraries: re, collections, google.colab.files

## 📌 Notes

* All input words are converted to lowercase for consistent matching.

* Corpus is tokenized using basic regex (\b\w+\b).

* You can easily customize or expand the suffix lists and mappings in the code.
