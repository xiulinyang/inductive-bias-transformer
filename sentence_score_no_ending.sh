#!/bin/bash

EXP=fakegrammarexp3
EXPP=fakegrammarexp3_permutation
# Create directory for output if it doesn't exist
mkdir -p trans_sentence_scores_no_end/

# Take the grammar argument from a predefined list
for SPLIT in {0..9}; do
      # Run the Python script for each split
      python get_sentence_scores.py -i "trans-results/${EXP}/${EXP}_correct/${EXP}.correct_${SPLIT}.test.txt" -O trans_sentence_scores_no_end/
      python get_sentence_scores.py -i "trans-results/${EXP}/${EXP}_incorrect/${EXP}.incorrect_${SPLIT}.test.txt" -O trans_sentence_scores_no_end/
      python get_sentence_scores.py -i "trans-results/${EXP}/${EXPP}_correct/${EXPP}.correct_${SPLIT}.test.txt" -O trans_sentence_scores_no_end/
      python get_sentence_scores.py -i "trans-results/${EXP}/${EXPP}_incorrect/${EXPP}.incorrect_${SPLIT}.test.txt" -O trans_sentence_scores_no_end/
  done
