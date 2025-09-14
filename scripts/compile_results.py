import argparse
import math
from glob import glob
from pathlib import Path

def get_perplexity(filename):
	file = open(filename, 'r')
	lines = file.readlines()
	final_line = lines[-1].strip('\n')
	return float(final_line.split(" ")[-1])

def calc_sd(vals):
	mean = calc_mean(vals)
	return math.sqrt(sum([(x - mean)**2 for x in vals])/len(vals))

def calc_mean(vals):
	return sum(vals)/len(vals)

parser = argparse.ArgumentParser(description="Calculate mean and SD of "
	"perplexity for dev and test for each grammar")

parser.add_argument("-m", "--model", type=str, required=True,
    help="Location of results file")

parser.add_argument("-o", "--output_file_name", type=str, required=True,
	help="file name, e.g., perpelxity.csv")
args = parser.parse_args()

out = args.output_file_name
model = args.model
grammar_folder =  f'{model}-results'
results_files = glob(f'results/{grammar_folder}/*.txt')
Path(f'results/{model}_scores/').mkdir(parents=True, exist_ok=True)

results_files = [x for x in results_files if 'correct' not in x]
output_file = open(f'results/{model}_scores/{out}', 'w')

perplexity_dict = {}
for res in results_files:
	grammar, split, test_dev, _ = res.split("/")[-1].split(".")
	if grammar not in perplexity_dict.keys():
		perplexity_dict[grammar] = {}
	if test_dev not in perplexity_dict[grammar].keys():
		perplexity_dict[grammar][test_dev] = []
	perplexity_dict[grammar][test_dev].append(get_perplexity(res))

for grammar in perplexity_dict.keys():
	for k, v in perplexity_dict[grammar].items():
		values = '\t'.join([str(x) for x in v])
		output_file.write(f'{grammar}\t{k}\t{values}\n')

