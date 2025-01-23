import csv
import argparse
import os
import math
from glob import glob
from pathlib import Path
import json

def get_perplexity(filename):
	file = open(filename, 'r')
	print(filename)
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

parser.add_argument("-g", "--grammar", type=str, required=True,
	help="grammar")
args = parser.parse_args()

model = args.model
grammar_name = args.grammar
grammar_folder =  f'{model}-results'
results_files = glob(f'{grammar_folder}/*.txt')
# print(results_files)
if 'incorrect' in grammar_name:
	results_files = [x for x in results_files if 'incorrect' in x]
	output_file = open('trans_scores/result_dependency.json', 'a')
elif 'correct' in grammar_name:
	results_files = [x for x in results_files if 'correct' in x and 'incorrect' not in x]
	output_file = open('trans_scores/result_dependency.json', 'a')
else:
	results_files = [x for x in results_files if 'correct' not in x]
	output_file = open('trans_scores/results.json', 'a')

perplexity_dict = {}
for res in results_files:
	grammar, split, test_dev, _ = res.split("/")[-1].split(".")
	if grammar not in perplexity_dict.keys():
		perplexity_dict[grammar] = {}
	if test_dev not in perplexity_dict[grammar].keys():
		perplexity_dict[grammar][test_dev] = []
	perplexity_dict[grammar][test_dev].append(get_perplexity(res))

Path(f'trans_scores/').mkdir(parents=True, exist_ok=True)


json.dump(perplexity_dict, output_file,indent=4)

