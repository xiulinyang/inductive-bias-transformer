import argparse
import os
import sys
import random
import copy
from pathlib import Path
from func_words import FUNC_WORDS

PATTERN_IDX = {
    1 : ['Comp'],
    2 : ['Vaff'],
    3 : ['Det'],
    4 : ['Prep'],
}

def get_function_words(num):
    num -=3
    dets = [x.split()[-1] for x in Path('english/dets.txt').read_text().strip().split('\n')][:num]
    comps = [x.split()[-1] for x in Path('english/comps.txt').read_text().strip().split('\n')][:num]
    preps = [x.split()[-1] for x in Path('english/prep.txt').read_text().strip().split('\n')][:num]
    return dets, comps, preps

def permutation_exp1(children, flip_id, grammar):
    children_updated = []

    if children:
        if len(children) != 1:
            # if the constituent contains a function word and its corresponding content word related phrase,
            # we simply reverse the order.
            for child in children[::-1]:
                children_updated += child

        else:
            # Otherwise,
            for child in children:
                print(child)
                assert len(children)==1
                # if the constituent contains only phrase without the function word,
                # we replace that content word with corresponding function words.
                key = list(FUNC_WORDS[grammar][flip_id].keys())[0]
                value = random.choice(FUNC_WORDS[grammar][flip_id][key])

                new_child = ['(', key, value, ')']
                children_updated += new_child
    return children_updated


# def permutation_exp2(children, flip_id):
#     children_updated = []
#     for child in children[::-1]:
#         children_updated += child
#     return children_updated

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
                    new_tail = reversed_children(s_split[tail_start:], pid, grammar)
                    s_split = s_split[:tail_start] + new_tail
                    j = tail_start
                    continue
                else:
                    break
        j += 1
    return ' '.join(s_split)

def check_x(pattern_id, child):
    # check if the category we need to manipulate or not
    overlap = [x for x in PATTERN_IDX[pattern_id] if x in child]
    return overlap

def reversed_children(sentence_part, flip_id, grammar):
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

    children_updated = permutation_exp1(children, flip_id, grammar)
    # elif exp=='rev':
    #     children_updated = permutation_exp2(children, flip_id)
    # else:
    #     raise ValueError('The permutation is not supported!')
    return children_updated + sentence_part[children_end:]

def remove_bracketing(s):
    new_s = []
    split_s = s.split(" ")
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

def generate_sentence_file(sentences, output_file, grammar):
    output_f = open(output_file, 'w')
    for s in sentences:
        # print(s)
        # print(remove_bracketing(flip_as_needed(s, grammar, exp)))
        output_f.write(remove_bracketing(flip_as_needed(s, grammar)) + "\n")
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
    root_dir = f'data_gen/grammar/{grammar_name}_permutation/'
    os.makedirs(root_dir, exist_ok=True)
    output_file = f'{root_dir}/{grammar_name}_permutation.txt'
    if grammar_name not in {'grammar_close_then_open',
                            'grammar_close_then_open_30',
                            'grammar_close_then_open_50',
                            'grammar_close_then_open_60'}:
        raise Exception("Unknown grammar name")
    generate_sentence_file(sentences, output_file, grammar_name)


