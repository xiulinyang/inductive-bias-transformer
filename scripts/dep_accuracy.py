from pathlib import Path
import argparse
parser = argparse.ArgumentParser(description="calculate the accuracy of the dependency test")

parser.add_argument("-m", "--model", type=str, required=True,
    help="Location of results file")

parser.add_argument("-o", "--output_file_name", type=str, required=True,
	help="file name, e.g., accuracy.csv")
args = parser.parse_args()
m = args.model
out = args.output_file_name
with open(f'results/{m}_scores/{out}', 'w') as res:
    for g in ['gn_grammarexp1', 'gn_grammarexp1_permutation','gn_grammarexp2', 'gn_grammarexp2_permutation', 'gn_grammarexp3', 'gn_grammarexp3_permutation']:
        correct_rate = []
        for i in range(10):
            correct = Path(f'results/sentence_scores_{m}/{g}/correct_{str(i)}.test.txt').read_text().strip().split('\n')
            incorrect = Path(f'results/sentence_scores_{m}/{g}/incorrect_{str(i)}.test.txt').read_text().strip().split('\n')

            c=0
            for c_score, i_score in zip(correct, incorrect):
                if float(c_score)>float(i_score):
                    c+=1
            correct_rate.append(c/len(correct))
        scores = '\t'.join([str(x) for x in correct_rate])
        res.write(f'{g}\ttest\t{scores}\n')
