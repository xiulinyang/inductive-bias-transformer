import pandas as pd
import argparse
from pathlib import Path
parser = argparse.ArgumentParser()
parser.add_argument('-g', '--grammar_name', type=str, help='name of the grammar, e.g., grammar_close_then_open')
parser.add_argument('-s', '--sample_split', type=int, help='0-9')
parser.add_argument('-m', '--model_type', type=str, choices=['trans', 'lstm'])


args = parser.parse_args()
model_type = args.model_type
sample_split = str(args.sample_split)
grammar_name = args.grammar_name
syntat = Path(f'data_gen/grammar/{grammar_name}/{grammar_name}/{sample_split}.tst').read_text().strip().split('\n')
test_data = pd.read_csv(f'{model_type}_sentence_scores/{grammar_name}/{sample_split}.test.txt', sep='\t', header=None,names=['sent', 'toks', 'model_prob']).to_dict(orient='records')

for sent1, sent2 in zip(test_data, syntat):
    toks = sent1['sent']
    if sent2 != toks:
        print(sent2, toks)
        print(grammar_name, sample_split)

