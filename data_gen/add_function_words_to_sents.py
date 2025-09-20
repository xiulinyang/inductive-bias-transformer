'''
This script will add more function words to the function word category.
'''

from pathlib import Path
import random
import os
import argparse
from func_words import FUNC_WORDS

def permutation_add_funcs(children, flip_id, grammar, reverse, random_func=False):
    children_updated = []

    if children:
        if len(children) == 2:
            # if the constituent contains a function word and its corresponding content word related phrase,
            # we simply reverse the order.
            if random_func:
                fid = random.choice([2,3,4]) # randomly select a group of function words
                key = list(FUNC_WORDS[grammar][fid].keys())[0] # get the function word name
                value = random.choice(FUNC_WORDS[grammar][fid][key]) # randomly select a word from that group
            else:
                key = list(FUNC_WORDS[grammar][flip_id].keys())[0]
                value = random.choice(FUNC_WORDS[grammar][flip_id][key])

            if reverse:
                children[1][2] = value
            else:
                children[0][2] = value
            for child in children:
                children_updated += child

        else:
            # Otherwise,
            for child in children:
                children_updated += child
    return children_updated

def add_func_words_children(sentence_part, flip_id, grammar, reverse, rand_fun=False):
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

    children_updated = permutation_add_funcs(children, flip_id, grammar, reverse, rand_fun)
    return children_updated + sentence_part[children_end:]

def flip_as_needed(sentence, grammar, reverse, rand_fun=False):
    to_flip = {2, 3, 4}
    s_split = sentence.strip().split()
    j = 0
    while j < len(s_split):
        tok = s_split[j]
        if tok and tok[0].isdigit():
            pid = int(tok[0])
            if pid in to_flip:
                tail_start = j + 1
                if tail_start < len(s_split):
                    new_tail = add_func_words_children(s_split[tail_start:], pid, grammar, reverse, rand_fun)
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

def generate_sentence_file(sentences, data_root, grammar, reverse, rand_fun):
    if rand_fun:
        output_f = open(f'{data_root}/{grammar}_r.txt', 'w')
        output_f_b = open(f'{data_root}/{grammar}_r_b.txt', 'w')
    else:
        output_f = open(f'{data_root}/{grammar}.txt', 'w')
        output_f_b = open(f'{data_root}/{grammar}_b.txt', 'w')
    for s in sentences:
        output_f.write(remove_bracketing(flip_as_needed(s, grammar, reverse, rand_fun)) + "\n")
        output_f_b.write(flip_as_needed(s, grammar, reverse,  rand_fun) + "\n")
    output_f.close()



if __name__ == '__main__':

    parser = argparse.ArgumentParser(description="Generate variants of sentences"
        " based on base grammar")

    parser.add_argument("-s", "--sentence_file", type=str, required=True,
        help="Path to base sentence file")

    parser.add_argument("-g", "--grammar_name", type=str, required=True,
        help="grammar name to decide the number of function words")

    parser.add_argument("-r", "--random_function", action= "store_true",
                        help="whether to randomly sample from all function words of the language or not")

    parser.add_argument("-rv", "--reverse", action="store_true",
                        help="whether to randomly sample from all function words of the language or not")

    args = parser.parse_args()


    sentences = Path(args.sentence_file).read_text().strip().split('\n')
    grammar_name = args.grammar_name
    reverse = args.reverse
    if args.random_function:
        data_root = f'grammar/{grammar_name}_r'
    else:
        data_root = f'grammar/{grammar_name}'
    os.makedirs(data_root, exist_ok=True)
    rand_fun = args.random_function

    if grammar_name not in {'grammar_close_then_open_3',
                            'grammar_close_then_open_30',
                            'grammar_close_then_open_50',
                            'grammar_close_then_open_60',
                            'grammar_close_then_open_3_reverse',
                            'grammar_close_then_open_30_reverse',
                            'grammar_close_then_open_50_reverse',
                            'grammar_close_then_open_60_reverse'
                            }:
        raise Exception("Unknown grammar name")
    print('grammar & function words')
    print(grammar_name)
    for i in [2,3,4]:
        for k, vs in FUNC_WORDS[grammar_name][i].items():
            for v in vs:
                print(f'1\t{k}\t{v}')
    generate_sentence_file(sentences, data_root, grammar_name, reverse, rand_fun)