#!/bin/bash
mkdir -p lstm-results


for num in {0..9}; do
  bash train_lm_lstm.sh gn_grammarexp1 $num
  bash train_lm_lstm.sh gn_grammarexp_permutation $num
  bash train_lm_lstm.sh gn_grammarexp2 $num
  bash train_lm_lstm.sh gn_grammarexp2_permutation $num
  bash train_lm_lstm.sh gn_grammarexp3 $num
  bash train_lm_lstm.sh gn_grammarexp3_permutation $num
  bash train_lm_lstm.sh grammar42exp1 $num
  bash train_lm_lstm.sh grammar42exp1_permutation $num
  bash train_lm_lstm.sh grammar41exp1 $num
  bash train_lm_lstm.sh grammar41exp1_permutation $num
  bash train_lm_lstm.sh grammar53exp1 $num
  bash train_lm_lstm.sh grammar53exp1_permutation $num
done
