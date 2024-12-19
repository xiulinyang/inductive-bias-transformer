from pathlib import Path
from collections import Counter
import random
from tqdm import tqdm

vocaba = Path('vocab/fakegrammarexp2_vocaba.txt').read_text().strip().split('\n')
vocab_open_exp1 = Path('vocab/fakegrammarexp1_vocaby.txt').read_text().strip().split('\n')
vocab_open_exp2 = Path('vocab/fakegrammarexp2_vocaby.txt').read_text().strip().split('\n')
vocab_open_exp3 = Path('vocab/fakegrammarexp3_vocaby.txt').read_text().strip().split('\n')

vocab_close = ['a', 'the', 'one', 'my', 'your', 'this', 'an', 'her', 'his', 'dank']
vocab_close_longer = Path('vocab/fakegrammarexp2_vocab_close.txt').read_text().strip().split('\n')

def get_bigrams(sents):
    bigrams = [b for l in sents for b in zip(l.split(" ")[0:-1], l.split(" ")[1:])]
    bigram_perm = ['_'.join(list(x)) for x in bigrams]
    return bigram_perm

def get_freq(bigrams, vocabx, vocaby):
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
    # print(sorted_freqax)
    # print(sorted_freqay)
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

def write_test_examples(grammar_folder, permutation=False):
    for i in tqdm(range(10)):
        with open(f'{grammar_folder}/correct_{str(i)}.tst', 'w') as c, open(f'{grammar_folder}/incorrect_{str(i)}.tst', 'w') as inc:
            sents = Path(f'{grammar_folder}/{str(i)}.trn').read_text().strip().split('\n')
            bigrams = get_bigrams(sents)
            # bigrams_inverse = get_bigrams(sents_inverse)
            if 'exp1' in grammar_folder:
                vocab_close_class = vocab_close
                vocab_open_class = vocab_open_exp1
            elif 'exp2' in grammar_folder:
                vocab_close_class = vocab_close_longer
                vocab_open_class = vocab_open_exp2
            elif 'exp3' in grammar_folder:
                vocab_close_class = vocab_close
                vocab_open_class = vocab_open_exp3

            if permutation:
                overlap, sorted_x, sorted_y = get_freq(bigrams, vocab_open_class, vocab_close_class)
            else:
                overlap, sorted_x, sorted_y = get_freq(bigrams, vocab_close_class, vocab_open_class)

            correct, incorrect = get_overlap(overlap, sorted_x, sorted_y)
            random.shuffle(correct)
            random.shuffle(incorrect)
            to_write_c = '\n'.join([' '.join(y.split('_')) for y in correct])
            to_write_inc = '\n'.join([' '.join(y.split('_')) for y in incorrect])
            c.write(f'{to_write_c}')
            inc.write(f'{to_write_inc}')



# write_test_examples('data_gen/fakegrammarexp1/fakegrammarexp1', False)
# write_test_examples('data_gen/fakegrammarexp1_permutation/fakegrammarexp1_permutation', True)
#
write_test_examples('data_gen/fakegrammarexp2/fakegrammarexp2', False)
write_test_examples('data_gen/fakegrammarexp2_permutation/fakegrammarexp2_permutation', True)

# write_test_examples('data_gen/fakegrammarexp3/fakegrammarexp3', False)
# write_test_examples('data_gen/fakegrammarexp3_permutation/fakegrammarexp3_permutation', True)



