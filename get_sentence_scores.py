import argparse
import os
from collections import Counter
def total_sentence_score(words):
    score = 0
    text =[]
    text_decode = ''
    words_text = words[:-2]
    for w in words:
        score += float(w.split()[1].strip()[1:])
    for w in words_text:
        word = w.split()[0]
        text.append(word)
        text_decode+=word
    text_decode = text_decode.replace('▁',' ')
    return score, ' '.join(text), text_decode.strip()

parser = argparse.ArgumentParser(
    description = "Get sentence scores from eval output file")

parser.add_argument("-i", "--input_file", type=str, required=True,
    help="Path to input file")

parser.add_argument("-O", "--output_folder", type=str, required=True,
    help="Location of output folder")

args = parser.parse_args()

if not os.path.exists(args.output_folder):
    os.mkdir(args.output_folder)

file = open(args.input_file, 'r')
all_lines = file.readlines()

all_lines = [l for l in all_lines if len(l.split('|')) > 3]
word_score_lines = [l.split('|')[3][1:] for l in all_lines if l.split(
    '|')[3].split(' ')[1].isnumeric()]

word_score_lines.sort(key=lambda a:int(a.split(' ')[0]))

full_text = ""
for line in word_score_lines:
    full_text += ' '.join(line.split(' ')[1:]).strip('\n') + " "

sentences = []
start = 0
words = full_text.split(']')

for i in range(len(words)):
    if words[i].strip().split(' ')[0].strip() == "</s>":
        sentences.append(words[start:i+1])
        start = i+1
    else:
        if '</s>' in words[i]:
            raise Exception('It seems that the sentence is not well seperated.')
sentence_scores = []
sentence_seq = []
sentence_toks = []
for s in sentences:
    score, tokens, text = total_sentence_score(s)
    sentence_scores.append(score)
    sentence_toks.append(tokens)
    sentence_seq.append(text)
grammar, split, dev_test, _ = args.input_file.split("/")[-1].split(".")
if not os.path.exists(os.path.join(args.output_folder, grammar)):
    os.mkdir(os.path.join(args.output_folder, grammar))

output_path = os.path.join(args.output_folder, grammar, ".".join([split, dev_test, "txt"]))
output_file = open(output_path, 'w')
print(f'Successfully saved the results to {output_path}')
for s, tok, sent in zip(sentence_scores, sentence_toks,sentence_seq):
    # if '</s>' in t:
    #     continue
    output_file.write(sent+'\t'+tok +'\t'+str(s) + "\n")
