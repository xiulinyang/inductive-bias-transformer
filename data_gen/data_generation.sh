#!/bin/bash
#set -euo pipefail

num_function="${1:?Usage: $0 <num_function>}"

out_dir="grammar/grammar_close_then_open_${num_function}"
perm_dir="${out_dir}_permutation"

reverse_dir="${out_dir}_reverse"
reverse_perm_dir="${reverse_dir}_permutation"

out_dir_r="${out_dir}_r"
perm_dir_r="${out_dir_r}_permutation"

reverse_dir_r="${reverse_dir}_r"
reverse_perm_dir_r="${reverse_dir_r}_permutation"

mkdir -p "$out_dir" "$perm_dir" "$out_dir_r" "$perm_dir_r" \
         "$reverse_dir" "$reverse_perm_dir" "$reverse_dir_r" "$reverse_perm_dir_r"

if [[ "$num_function" -eq 3 ]]; then
  python sample_sentences.py \
    -g "grammar_close_then_open_${num_function}.gr" \
    -n 100000 \
    -O "${out_dir}/" \
    -b
  python sample_sentences.py \
  -g "grammar_close_then_open_${num_function}_reverse.gr" \
  -n 100000 \
  -O "${reverse_dir}/" \
  -b


  python postprocess.py \
    -i "${out_dir}/grammar_close_then_open_${num_function}_b.txt" \
    -o "${out_dir}/grammar_close_then_open_${num_function}.txt"

  python postprocess.py \
  -i "${reverse_dir}/grammar_close_then_open_${num_function}_reverse_b.txt" \
  -o "${reverse_dir}/grammar_close_then_open_${num_function}_reverse.txt"

fi



if [[ "$num_function" -ne 3 ]]; then
  python add_function_words_to_sents.py \
  -s "grammar/grammar_close_then_open_3/grammar_close_then_open_3_b.txt" \
  -g "grammar_close_then_open_${num_function}"

   python add_function_words_to_sents.py \
  -s "grammar/grammar_close_then_open_3_reverse/grammar_close_then_open_3_reverse_b.txt" \
  -g "grammar_close_then_open_${num_function}_reverse" -rv
fi

python add_function_words_to_sents.py \
  -s "grammar/grammar_close_then_open_3/grammar_close_then_open_3_b.txt" \
  -g "grammar_close_then_open_${num_function}" -r

python add_function_words_to_sents.py \
  -s "grammar/grammar_close_then_open_3_reverse/grammar_close_then_open_3_reverse_b.txt" \
  -g "grammar_close_then_open_${num_function}_reverse" -r -rv

python permute_sentences.py \
  -s "grammar/grammar_close_then_open_3/grammar_close_then_open_3_b.txt" \
  -g "grammar_close_then_open_${num_function}"

python permute_sentences.py \
  -s "grammar/grammar_close_then_open_3_reverse/grammar_close_then_open_3_reverse_b.txt" \
  -g "grammar_close_then_open_${num_function}_reverse"


python make_splits.py -s "${out_dir}/grammar_close_then_open_${num_function}.txt" -O .
python make_splits.py -s "${out_dir_r}/grammar_close_then_open_${num_function}_r.txt" -O .
python make_splits.py -s "${perm_dir}/grammar_close_then_open_${num_function}_permutation.txt" -O .

python make_splits.py -s "${reverse_dir}/grammar_close_then_open_${num_function}_reverse.txt" -O .
python make_splits.py -s "${reverse_dir_r}/grammar_close_then_open_${num_function}_reverse_r.txt" -O .
python make_splits.py -s "${reverse_perm_dir}/grammar_close_then_open_${num_function}_reverse_permutation.txt" -O .

echo "Finish."