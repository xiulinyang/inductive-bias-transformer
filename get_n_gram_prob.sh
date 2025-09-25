#!/bin/bash

all_grammars=("grammar_close_then_open_3" "grammar_close_then_open_30" "grammar_close_then_open_60")
mkdir -p bigram

for num in {0..9}; do
  for grammar in "${all_grammars[@]}"; do
    python bi_gram.py -g "${grammar}_permutation" -s $num -m 'trans'
    python bi_gram.py -g "${grammar}_permutation" -s $num -m 'lstm'
    python bi_gram.py -g "${grammar}_r" -s $num -m 'trans'
    python bi_gram.py -g "${grammar}_r" -s $num -m 'lstm'
    python bi_gram.py -g "${grammar}_reverse" -s $num -m 'trans'
    python bi_gram.py -g "${grammar}_reverse" -s $num -m 'lstm'
  done
done
