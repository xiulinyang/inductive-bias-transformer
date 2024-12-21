import csv
import argparse
import os
import math
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

parser.add_argument("-f", "--folder", type=str, required=True,
    help="Location of results file")

parser.add_argument("-O", "--output", type=str, required=True,
	help="Location to save output")

parser.add_argument("-g", "--grammar", type=str, required=True,
	help="grammar")
args = parser.parse_args()

grammar_name = args.grammar
grammar_folder = args.folder +'/'+ grammar_name
results_files = [os.path.join(grammar_folder, f) for f in os.listdir(
	grammar_folder) if f.endswith('.txt')]
# print(results_files)
perplexity_dict = {}
for res in results_files:
	grammar, split, test_dev, _ = res.split("/")[-1].split(".")
	if grammar not in perplexity_dict.keys():
		perplexity_dict[grammar] = {}
	if test_dev not in perplexity_dict[grammar].keys():
		perplexity_dict[grammar][test_dev] = []
	perplexity_dict[grammar][test_dev].append(get_perplexity(res))

Path(f'trans_scores/{grammar_name}/').mkdir(parents=True, exist_ok=True)
output_file = open(args.output, 'w')
if 'correct' not in grammar_name:
	fieldnames = ['grammar', 'dev_av', 'dev_sd', 'tst_av', 'tst_sd']
else:
	fieldnames = ['grammar', 'tst_av', 'tst_sd']

writer = csv.DictWriter(output_file, fieldnames=fieldnames)
writer.writeheader()

real_grammar = results_files[-1].split('/')[-1].split('.')[0]

if 'correct' not in grammar_name:
	print('haha')
	writer.writerow({'grammar':grammar_name,
		'dev_av':calc_mean(perplexity_dict[real_grammar]['dev']),
		'dev_sd':calc_sd(perplexity_dict[real_grammar]['dev']),
		'tst_av':calc_mean(perplexity_dict[real_grammar]['test']),
		'tst_sd':calc_sd(perplexity_dict[real_grammar]['test']),
		})
else:
	writer.writerow({'grammar': grammar,
					 'tst_av': calc_mean(perplexity_dict[real_grammar]['test']),
					 'tst_sd': calc_sd(perplexity_dict[real_grammar]['test']),
					 })

