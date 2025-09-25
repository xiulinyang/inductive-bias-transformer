#!/bin/bash

all_grammars=("grammar_close_then_open_3" "grammar_close_then_open_30" "grammar_close_then_open_60")
mkdir -p trigram

for num in {0..9}; do
  for grammar in "${all_grammars[@]}"; do
    kenlm/build/bin/lmplz -o 3 -S 80% --discount_fallback -T /tmp < data-bin/${grammar}/${num}/trn.spm > trigram/${grammar}_${num}.arpa
    kenlm/build/bin/lmplz -o 3 -S 80% --discount_fallback -T /tmp < data-bin/${grammar}_permutation/${num}/trn.spm > trigram/${grammar}_${num}_permutation.arpa
    kenlm/build/bin/lmplz -o 3 -S 80% --discount_fallback -T /tmp < data-bin/${grammar}_r/${num}/trn.spm > trigram/${grammar}_${num}_r.arpa
    kenlm/build/bin/lmplz -o 3 -S 80% --discount_fallback -T /tmp < data-bin/${grammar}_reverse/${num}/trn.spm > trigram/${grammar}_${num}_reverse.arpa
  done
done