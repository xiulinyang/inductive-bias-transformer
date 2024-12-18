#!/bin/bash

mkdir -p trans-results

for num in {0..9}; do
  bash train_lm_transformer.sh grammar41 $num
  bash train_lm_transformer.sh grammar41_permutation $num
  bash train_lm_transformer.sh grammar53 $num
  bash train_lm_transformer.sh grammar53_permutation $num
done
