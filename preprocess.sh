#!/bin/bash

GRAMMAR=$1

mkdir -p data-bin
mkdir -p checkpoints
mkdir -p lstm-results
mkdir -p trans-results

mkdir -p data-bin/${GRAMMAR}/
for SPLIT in {0..9}; do
  mkdir -p data-bin/${GRAMMAR}/${SPLIT}-dataset
  mkdir -p data-bin/${GRAMMAR}/${SPLIT}

  spm_train --input "data_gen/grammar/${GRAMMAR}/${GRAMMAR}/${SPLIT}.trn" --model_prefix="data-bin/${GRAMMAR}/${SPLIT}/spm" --vocab_size=512 --character_coverage=1.0

  for part in trn dev tst; do
    spm_encode \
      --model "data-bin/${GRAMMAR}/${SPLIT}/spm.model" \
      --output_format=piece \
      < "data_gen/grammar/${GRAMMAR}/${GRAMMAR}/${SPLIT}.${part}" \
      > "data_gen/grammar/${GRAMMAR}/${GRAMMAR}/${SPLIT}/${part}.spm"
      done

  fairseq-preprocess --only-source --trainpref "data_gen/grammar/${GRAMMAR}/${GRAMMAR}/${SPLIT}/trn.spm" --validpref "data_gen/grammar/${GRAMMAR}/${GRAMMAR}/${SPLIT}/dev.spm" --testpref "data_gen/grammar/${GRAMMAR}/${GRAMMAR}/${SPLIT}/tst.spm" --destdir "data-bin/${GRAMMAR}/${SPLIT}-dataset" --workers 10
  done
