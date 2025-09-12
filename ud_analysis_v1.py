from pathlib import Path
from conllu import parse
from glob import glob
from tqdm import tqdm
ud_trees = Path('ud/en_gum-ud-train.conllu').read_text().strip().split('\n\n')
closed_upos = ['ADP', 'AUX', 'CCONJ', 'DET', 'PART', 'PRON', 'SCONJ']
open_upos = ['ADJ', 'ADV', 'INTJ', 'NOUN', 'PROPN', 'VERB','NUM']
other_upos = ['X', 'PUNCT', 'SYM','_']


with open('open_close_dependent_all_pron.tsv', 'w') as open_close_dependent:
    open_close_dependent.write(f'Lang\topen_require_close\topen_require_close_ratio'
                               f'\topen_stand_alone\topen_stand_alone_ratio'
                               f'\tclose_require_open\tclose_require_open_ratio\t'
                               f'close_stand_alone\tclose_stand_alone_ratio\tclose_all\topen_all\n')

    for lang in tqdm(sorted(glob('/Users/xiulinyang/Downloads/ud2/ud-treebanks-v2.15/*'))):


        real_lang = lang.split('/')[-1]
        all_conllu_files = glob(lang + '/*.conllu')
        ud_trees =[]
        for conllu_file in all_conllu_files:
            ud_trees.extend(Path(conllu_file).read_text().strip().split('\n\n'))
        all_open=0
        all_close=0
        oc = 0
        oo=0
        cc =0

        open_require_close = 0
        open_stand_alone = 0
        close_require_open = 0
        close_stand_alone = 0
        for tree in tqdm(ud_trees):
            parsed_sent = parse(tree)[0]
            all_heads = [x['head'] for x in parsed_sent]
            for parsed_token in parsed_sent:
                upos = parsed_token['upos']
                if upos in closed_upos:
                    all_close+=1
                if upos in open_upos:
                    all_open+=1
                head = parsed_token['head']
                if head not in [0,None]:
                    head_upos = [x['upos'] for x in parsed_sent if x['id']==head][0]
                id = parsed_token['id']
                dependent_upos = [x['upos'] for x in parsed_sent if x['head'] == id and x['upos'] not in other_upos]
                close_upos_depent = len(dependent_upos + closed_upos) - len(set(dependent_upos + closed_upos))
                open_upos_depent = len(dependent_upos + open_upos) - len(set(dependent_upos + open_upos))

                # if len(dependent_upos) > 0:
                #     if upos in open_upos:
                #         if close_upos_depent > 0:
                #             oc+=close_upos_depent
                #         elif open_upos_depent >0:
                #             oo+=open_upos_depent
                #
                #     elif upos in closed_upos:
                #         if open_upos_depent > 0:
                #             oc+=open_upos_depent
                #         elif close_upos_depent > 0:
                #             cc+=close_upos_depent
                #     else:
                #         if upos in ['PUNCT', 'X', 'SYM', '_']:
                #             continue
                #         else:
                #             print(upos)
                #             raise ValueError(
                #                 'UPOS tags are not found!'
                #             )


        open_require_close_ratio = (oc / all_open)*100 if all_open > 0 else 0
        close_require_open_ratio = (oc / all_close)*100  if all_close > 0 else 0
        print(oc, all_close, all_open)
        open_stand_alone_ratio = (oo / all_open)*100  if all_open > 0 else 0
        close_stand_alone_ratio = (cc / all_close)*100  if all_close > 0 else 0
        # close_predict_open_ratio = open_require_close/(open_require_close + )
        # open_require_close_ratio = round(open_require_close/(open_require_close+open_stand_alone),3)*100 if (open_require_close + open_stand_alone) != 0 else 0
        # open_stand_alone_ratio = round(open_stand_alone/(open_stand_alone+open_require_close),3)*100 if (open_stand_alone + open_require_close) != 0 else 0
        # close_require_open_ratio = round(close_require_open/(close_require_open+close_stand_alone),3)*100 if (close_require_open + close_stand_alone) != 0 else 0
        # close_stand_alone_ratio = round(close_stand_alone/(close_stand_alone+close_require_open),3)*100 if (close_stand_alone + close_require_open) != 0 else 0
        # close_predict_open_ratio = round(open_require_close/(open_require_close+close_stand_alone),3)*100 if (open_require_close + close_stand_alone) != 0 else 0
        open_close_dependent.write(f'{real_lang}\t{open_require_close}\t{open_require_close_ratio:.1f}\t{open_stand_alone}\t{open_stand_alone_ratio:.1f}\t{close_require_open}\t{close_require_open_ratio:.1f}\t{close_stand_alone}\t{close_stand_alone_ratio:.1f}\t{all_close}\t{all_open}\n')
