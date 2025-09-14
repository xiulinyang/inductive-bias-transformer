#!/bin/bash

mkdir -p trans-results


for num in {0..9}; do
  bash train_lm_transformer.sh gn_grammarexp1 $num
  bash train_lm_transformer.sh gn_grammarexp1_permutation $num
  bash train_lm_transformer.sh gn_grammarexp2 $num
  bash train_lm_transformer.sh gn_grammarexp2_permutation $num
  bash train_lm_transformer.sh gn_grammarexp3 $num
  bash train_lm_transformer.sh gn_grammarexp3_permutation $num
  bash train_lm_transformer.sh grammar42exp1 $num
  bash train_lm_transformer.sh grammar42exp1_permutation $num
  bash train_lm_transformer.sh grammar41exp1 $num
  bash train_lm_transformer.sh grammar41exp1_permutation $num
  bash train_lm_transformer.sh grammar53exp1 $num
  bash train_lm_transformer.sh grammar53exp1_permutation $num
done

