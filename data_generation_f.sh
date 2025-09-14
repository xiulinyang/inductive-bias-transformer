#!/bin/bash

# Array of 10 random seeds
grammar=$1
num_function=$2


mkdir -p data_gen/grammar/"${grammar}"
mkdir -p data_gen/grammar/"${grammar}"_permutation
python data_gen/add_function_words_to_sents.py -s data_gen/grammar/"${grammar}"/"${grammar}"_b.txt -g "${grammar}"_"${num_function}"
python data_gen/permute_sentences.py -s data_gen/grammar/"${grammar}"_"${num_function}"/"${grammar}"_"${num_function}"_b.txt -g "${grammar}"_"${num_function}"
python scripts/postprocess.py -i data_gen/grammar/"${grammar}"_"${num_function}"/"${grammar}"_"${num_function}"_b.txt -o data_gen/grammar/"${grammar}"_"${num_function}"/"${grammar}"_"${num_function}".txt

echo "All scripts have been run with all seeds."

python data_gen/make_splits.py -S data_gen/grammar/"${grammar}"_"${num_function}"_permutation/ -O .
python data_gen/make_splits.py -S data_gen/grammar/"${grammar}"_"${num_function}"/ -O .

