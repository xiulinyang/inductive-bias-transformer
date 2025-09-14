#!/bin/bash

# Array of 10 random seeds
seed=$1
grammar=$2


mkdir -p data_gen/grammar/"${grammar}"
mkdir -p data_gen/grammar/"${grammar}"_permutation
python data_gen/sample_sentences.py -g data_gen/"${grammar}.gr" -n 100000 -O data_gen/grammar/"${grammar}"/"${grammar}"_b.txt -s "${seed}" -b True
python data_gen/permute_sentences.py -s data_gen/grammar/"${grammar}"/"${grammar}"_b.txt -g "${grammar}"
python scripts/postprocess.py -i data_gen/grammar/"${grammar}"/"${grammar}"_b.txt -o data_gen/grammar/"${grammar}"/"${grammar}".txt
#
echo "All scripts have been run with all seeds."

python data_gen/make_splits.py -S data_gen/grammar/"${grammar}"_permutation/ -O .
python data_gen/make_splits.py -S data_gen/grammar/"${grammar}"/ -O .

