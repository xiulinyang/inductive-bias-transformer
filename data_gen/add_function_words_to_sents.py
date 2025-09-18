'''
This script will add more function words to the function word category.
'''

from pathlib import Path
import random
import os
import argparse
from func_words import FUNC_WORDS

# def(children, flip_id, grammar_key):
def permutation_add_funcs(children, flip_id, grammar):
    children_updated = []

    if children:
        if len(children) == 2:
            # if the constituent contains a function word and its corresponding content word related phrase,
            # we simply reverse the order.
            key = list(FUNC_WORDS[grammar][flip_id].keys())[0]
            value = random.choice(FUNC_WORDS[grammar][flip_id][key])
            children[0][2] = value
            for child in children:
                children_updated += child

        else:
            # Otherwise,
            for child in children:
                children_updated += child
    return children_updated

def add_func_words_children(sentence_part, flip_id, grammar):
    children = []
    bracket_stack = []
    L_brack = '('
    R_brack = ')'
    children_end = -1
    for i in range(len(sentence_part)):
        s = sentence_part[i]
        if s == L_brack:
            bracket_stack.append((L_brack, i))
        elif s == R_brack:
            if len(bracket_stack) > 0:
                if bracket_stack[-1][0] == L_brack:
                    opening = bracket_stack.pop()
                    if len(bracket_stack) == 0:
                        children.append(sentence_part[opening[1]:i+1])
            else:
                children_end = i - 1
                break
        else:
            continue

    children_updated = permutation_add_funcs(children, flip_id, grammar)
    return children_updated + sentence_part[children_end:]

def flip_as_needed(sentence, grammar):
    to_flip = {1, 2, 3, 4}
    s_split = sentence.strip().split()
    j = 0
    while j < len(s_split):
        tok = s_split[j]
        if tok and tok[0].isdigit():
            pid = int(tok[0])
            if pid in to_flip:
                tail_start = j + 1
                if tail_start < len(s_split):
                    new_tail = add_func_words_children(s_split[tail_start:], pid, grammar)
                    s_split = s_split[:tail_start] + new_tail
                    j = tail_start
                    continue
                else:
                    break
        j += 1
    return ' '.join(s_split)

def remove_bracketing(s):
    new_s = []
    split_s = s.split()
    i = 0
    while i < len(split_s):
        if split_s[i] == ")":
            i += 1
        elif split_s[i] == "(":
            i += 2
        else:
            new_s.append(split_s[i])
            i += 1
    return ' '.join(new_s).strip()

def generate_sentence_file(sentences, data_root, grammar):
    output_f = open(f'{data_root}/{grammar}.txt', 'w')
    output_f_b = open(f'{data_root}/{grammar}_b.txt', 'w')
    for s in sentences:
        # print(s)
        # print(remove_bracketing(flip_as_needed(s, grammar, exp)))
        output_f.write(remove_bracketing(flip_as_needed(s, grammar)) + "\n")
        output_f_b.write(flip_as_needed(s, grammar) + "\n")
    output_f.close()



if __name__ == '__main__':

    parser = argparse.ArgumentParser(description="Generate variants of sentences"
        " based on base grammar")

    parser.add_argument("-s", "--sentence_file", type=str, required=True,
        help="Path to base sentence file")

    parser.add_argument("-g", "--grammar_name", type=str, required=True,
        help="Location of output folder")

    args = parser.parse_args()


    sentences = Path(args.sentence_file).read_text().strip().split('\n')
    grammar_name = args.grammar_name
    data_root = f'data_gen/grammar/{grammar_name}'
    os.makedirs(data_root, exist_ok=True)
    if grammar_name not in {'grammar_close_then_open_30',
                            'grammar_close_then_open_50',
                            'grammar_close_then_open_60'}:
        raise Exception("Unknown grammar name")
    generate_sentence_file(sentences, data_root, grammar_name)