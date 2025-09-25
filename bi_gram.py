import pandas as pd
import argparse
import kenlm
import math
from tqdm import tqdm 
from pathlib import Path
parser = argparse.ArgumentParser()
parser.add_argument('-g', '--grammar_name', type=str, help='name of the grammar, e.g., grammar_close_then_open')
parser.add_argument('-s', '--sample_split', type=int, help='0-9')
parser.add_argument('-m', '--model_type', type=str, choices=['trans', 'lstm'])


args = parser.parse_args()
model_type = args.model_type
sample_split = str(args.sample_split)
grammar_name = args.grammar_name


test_data = pd.read_csv(f'{model_type}_sentence_scores/{grammar_name}/{sample_split}.test.tsv', sep=',').to_dict(orient='records')
# test_data = Path(f'{model_type}_sentence_scores/{grammar_name}/{sample_split}.test.txt').read_text().strip().split('\n')
# test_data = [{'sent':x.split('\t')[0], 'toks': x.split('\t')[1], 'model_prob': x.split('\t')[2]} for x in test_data]
# print(test_data)

model = kenlm.LanguageModel(f'trigram/{grammar_name}_{sample_split}.arpa')
for sent in tqdm(test_data):
    toks = sent['toks']
    model_score = model.score(toks, bos=False, eos=False)
    sent['trigram_prob'] = model_score*math.log(10)


pd.DataFrame(test_data).to_csv(f'{model_type}_sentence_scores/{grammar_name}/{sample_split}.test.csv')
