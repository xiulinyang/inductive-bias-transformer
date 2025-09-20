#!/bin/bash

GRAMMAR=$1
SPLIT=$2

fairseq-train --task language_modeling "data-bin/${GRAMMAR}/${SPLIT}-dataset" --save-dir "checkpoints/${GRAMMAR}/${SPLIT}-lstm" --arch lstm_lm_small  --dropout 0.3 --optimizer adam --adam-betas '(0.9,0.98)' --weight-decay 0.01 --lr 0.0005 --lr-scheduler inverse_sqrt --wandb-project xiulin-yang-compling --warmup-updates 500 --clip-norm 0.0 --warmup-init-lr 1e-07 --tokens-per-sample 125 --sample-break-mode none --max-tokens 512 --update-freq 2 --patience 5 --max-update 10000 --no-epoch-checkpoints --no-last-checkpoints
fairseq-eval-lm "data-bin/${GRAMMAR}/${SPLIT}-dataset" --path "checkpoints/${GRAMMAR}/${SPLIT}-lstm/checkpoint_best.pt" --tokens-per-sample 125 --gen-subset "valid" --output-word-probs --quiet 2> "lstm-results/${GRAMMAR}.${SPLIT}.dev.txt"
fairseq-eval-lm "data-bin/${GRAMMAR}/${SPLIT}-dataset" --path "checkpoints/${GRAMMAR}/${SPLIT}-lstm/checkpoint_best.pt" --tokens-per-sample 125 --gen-subset "test" --output-word-probs --quiet 2> "lstm-results/${GRAMMAR}.${SPLIT}.test.txt"
python get_sentence_scores.py -i "lstm-results/${GRAMMAR}.${SPLIT}.test.txt" -O "sentence_scores_lstm/"
