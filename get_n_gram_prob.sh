#!/bin/bash

all_grammars=("grammar_close_then_open_3" "grammar_close_then_open_30" "grammar_close_then_open_60"
"grammar_close_then_open_3_permutation" "grammar_close_then_open_30_permutation" "grammar_close_then_open_60_permutation"
 "grammar_close_then_open_3_reverse" "grammar_close_then_open_3_reverse_permutation"
"grammar_close_then_open_3_r" "grammar_close_then_open_30_r" "grammar_close_then_open_60_r")

mkdir -p bigram

for num in {0..9}; do
  for grammar in "${all_grammars[@]}"; do
    python bi_gram.py -g "${grammar}" -s $num -m 'trans'
    python bi_gram.py -g "${grammar}" -s $num -m 'lstm'
    python bi_gram.py -g "${grammar}" -s $num -m 'trans'
    python bi_gram.py -g "${grammar}" -s $num -m 'lstm'
    python bi_gram.py -g "${grammar}" -s $num -m 'trans'
    python bi_gram.py -g "${grammar}" -s $num -m 'lstm'
  done
done
