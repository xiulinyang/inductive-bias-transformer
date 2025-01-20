from pathlib import Path
from glob import glob
from collections import Counter
import matplotlib.pyplot as plt
import numpy as np
import random

vocab = Path('data_gen/base-grammar.gr').read_text().strip().split('\n\n\n')[1]
with open('vocab/vocab_Y.txt', 'w') as vy:
    all_vocab = [x.split()[-1] for x in vocab.split('\n') if len(x.strip())>1]
    vy.write('\n'.join(all_vocab))

# random.seed(50)
# def get_bigrams(sents):
#     bigrams = [b for l in sents for b in zip(l.split(" ")[1:-1], l.split(" ")[2:])]
#     bigram_perm = ['_'.join(list(x)) for x in bigrams if x[1]!='']
#     return bigram_perm
#
# def get_bigram_persent(sent):
#     bigrams = [b for b in zip(sent.split(' ')[1:-1], sent.split(' ')[2:])]
#     bigram_perm = ['_'.join(list(x)) for x in bigrams]
#     return bigram_perm
#
# clo =["glim flugit",
# "flairb flugit gentif",
# "daffin clidam",
# "glim ka zup",
# "glim ka tombur bleggin",
# "flairb ka lapal bleggin gentif",
# "daffin ka tombur spad",
# "flairb zup",
# "daffin lapal nawg",
# "flairb tombur flugit spad",
# "flairb lapal spad",
# "bleggin spad",
# "ka lapal",
# "ka lapal flugit",
# "ka tombur nawg clidam",
# "ka lapal spad",
# "lapal nawg",
# "tombur bleggin gentif",
# "zup gentif",
# "glim nawg",
# "glim mawg spad",
# "glim clidam",
# "flairb ka tombur",
# "flairb ka zup nawg",
# "daffin ka zup flugit clidam",
# "glim ka lapal gentif",
# "daffin lapal",
# "glim zup bleggin",
# "daffin zup flugit spad",
# "daffin tombur clidam",
# "mawg gentif",
# "ka zup",
# "ka zup bleggin",
# "ka tombur mawg gentif",
# "ka zup spad",
# "tombur flugit",
# "zup mawg clidam",
# "lapal clidam"]
#
#
# op = ["glim flugit",
# "flairb flugit gentif",
# "daffin clidam",
# "glim tombur ka",
# "glim lapal ka bleggin",
# "flairb tombur ka bleggin gentif",
# "daffin tombur ka spad",
# "flairb ka",
# "daffin ka nawg",
# "flairb ka flugit spad",
# "flairb ka spad",
# "bleggin spad",
# "tombur ka",
# "lapal ka flugit",
# "tombur ka mawg clidam",
# "lapal ka spad",
# "ka nawg",
# "ka bleggin gentif",
# "ka gentif",
# "glim nawg",
# "glim mawg spad",
# "glim clidam",
# "flairb zup ka",
# "flairb lapal ka nawg",
# "daffin zup ka flugit clidam",
# "glim zup ka gentif",
# "daffin ka",
# "glim ka bleggin",
# "daffin ka flugit spad",
# "daffin ka clidam",
# "mawg gentif",
# "zup ka",
# "tombur ka bleggin",
# "zup ka nawg gentif",
# "lapal ka spad",
# "ka flugit",
# "ka mawg clidam",
# "ka clidam"]
#
# grammar_file = 'data_gen/grammar53exp1'
# grammar_file_pert = 'data_gen/grammar53exp1_permutation'
# b_a = []
# b_p = []
# # with open('same_bigram_sents.txt', 'w') as same, open('same_bigram_sents_pert.txt', 'w') as pe:
# for i in range(10):
#
#     sents = Path(f'{grammar_file}/grammar53exp1/{str(i)}.trn').read_text().strip().split('\n')
#     sents_pert = Path(f'{grammar_file_pert}/grammar53exp1_permutation/{str(i)}.trn').read_text().strip().split('\n')
#     # sents = clo
#     # sents_pert = op
#     bigrams = len(Counter(get_bigrams(sents)))
#     bigrams_pert = len(Counter(get_bigrams(sents_pert)))
#     b_a.append(bigrams)
#     b_p.append(bigrams_pert)
#     print(bigrams, bigrams_pert)
#
#     counter_a = Counter(get_bigrams(sents_pert))
#     counter_b = Counter(get_bigrams(sents))
#
# print(np.mean(b_a))
# print(np.mean(b_p))

    # frq = []
    # sent_frq = []
    # for sent, sent_pert in zip(sents, sents_pert):
    #     bigram = get_bigram_persent(sent)
    #     bigram_f = sorted([counter_b[x] for x in bigram])
    #     sent_frq.append(sent)
    #     frq.append(bigram_f)
    # # for sent_pert in sents_pert:
    #     bigram_p = get_bigram_persent(sent_pert)
    #     bigram_pf = sorted([counter_a[x] for x in bigram_p])
        # if bigram_pf == bigram_f:
        #     print(sent, sent_pert)

        # if bigram_pf in frq:
        #     print(sent_pert)
        #     pe.write(f'{sent_pert}\n')
        #     print(sent_frq[frq.index(bigram_pf)])
            # same.write(f'{}')

    # print(bigram_pf, bigram_f)
    # if bigram_f == bigram_pf:
    #     print(sent, sents_pert)

    # bin_size = 10
    # max_freq = max(max(counter_a.values()), max(counter_b.values()))
    # bins = range(0, 110, bin_size)
    # #max_freq + bin_size
    #
    # # Compute frequency counts for each bin
    # def bin_counts(counter, bins):
    #     counts = np.zeros(len(bins) - 1, dtype=int)
    #     for freq in counter.values():
    #         for i in range(len(bins) - 1):
    #             if bins[i] <= freq < bins[i + 1]:
    #                 counts[i] += 1
    #                 break
    #     return counts
    #
    #
    # counts_a = bin_counts(counter_a, bins)
    # counts_b = bin_counts(counter_b, bins)
    #
    # # Plot
    # plt.figure(figsize=(10, 6))
    # x = np.arange(len(bins) - 1)  # Bin indices
    # width = 0.35  # Width of each bar
    #
    # plt.bar(x - width / 2, counts_a, width, label='Perturbation', color='skyblue', alpha=0.8)
    # plt.bar(x + width / 2, counts_b, width, label='No Perturbation', color='orange', alpha=0.8)
    #
    # # Add labels and title
    # plt.xlabel("Frequency Range", fontsize=12)
    # plt.ylabel("Number of Items", fontsize=12)
    # plt.title("Frequency Distribution Comparison", fontsize=14)
    # plt.xticks(x, [f"{bins[i]}-{bins[i + 1] - 1}" for i in range(len(bins) - 1)], rotation=45)
    # plt.legend()
    #
    # # Adjust layout and show
    # plt.tight_layout()
    # plt.show()

# existing_vocab = Path('grammar42_y_vocab.txt').read_text().strip().split('\n')
# adj = Path('data_gen/english/english-adjectives.txt').read_text().strip().split('\n')
# grammar53 = Path('data_gen/base-grammar53.gr').read_text().strip().split('\n\n\n')
# print(len(grammar53))
# grammar41 = Path('data_gen/base-grammar41.gr').read_text().strip().split('\n\n\n')
# print(len(grammar41))
# with open('vocab/grammar53_y_vocab.txt', 'w') as g53, open('vocab/grammar41_y_vocab.txt', 'w') as g41:
#     for l in grammar53[1].split('\n'):
#         if l:
#             w = l.split()[2]
#             g53.write(f'{w}\n')
#     for l in grammar41[1].split('\n'):
#         if l:
#             w = l.split()[2]
#             g41.write(f'{w}\n')




# dict_cat ={'prep': prep, 'determ': determiner, 'aff': affix, 'comp': comp}
#
# with open('new_open_class_words.txt', 'a') as o:
#     for category, word_list in dict_cat.items():
#         for w in word_list:
#             if category == 'prep':
#                 to_write = f'1\tPrep\t{w}\n'
#             elif category == 'determ':
#                 to_write = f'1\tDet\t{w}\n'
#             elif category =='aff':
#                 to_write = f'1\tVaff\t{w}\n'
#             elif category == 'comp':
#                 to_write = f'1\tComp\t{w}\n'
#
#             o.write(f'{to_write}')
#         o.write('\n\n')