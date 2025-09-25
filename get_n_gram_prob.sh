#!/bin/bash

all_grammars=("grammar_close_then_open_3" "grammar_close_then_open_30" "grammar_close_then_open_60")
mkdir -p bigram

for num in {0..9}; do
  for grammar in "${all_grammars[@]}"; do
    python bi_gram.py -g "${grammar}" -s $num -m 'trans' -a "permutation"
    python bi_gram.py -g "${grammar}" -s $num -m 'lstm' -a "permutation"
    python bi_gram.py -g "${grammar}" -s $num -m 'trans' -a "r"
    python bi_gram.py -g "${grammar}" -s $num -m 'lstm' -a "r"
    python bi_gram.py -g "${grammar}" -s $num -m 'trans' -a "reverse"
    python bi_gram.py -g "${grammar}" -s $num -m 'lstm' -a "reverse"
  done
done
