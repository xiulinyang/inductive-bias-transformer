
#!/bin/bash

GRAMMAR=$1
SPLIT=$2


fairseq-train --task language_modeling "data-bin/${GRAMMAR}/${SPLIT}-dataset" --save-dir "checkpoints/${GRAMMAR}/${SPLIT}-transformer" --arch transformer_lm_gpt_base --share-decoder-input-output-embed --dropout 0.3 --optimizer adam --adam-betas '(0.9,0.98)' --weight-decay 0.01 --lr 0.0005 --lr-scheduler inverse_sqrt --wandb-project xiulin-yang-compling  --warmup-updates 500 --clip-norm 0.0 --batch-size 128 --warmup-init-lr 1e-07 --tokens-per-sample 128 --sample-break-mode none --max-tokens 2048  --update-freq 16 --patience 5 --max-update 5000 --no-epoch-checkpoints --no-last-checkpoints --log-format simple --log-interval 1
echo "split: $SPLIT"
fairseq-eval-lm "data-bin/${GRAMMAR}/${SPLIT}-dataset" --path "checkpoints/${GRAMMAR}/${SPLIT}-transformer/checkpoint_best.pt" --tokens-per-sample 24 --gen-subset "valid" --output-word-probs --quiet 2> "trans-results/${GRAMMAR}.${SPLIT}.dev.txt"

fairseq-eval-lm "data-bin/${GRAMMAR}/${SPLIT}-dataset" --path "checkpoints/${GRAMMAR}/${SPLIT}-transformer/checkpoint_best.pt" --tokens-per-sample 24 --gen-subset "test" --output-word-probs --quiet 2> "trans-results/${GRAMMAR}.${SPLIT}.test.txt"
python get_sentence_scores.py -i "trans-results/${GRAMMAR}.${SPLIT}.test.txt" -O "trans_sentence_scores/"

fairseq-eval-lm "data-bin/${GRAMMAR}/correct_${SPLIT}-dataset" --path "checkpoints/${GRAMMAR}/${SPLIT}-transformer/checkpoint_best.pt" --tokens-per-sample 24 --gen-subset "test" --output-word-probs --quiet 2> "trans-results/${GRAMMAR}.correct_${SPLIT}.test.txt"
python get_sentence_scores.py -i "trans-results/${GRAMMAR}.correct_${SPLIT}.test.txt" -O "trans_sentence_scores/"

fairseq-eval-lm "data-bin/${GRAMMAR}/incorrect_${SPLIT}-dataset" --path "checkpoints/${GRAMMAR}/${SPLIT}-transformer/checkpoint_best.pt" --tokens-per-sample 24 --gen-subset "test" --output-word-probs --quiet 2> "trans-results/${GRAMMAR}.incorrect_${SPLIT}.test.txt"
python get_sentence_scores.py -i "trans-results/${GRAMMAR}.incorrect_${SPLIT}.test.txt" -O "trans_sentence_scores/"
