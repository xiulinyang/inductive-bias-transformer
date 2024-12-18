#!/bin/bash
mkdir -p lstm-results

for num in {0..9}; do
  bash train_lm_lstm.sh grammar42 $num
  bash train_lm_lstm.sh grammar42_permutation $num
  bash train_lm_lstm.sh grammar41 $num
  bash train_lm_lstm.sh grammar41_permutation $num
  bash train_lm_lstm.sh grammar53 $num
  bash train_lm_lstm.sh grammar53_permutation $num
done
