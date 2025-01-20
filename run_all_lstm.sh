#!/bin/bash
mkdir -p lstm-results

grammar=$1
for num in {0..9}; do
  bash train_lm_lstm.sh $grammar $num
  bash train_lm_lstm.sh ${grammar}_permutation $num
  bash train_lm_lstm.sh $grammar $num
  bash train_lm_lstm.sh ${grammar}_permutation $num
  bash train_lm_lstm.sh $grammar $num
  bash train_lm_lstm.sh ${grammar}_permutation $num
done
