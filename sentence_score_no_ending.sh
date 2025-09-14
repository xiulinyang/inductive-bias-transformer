#!/bin/bash

EXP=$1
EXPP=$2
MD=$3
# Create directory for output if it doesn't exist
#mkdir -p trans_sentence_scores_no_end/

# Take the grammar argument from a predefined list
for SPLIT in {0..9}; do
      # Run the Python script for each split
      python scripts/get_sentence_scores.py -i "results/${MD}-results/${EXP}.correct_${SPLIT}.test.txt" -O "results/sentence_scores_${MD}/"
      python scripts/get_sentence_scores.py -i "results/${MD}-results/${EXP}.incorrect_${SPLIT}.test.txt" -O "results/sentence_scores_${MD}/"
      python scripts/get_sentence_scores.py -i "results/${MD}-results/${EXPP}.correct_${SPLIT}.test.txt" -O "results/sentence_scores_${MD}/"
      python scripts/get_sentence_scores.py -i "results/${MD}-results/${EXPP}.incorrect_${SPLIT}.test.txt" -O "results/sentence_scores_${MD}/"
  done
