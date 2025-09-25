import pandas as pd
import argparse
import kenlm
parser = argparse.ArgumentParser()
parser.add_argument('-g', '--grammar_name', type=str, help='name of the grammar, e.g., grammar_close_then_open')
parser.add_argument('-s', '--sample_split', type=int, help='0-9')
parser.add_argument('-m', '--model_type', type=str, choices=['trans', 'lstm'])


args = parser.parse_args()
model_type = args.model_type
sample_split = str(args.sample_split)
grammar_name = args.grammar_name

model = kenlm.LanguageModel(f'bigram/{grammar_name}_{sample_split}.arpa')
test_data = pd.read_csv(f'{sample_split}_sentence_scores/{grammar_name}/{sample_split}.test.txt', sep='\t', header=None,
            names=['sent', 'toks', 'model_prob']).to_dict(orient='records')


for sent in test_data:
    toks = sent['toks']
    model_score = model.score(toks, sos=False, eos=False)
    sent['bigram_prob'] = model_score


pd.DataFrame(test_data).to_csv(f'{sample_split}_sentence_scores/{grammar_name}/{sample_split}.test.tsv')
