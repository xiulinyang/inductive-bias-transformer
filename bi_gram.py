import pandas as pd
import argparse
import kenlm
import math
from tqdm import tqdm 


ngram = 'bigram'
parser = argparse.ArgumentParser()
parser.add_argument('-g', '--grammar_name', type=str, help='name of the grammar, e.g., grammar_close_then_open')
parser.add_argument('-s', '--sample_split', type=int, help='0-9')
parser.add_argument('-m', '--model_type', type=str, choices=['trans', 'lstm'])

args = parser.parse_args()
model_type = args.model_type
sample_split = str(args.sample_split)
grammar_name = args.grammar_name


if ngram=='bigram':
    test_data = pd.read_csv(f'{model_type}_sentence_scores/{grammar_name}/{sample_split}.test.txt', sep='\t',
                            header=None, names=['sent', 'toks', 'model_prob'], index=False,).to_dict(orient='records')
elif ngram=='trigram':
    test_data = pd.read_csv(f'{model_type}_sentence_scores/{grammar_name}/{sample_split}.test.csv', index=False, sep=',').to_dict(orient='records')

model = kenlm.LanguageModel(f'{ngram}/{grammar_name}_{sample_split}.arpa')
for sent in tqdm(test_data):
    toks = sent['toks']
    model_score = model.score(toks, bos=False, eos=False)
    sent[f'{ngram}_prob'] = model_score*math.log(10)


pd.DataFrame(test_data).to_csv(f'{model_type}_sentence_scores/{grammar_name}/{sample_split}.test.csv')
