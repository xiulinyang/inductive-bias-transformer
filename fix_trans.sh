#!/bin/bash

mkdir -p trans-results


for num in {0..9}; do
  bash train_lm_transformer.sh gn_grammarexp1_permutation $num
done
