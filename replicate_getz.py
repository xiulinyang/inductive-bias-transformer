from pathlib import Path
import random
import re
random.seed(21)
rule_list = [
    "AXYBC", "XYBC", "AYC", "AY", "YB",
    "AXYB", "ABC", "XYC", "AB", "YC",
    "AXYC", "AXY", "XYB", "AC", "BC",
    "AYBC", "AYB", "YBC", "XY"
]
close_class = ['a', 'the', 'one', 'my', 'your', 'this', 'an', 'her', 'his', 'dank']
vocab_source = ['vocab/grammar41_y_vocab.txt', 'data_gen/english/mostly-verbs-infinitive.txt',
                'data_gen/english/mostly-verbs-infinitive.txt', 'data_gen/english/english-trans.txt']
open_class_vocab = list(set([y.split()[0].strip() for x in vocab_source for y in Path(x).read_text().strip().split('\n') if y!='' and y.strip() not in '1234567890']))
open_class_vocab = [x.split()[0] for x in open_class_vocab if x not in close_class]

a = random.sample(open_class_vocab, 200)
open_class = random.sample([x for x in open_class_vocab if x not in a], 200)
b = random.sample([x for x in open_class_vocab if x not in a+open_class], 200)
c = random.sample([x for x in open_class_vocab if x not in a+open_class+b], 200)
# close_class = random.sample([x for x in open_class_vocab if x not in a+b+c+open_class and len(x)>10], 10)


GRAMMAR_NAME='fakegrammarexp3'

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
          open(f'data_gen/{GRAMMAR_NAME}_permutation/{GRAMMAR_NAME}_permutation/{n}.tst', 'w') as perm_test,
          open(f'data_gen/{GRAMMAR_NAME}/{GRAMMAR_NAME}/inverse{n}.trn', 'w') as hh,
          open(f'data_gen/{GRAMMAR_NAME}_permutation/{GRAMMAR_NAME}_permutation/inverse{n}.trn', 'w') as perm_hh,
          ):
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
                                print('wtf')

                no_per = ' '.join(no_pertub)
                yes_per = ' '.join(pertub)

                helper_no_perb_sent = ' '.join(helper_no_perb)
                helper_perb_sent = ' '.join(helper_perb)
                print(helper_no_perb_sent)
                print(no_per)
                if i<500:
                    sents.append((no_per, yes_per, helper_no_perb_sent, helper_perb_sent))
                    # sents_helper.append((helper_no_perb_sent, helper_perb_sent))
                elif i>500 and i<551:
                    sents_dev.append((no_per, yes_per))
                else:
                    sents_test.append((no_per, yes_per))
        random.shuffle(sents)
        random.shuffle(sents_dev)
        random.shuffle(sents_test)
        print(sents[:10])

        for x, y, z, h in sents:
            train.write(f'{x}\n')
            perm_train.write(f'{y}\n')
            hh.write(f'{z}\n')
            perm_hh.write(f'{h}\n')

        for x, y in sents_dev:
            dev.write(f'{x}\n')
            perm_dev.write(f'{y}\n')

        for x, y in sents_test:
            test.write(f'{x}\n')
            perm_test.write(f'{y}\n')




