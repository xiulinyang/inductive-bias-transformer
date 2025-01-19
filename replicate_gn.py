from pathlib import Path
import random
import re
import argparse
random.seed(21)
parser = argparse.ArgumentParser(description='The script generates the language based on the grammar designed by Getz & Newport (2019)')
parser.add_argument('experiment', help='the name of the experiment, the ending must be in [exp1, exp2, exp3]')
args = parser.parse_args()


GRAMMAR_NAME= args.experiment
assert GRAMMAR_NAME[-4:] in ['exp1', 'exp2', 'exp3']

rule_list = [
    "AXYBC", "XYBC", "AYC", "AY", "YB",
    "AXYB", "ABC", "XYC", "AB", "YC",
    "AXYC", "AXY", "XYB", "AC", "BC",
    "AYBC", "AYB", "YBC", "XY"
]


if 'exp2' in GRAMMAR_NAME:
    close_class = ['institutionalise', 'internationalise', 'black-and-white', 'well-documented', 'intellectualise',
                    'departmentalise', 'inconsequential', 'impressionable', 'counterbalance', 'happy-go-lucky']
else:
    close_class = ['a', 'the', 'one', 'my', 'your', 'this', 'an', 'her', 'his', 'dank']


vocab_source = 'data_gen/english/vocab_source_filtered.txt'
open_class_vocab = list(set([y.split()[0].strip() for y in Path(vocab_source).read_text().strip().split('\n')]))

a = random.sample(open_class_vocab, 200)
open_class = random.sample([x for x in open_class_vocab if x not in a], 200)
b = random.sample([x for x in open_class_vocab if x not in a+open_class], 200)
c = random.sample([x for x in open_class_vocab if x not in a+open_class+b], 200)


with open(f'vocab/{GRAMMAR_NAME}_vocaba.txt', 'w') as avocab, open(f'vocab/{GRAMMAR_NAME}_vocaby.txt', 'w') as openc_vocab:
    to_a = '\n'.join(a)
    to_o = '\n'.join(open_class)
    avocab.write(to_a)
    openc_vocab.write(to_o)


with open(f'vocab/{GRAMMAR_NAME}_vocab.txt', 'w') as v, open(f'vocab/{GRAMMAR_NAME}_vocab_close.txt', 'w') as cv:
    to_wr = '\n'.join(a+b+c+open_class)
    to_cv = '\n'.join(close_class)
    v.write(to_wr)
    cv.write(to_cv)


Path(f'data_gen/{GRAMMAR_NAME}/{GRAMMAR_NAME}').mkdir(parents=True, exist_ok=True)
Path(f'data_gen/{GRAMMAR_NAME}_permutation/{GRAMMAR_NAME}_permutation').mkdir(parents=True, exist_ok=True)
vocab = {'A': a, 'X': close_class, 'Y': open_class, 'B': b, 'C': c}
for n in range(10):
    with (open(f'data_gen/{GRAMMAR_NAME}/{GRAMMAR_NAME}/{n}.trn', 'w') as train,
         open(f'data_gen/{GRAMMAR_NAME}_permutation/{GRAMMAR_NAME}_permutation/{n}.trn', 'w') as perm_train,
        open(f'data_gen/{GRAMMAR_NAME}/{GRAMMAR_NAME}/{n}.dev', 'w') as dev,
        open(f'data_gen/{GRAMMAR_NAME}_permutation/{GRAMMAR_NAME}_permutation/{n}.dev', 'w') as perm_dev,
        open(f'data_gen/{GRAMMAR_NAME}/{GRAMMAR_NAME}/{n}.tst', 'w') as test,
        open(f'data_gen/{GRAMMAR_NAME}_permutation/{GRAMMAR_NAME}_permutation/{n}.tst', 'w') as perm_test,):
        if 'exp3' in GRAMMAR_NAME:
            hh = open(f'data_gen/{GRAMMAR_NAME}/{GRAMMAR_NAME}/inverse{n}.trn', 'w')
            perm_hh = open(f'data_gen/{GRAMMAR_NAME}_permutation/{GRAMMAR_NAME}_permutation/inverse{n}.trn', 'w')
        else:
            hh = None
            perm_hh = None
        sents = []
        sents_dev =[]
        sents_test =[]
        sents_helper = []
        for rule in rule_list:
            if 'exp3' in GRAMMAR_NAME:
                rule = re.sub('XY', 'YX', rule)
            for i in range(600):
                no_pertub =[]
                pertub = []
                helper_no_perb =[]
                helper_perb  =[]
                X = random.choice(close_class)
                Y = random.choice(open_class)
                for r in rule:

                    if r not in ['X','Y']:
                        word = random.choice(vocab[r])
                        no_pertub.append(word)
                        pertub.append(word)
                        helper_perb.append(word)
                        helper_no_perb.append(word)

                    else:
                        if 'X' in rule and 'Y' in rule:
                            if r =='X':
                                word = X
                                no_pertub.append(word)
                                pertub.append(Y)
                                helper_no_perb.append(Y)
                                helper_perb.append(word)

                            else:
                                word = Y
                                no_pertub.append(word)
                                pertub.append(X)
                                helper_no_perb.append(X)
                                helper_perb.append(word)
                        else:
                            if r =='Y':
                                word = Y
                                no_pertub.append(word)
                                pertub.append(X)
                                helper_no_perb.append(X)
                                helper_perb.append(word)
                            else:
                                raise ValueError('Something went wrong! Need debugging!')

                no_per = ' '.join(no_pertub)
                yes_per = ' '.join(pertub)

                helper_no_perb_sent = ' '.join(helper_no_perb)
                helper_perb_sent = ' '.join(helper_perb)
                #debug
                # print(helper_no_perb_sent)
                # print(no_per)
                if i<500:
                    sents.append((no_per, yes_per, helper_no_perb_sent, helper_perb_sent))
                elif 500 < i < 551: #generate examples for test and dev split
                    sents_dev.append((no_per, yes_per))
                else:
                    sents_test.append((no_per, yes_per))
        random.shuffle(sents)
        random.shuffle(sents_dev)
        random.shuffle(sents_test)

        print('Generate language successfully. Here are the 3 example sentences.\n')
        print(sents[:3])

        for x, y, z, h in sents:
            train.write(f'{x}\n')
            perm_train.write(f'{y}\n')
            if hh and perm_hh:
                hh.write(f'{z}\n')
                perm_hh.write(f'{h}\n')

        for x, y in sents_dev:
            dev.write(f'{x}\n')
            perm_dev.write(f'{y}\n')

        for x, y in sents_test:
            test.write(f'{x}\n')
            perm_test.write(f'{y}\n')

    if hh:
        hh.close()
    if perm_hh:
        perm_hh.close()


