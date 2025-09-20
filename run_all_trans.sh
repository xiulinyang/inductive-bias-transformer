#!/bin/bash
mkdir -p trans-results

for num in {0..9}; do
  bash train_lm_transformer.sh grammar_close_then_open_3 $num
  bash train_lm_transformer.sh grammar_close_then_open_3_permutation $num
  bash train_lm_transformer.sh grammar_close_then_open_30 $num
  bash train_lm_transformer.sh grammar_close_then_open_30_permutation $num
  bash train_lm_transformer.sh grammar_close_then_open_60 $num
  bash train_lm_transformer.sh grammar_close_then_open_60_permutation $num
  bash train_lm_transformer.sh grammar_close_then_open_3_r $num
  bash train_lm_transformer.sh grammar_close_then_open_30_r $num
  bash train_lm_transformer.sh grammar_close_then_open_60_r $num
  bash train_lm_transformer.sh grammar_close_then_open_3_reverse $num
  bash train_lm_transformer.sh grammar_close_then_open_3_reverse_permutation $num
done
