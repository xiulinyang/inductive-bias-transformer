#!/bin/bash

# Array of 10 random seeds
seed=$1
exp=$2
grammar=$3


mkdir -p data_gen/grammar/grammar${seed}${exp}
mkdir -p data_gen/grammar/grammar${seed}${exp}_permutation
python data_gen/sample_sentences.py -g ${grammar} -n 100000 -O data_gen/grammar/grammar${seed}${exp}/grammar${seed}${exp}_b.txt -s ${seed} -b True
python data_gen/permute_sentences.py -s data_gen/grammar/grammar${seed}${exp}/grammar${seed}${exp}_b.txt -o data_gen/grammar/grammar${seed}${exp}_permutation/grammar${seed}${exp}_permutation.txt -e ${exp}
python postprocess.py -i data_gen/grammar/grammar${seed}${exp}/grammar${seed}${exp}_b.txt -o data_gen/grammar/grammar${seed}${exp}/grammar${seed}${exp}.txt

echo "All scripts have been run with all seeds."

python data_gen/make_splits.py -S data_gen/grammar/grammar${seed}${exp}_permutation/ -O .
python data_gen/make_splits.py -S data_gen/grammar/grammar${seed}${exp}/ -O .

