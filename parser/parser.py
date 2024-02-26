import nltk
import sys

TERMINALS = """
Adj -> "country" | "dreadful" | "enigmatical" | "little" | "moist" | "red"
Adv -> "down" | "here" | "never"
Conj -> "and" | "until"
Det -> "a" | "an" | "his" | "my" | "the"
N -> "armchair" | "companion" | "day" | "door" | "hand" | "he" | "himself"
N -> "holmes" | "home" | "i" | "mess" | "paint" | "palm" | "pipe" | "she"
N -> "smile" | "thursday" | "walk" | "we" | "word"
P -> "at" | "before" | "in" | "of" | "on" | "to"
V -> "arrived" | "came" | "chuckled" | "had" | "lit" | "said" | "sat"
V -> "smiled" | "tell" | "were"
"""

NONTERMINALS = """
S -> NP VP | S Conj S | VP NP

NP -> N | N VP | Det N | NP PP | Det AdjP | NP Adv
VP -> V | V NP | VP PP | Adv VP | VP Adv

PP -> P NP
AdjP -> Adj N | Adj AdjP
"""

grammar = nltk.CFG.fromstring(NONTERMINALS + TERMINALS)
parser = nltk.ChartParser(grammar)


def main():
    # If filename specified, read sentence from file
    if len(sys.argv) == 2:
        with open(sys.argv[1]) as f:
            s = f.read()

    # Otherwise, get sentence as input
    else:
        s = input("Sentence: ")

    # Convert input into list of words
    s = preprocess(s)

    # Attempt to parse sentence
    try:
        trees = list(parser.parse(s))
    except ValueError as e:
        print(e)
        return
    if not trees:
        print("Could not parse sentence.")
        return

    # Print each tree with noun phrase chunks
    for tree in trees:
        tree.pretty_print()

        print("Noun Phrase Chunks")
        for np in np_chunk(tree):
            print(" ".join(np.flatten()))


def preprocess(sentence):
    """
    Convert `sentence` to a list of its words.
    Pre-process sentence by converting all characters to lowercase
    and removing any word that does not contain at least one alphabetic
    character.
    """
    final_list = []

    tokens = nltk.word_tokenize(sentence)

    for token in tokens:
        isValid = False
        for char in token:
            if char.isalpha():
                isValid = True

        if isValid:
            final_list.append(token.lower())

    return final_list


def np_chunk(tree):
    """
    Return a list of all noun phrase chunks in the sentence tree.
    A noun phrase chunk is defined as any subtree of the sentence
    whose label is "NP" that does not itself contain any other
    noun phrases as subtrees.
    """
    np_chunks = []

    tree_climber(tree, np_chunks)

    return np_chunks


def tree_climber(tree, np_chunks):
    for subtree in tree:
        if subtree.label() == "NP" and not has_nounphrases(subtree):
            np_chunks.append(subtree)
        elif len(subtree) > 1:
            tree_climber(subtree, np_chunks)


def has_nounphrases(tree):
    for subtree in tree:
        if isinstance(subtree, nltk.Tree) and subtree.label() == "NP":
            return True
        if isinstance(subtree, nltk.Tree) and has_nounphrases(subtree):
            return True

    return False


if __name__ == "__main__":
    main()