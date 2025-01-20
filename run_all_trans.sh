#!/bin/bash

mkdir -p trans-results

grammar=$1
for num in {0..9}; do
  bash train_lm_transformer.sh $grammar $num
  bash train_lm_transformer.sh ${grammar}_permutation $num
done
