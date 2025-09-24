#!/bin/bash
mkdir -p lstm-results


for num in {4..5}; do
  bash train_lm_lstm.sh grammar_close_then_open_3 $num
  bash train_lm_lstm.sh grammar_close_then_open_3_permutation $num
  bash train_lm_lstm.sh grammar_close_then_open_30 $num
  bash train_lm_lstm.sh grammar_close_then_open_30_permutation $num
  bash train_lm_lstm.sh grammar_close_then_open_60 $num
  bash train_lm_lstm.sh grammar_close_then_open_60_permutation $num
  bash train_lm_lstm.sh grammar_close_then_open_3_r $num
  bash train_lm_lstm.sh grammar_close_then_open_30_r $num
  bash train_lm_lstm.sh grammar_close_then_open_60_r $num
  bash train_lm_lstm.sh grammar_close_then_open_3_reverse $num
  bash train_lm_lstm.sh grammar_close_then_open_3_reverse_permutation $num
done
