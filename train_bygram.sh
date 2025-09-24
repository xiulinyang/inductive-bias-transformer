#!/bin/bash

all_grammars=("grammar_close_then_open_3" "grammar_close_then_open_30" "grammar_close_then_open_60")
mkdir bigram

for num in {0..9}; do
  for grammar in "${all_grammars[@]}"; do
    bin/lmplz -o 2 -S 80% -T /tmp < data-bin/${grammar}/${num}/trn.spm > bigram/${grammar}_${num}.arpa
    bin/build_binary bigram/${grammar}_${num}.arpa ${grammar}_${num}.bin

    bin/lmplz -o 2 -S 80% -T /tmp < data-bin/${grammar}_permutation/${num}/trn.spm > ${grammar}_${num}_permutation.arpa
    bin/lmplz -o 2 -S 80% -T /tmp < data-bin/${grammar}_r/${num}/trn.spm > ${grammar}_${num}_r.arpa
    bin/build_binary bigram/${grammar}_${num}_r.arpa ${grammar}_${num}_r.bin
    bin/build_binary bigram/${grammar}_${num}_permutation.arpa ${grammar}_${num}_permutation.bin

  done
done