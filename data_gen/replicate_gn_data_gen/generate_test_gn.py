from pathlib import Path
from collections import Counter
import random
from tqdm import tqdm
import argparse
random.seed(42)
parser = argparse.ArgumentParser(description='the script generates the dependency test examples reported in Getz & Newport (2019) ')
parser.add_argument('grammar_name', help='the name of the grammar')
args = parser.parse_args()
grammar_name = args.grammar_name
vocaba = Path(f'vocab/{grammar_name}_vocaba.txt').read_text().strip().split('\n')
vocab_open = Path(f'vocab/{grammar_name}_vocaby.txt').read_text().strip().split('\n')
vocab_close = ['a', 'the', 'one', 'my', 'your', 'this', 'an', 'her', 'his', 'dank']
vocab_close_longer = ['institutionalise', 'internationalise', 'black-and-white', 'well-documented', 'intellectualise',
                    'departmentalise', 'inconsequential', 'impressionable', 'counterbalance', 'happy-go-lucky']

def get_bigrams(sents):
    bigrams = [b for l in sents for b in zip(l.split(" ")[0:-1], l.split(" ")[1:])]
    bigram_perm = ['_'.join(list(x)) for x in bigrams]
    return bigram_perm

def get_freq(bigrams, vocabx, vocaby):
    if 'exp3' in grammar_name:
        bigram_inverse, bigram_noinverse = bigrams
        freqax = [(x, Counter(bigram_inverse)[x]) for x in bigram_inverse if x.split('_')[0] in vocaba and x.split('_')[1] in vocabx]
        freqay = [(x, Counter(bigram_noinverse)[x]) for x in bigram_noinverse if x.split('_')[0] in vocaba and x.split('_')[1] in vocaby]
    else:
        freqax = [(x, Counter(bigrams)[x]) for x in bigrams if x.split('_')[0] in vocaba and x.split('_')[1] in vocabx]
        freqay = [(x, Counter(bigrams)[x]) for x in bigrams if x.split('_')[0] in vocaba and x.split('_')[1] in vocaby]
    sorted_freqax ={}
    sorted_freqay = {}
    for word, freq in freqax:
        if word.split('_')[0] not in sorted_freqax:
            sorted_freqax[word.split('_')[0]] = {freq: [word]}
        else:
            if freq in sorted_freqax[word.split('_')[0]]:
                sorted_freqax[word.split('_')[0]][freq].append(word)
            else:
                sorted_freqax[word.split('_')[0]][freq] = [word]
    for wordy, freqy in freqay:
        if wordy.split('_')[0] not in sorted_freqay:
            sorted_freqay[wordy.split('_')[0]] = {freqy: [wordy]}
        else:
            if freqy not in sorted_freqay[wordy.split('_')[0]]:
                sorted_freqay[wordy.split('_')[0]][freqy] = [wordy]
            else:
                sorted_freqay[wordy.split('_')[0]][freqy].append(wordy)
    return set(sorted_freqay.keys())&set(sorted_freqax.keys()), sorted_freqax, sorted_freqay

def get_overlap(overlap_keys, sorted_x, sorted_y):
    correct=[]
    incorrect =[]
    for k in overlap_keys:
        overlap_freq = list(set(sorted_x[k].keys())&set(sorted_y[k].keys()))
        for overlap_f in overlap_freq:
            x = list(set(sorted_x[k][overlap_f]))
            y = list(set(sorted_y[k][overlap_f]))
            to_pic_num = min(len(x), len(y))
            correct.extend(random.sample(x, to_pic_num))
            incorrect.extend(random.sample(y, to_pic_num))
    return correct, incorrect

def write_test_examples(grammar_folder,permutation=False):
    for i in tqdm(range(10)):
        with open(f'{grammar_folder}/correct_{str(i)}.tst', 'w') as c, open(f'{grammar_folder}/incorrect_{str(i)}.tst', 'w') as inc:
            if 'exp3' in grammar_name:
                sents_inverse = Path(f'{grammar_folder}/inverse{str(i)}.trn').read_text().strip().split('\n')
                sents = Path(f'{grammar_folder}/{str(i)}.trn').read_text().strip().split('\n')
                bigrams = (get_bigrams(sents_inverse),get_bigrams(sents))
            else:
                sents = Path(f'{grammar_folder}/{str(i)}.trn').read_text().strip().split('\n')
                bigrams = get_bigrams(sents)
            if 'exp1' in grammar_folder or 'exp3' in grammar_folder:
                vocab_close_class = vocab_close
            elif 'exp2' in grammar_folder:
                vocab_close_class = vocab_close_longer
            else:
                raise ValueError('The grammar name is not recognized!')
            vocab_open_class = vocab_open

            if permutation:
                overlap, sorted_x, sorted_y = get_freq(bigrams, vocab_open_class, vocab_close_class)
            else:
                overlap, sorted_x, sorted_y = get_freq(bigrams, vocab_close_class, vocab_open_class)
            # if permutation:
            #     correct, incorrect = get_overlap(overlap, sorted_x, sorted_y)
            # else:
            incorrect, correct = get_overlap(overlap, sorted_x, sorted_y)
            # random.shuffle(correct)
            # random.shuffle(incorrect)
            to_write_c = '\n'.join([' '.join(y.split('_')) for y in correct])
            to_write_inc = '\n'.join([' '.join(y.split('_')) for y in incorrect])
            c.write(f'{to_write_c}')
            inc.write(f'{to_write_inc}')



grammar_folder = f'data_gen/grammar/{grammar_name}/{grammar_name}'
grammar_folder_permute = f'data_gen/grammar/{grammar_name}_permutation/{grammar_name}_permutation'
write_test_examples(grammar_folder, False)
write_test_examples(grammar_folder_permute, True)



