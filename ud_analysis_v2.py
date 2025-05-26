from pathlib import Path
from conllu import parse
from glob import glob
from tqdm import tqdm
import json


ud_trees = Path('ud/en_gum-ud-train.conllu').read_text().strip().split('\n\n')
closed_upos = ['ADP', 'AUX', 'CCONJ', 'DET', 'PART', 'PRON', 'SCONJ']
open_upos = ['ADJ', 'ADV', 'INTJ', 'NOUN', 'PROPN', 'VERB', 'NUM']
other_upos = ['X', 'PUNCT', 'SYM', '_']

ling_map = json.loads(Path('ud_language_abbreviations.json').read_text().strip())


with open('open_close_dependent_all_pron.tsv', 'w') as open_close_dependent:
    open_close_dependent.write(f'Lang\topen_require_close\topen_require_close_ratio'
                               f'\topen_stand_alone\topen_stand_alone_ratio'
                               f'\tclose_require_open\tclose_require_open_ratio\t'
                               f'close_stand_alone\tclose_stand_alone_ratio\tclose_all\topen_all\n')

    for lang in tqdm(sorted(glob('/Users/xiulinyang/Downloads/ud2/ud-treebanks-v2.15/*'))):

        real_lang = lang.split('/')[-1]
        real_lang = ling_map[real_lang]
        all_conllu_files = glob(lang + '/*.conllu')
        ud_trees = []
        for conllu_file in all_conllu_files:
            ud_trees.extend(Path(conllu_file).read_text().strip().split('\n\n'))
        all_open = 0
        all_close = 0
        oc = 0
        oo = 0
        cc = 0
        oc_pair = []
        oo_pair = []
        cc_pair = []
        dep_pair = []
        open_require_close = 0
        open_stand_alone = 0
        close_require_open = 0
        close_stand_alone = 0
        for tree in tqdm(ud_trees):
            parsed_sent = parse(tree)[0]
            all_heads = [x['head'] for x in parsed_sent]
            for parsed_token in parsed_sent:
                upos = parsed_token['upos']
                head = parsed_token['head']
                if head not in [0, None]:
                    head_upos = [x['upos'] for x in parsed_sent if x['id'] == head][0]
                else:
                    continue

                dep_pair.append((upos, head_upos))

        oc_pair = [x for x in dep_pair if (x[0] in open_upos and x[1] in closed_upos) or (x[0] in closed_upos and x[1] in open_upos)]
        cc_pair = [x for x in dep_pair if x[0] in closed_upos and x[1] in closed_upos]
        oo_pair = [x for x in dep_pair if x[0] in open_upos and x[1] in open_upos]
        o = [x for x in dep_pair if x[0] in open_upos or x[1] in open_upos]
        c = [x for x in dep_pair if x[0] in closed_upos or x[1] in closed_upos]



        open_require_close_ratio = (len(oc_pair) / len(c)) * 100 if len(c) > 0 else 0
        close_require_open_ratio = (len(oc_pair) / len(o)) * 100 if len(o) > 0 else 0
        print(len(oc_pair), len(o), len(c))
        open_stand_alone_ratio = (len(oo_pair) / len(o)) * 100 if len(o) > 0 else 0
        close_stand_alone_ratio = (len(cc_pair) / len(c)) * 100 if len(c) > 0 else 0
        # close_predict_open_ratio = open_require_close/(open_require_close + )
        # open_require_close_ratio = round(open_require_close/(open_require_close+open_stand_alone),3)*100 if (open_require_close + open_stand_alone) != 0 else 0
        # open_stand_alone_ratio = round(open_stand_alone/(open_stand_alone+open_require_close),3)*100 if (open_stand_alone + open_require_close) != 0 else 0
        # close_require_open_ratio = round(close_require_open/(close_require_open+close_stand_alone),3)*100 if (close_require_open + close_stand_alone) != 0 else 0
        # close_stand_alone_ratio = round(close_stand_alone/(close_stand_alone+close_require_open),3)*100 if (close_stand_alone + close_require_open) != 0 else 0
        # close_predict_open_ratio = round(open_require_close/(open_require_close+close_stand_alone),3)*100 if (open_require_close + close_stand_alone) != 0 else 0
        open_close_dependent.write(
            f'{real_lang}\t{open_require_close}\t{open_require_close_ratio:.1f}\t{open_stand_alone}\t{open_stand_alone_ratio:.1f}\t{close_require_open}\t{close_require_open_ratio:.1f}\t{close_stand_alone}\t{close_stand_alone_ratio:.1f}\t{all_close}\t{all_open}\n')

# with open('open_close_dependent_all_pron.tsv', 'w') as open_close_dependent:
#     open_close_dependent.write(f'Lang\topen_require_close\topen_require_close_ratio'
#                                f'\topen_stand_alone\topen_stand_alone_ratio'
#                                f'\tclose_require_open\tclose_require_open_ratio\t'
#                                f'close_stand_alone\tclose_stand_alone_ratio\tclose_all\topen_all\n')
#
#     for lang in tqdm(sorted(glob('/Users/xiulinyang/Downloads/ud2/ud-treebanks-v2.15/UD_English*'))):
#
#         real_lang = lang.split('/')[-1]
#         real_lang = ling_map[real_lang]
#         all_conllu_files = glob(lang + '/*.conllu')
#         ud_trees = []
#         for conllu_file in all_conllu_files:
#             ud_trees.extend(Path(conllu_file).read_text().strip().split('\n\n'))
#
#         for tree in tqdm(ud_trees):
#             all_open = 0
#             all_close = 0
#             oc = 0
#             oo = 0
#             cc = 0
#             oc_pair = []
#             oo_pair = []
#             cc_pair = []
#             dep_pair = []
#             open_require_close = 0
#             open_stand_alone = 0
#             close_require_open = 0
#             close_stand_alone = 0
#             parsed_sent = parse(tree)[0]
#             all_heads = [x['head'] for x in parsed_sent]
#             for parsed_token in parsed_sent:
#                 upos = parsed_token['upos']
#                 head = parsed_token['head']
#
#                 if head not in [0, None]:
#                     head_upos = [x['upos'] for x in parsed_sent if x['id'] == head][0]
#                 else:
#                     continue
#
#                 dep_pair.append((upos, head_upos))
#                 if upos in closed_upos and head_upos in closed_upos:
#                     print(tree)
#             oc_pair = [x for x in dep_pair if (x[0] in open_upos and x[1] in closed_upos) or (x[0] in closed_upos and x[1] in open_upos)]
#             cc_pair = [x for x in dep_pair if x[0] in closed_upos and x[1] in closed_upos]
#             oo_pair = [x for x in dep_pair if x[0] in open_upos and x[1] in open_upos]
#             o = [x for x in dep_pair if x[0] in open_upos or x[1] in open_upos]
#             c = [x for x in dep_pair if x[0] in closed_upos or x[1] in closed_upos]
#
#             open_require_close_ratio = (len(oc_pair) / len(c)) * 100 if len(c) > 0 else 0
#             close_require_open_ratio = (len(oc_pair) / len(o)) * 100 if len(o) > 0 else 0
#
#
#             if open_require_close_ratio<close_require_open:
#                 print(len(oc_pair), len(o), len(c))
#                 print('find the tree that closed class is required by the open class')
#                 print(open_require_close_ratio, close_require_open_ratio)
#                 print(tree)
#             open_stand_alone_ratio = (len(oo_pair) / len(o)) * 100 if len(o) > 0 else 0
#             close_stand_alone_ratio = (len(cc_pair) / len(c)) * 100 if len(c) > 0 else 0
#         # close_predict_open_ratio = open_require_close/(open_require_close + )
#         # open_require_close_ratio = round(open_require_close/(open_require_close+open_stand_alone),3)*100 if (open_require_close + open_stand_alone) != 0 else 0
#         # open_stand_alone_ratio = round(open_stand_alone/(open_stand_alone+open_require_close),3)*100 if (open_stand_alone + open_require_close) != 0 else 0
#         # close_require_open_ratio = round(close_require_open/(close_require_open+close_stand_alone),3)*100 if (close_require_open + close_stand_alone) != 0 else 0
#         # close_stand_alone_ratio = round(close_stand_alone/(close_stand_alone+close_require_open),3)*100 if (close_stand_alone + close_require_open) != 0 else 0
#         # close_predict_open_ratio = round(open_require_close/(open_require_close+close_stand_alone),3)*100 if (open_require_close + close_stand_alone) != 0 else 0
#         open_close_dependent.write(
#             f'{real_lang}\t{open_require_close}\t{open_require_close_ratio:.1f}\t{open_stand_alone}\t{open_stand_alone_ratio:.1f}\t{close_require_open}\t{close_require_open_ratio:.1f}\t{close_stand_alone}\t{close_stand_alone_ratio:.1f}\t{all_close}\t{all_open}\n')
