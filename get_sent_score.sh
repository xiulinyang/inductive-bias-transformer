#!/bin/bash

for num in {0..9}; do
  python get_sentence_scores.py -i "trans-results/grammar42exp2/grammar42exp2/grammar42exp2.${num}.dev.txt" -O "trans_sentence_scores/"
done
