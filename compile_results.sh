#!/bin/bash

#python compile_results.py -f trans-results/fakegrammarexp1 -O trans_scores/fakegrammarexp1_permutation_correct/result.csv -g fakegrammarexp1_permutation_correct
#python compile_results.py -f trans-results/fakegrammarexp1 -O trans_scores/fakegrammarexp1_permutation_incorrect/result.csv -g fakegrammarexp1_permutation_incorrect
#
#python compile_results.py -f trans-results/fakegrammarexp1 -O trans_scores/fakegrammarexp1_correct/result.csv -g fakegrammarexp1_correct
#python compile_results.py -f trans-results/fakegrammarexp1 -O trans_scores/fakegrammarexp1_incorrect/result.csv -g fakegrammarexp1_incorrect

python compile_results.py -f trans-results/fakegrammarexp3 -O trans_scores/fakegrammarexp3/result.csv -g fakegrammarexp3
python compile_results.py -f trans-results/fakegrammarexp3 -O trans_scores/fakegrammarexp3_permutation/result.csv -g fakegrammarexp3_permutation

#python compile_results.py -f trans-results/fakegrammarexp3 -O trans_scores/fakegrammarexp3_permutation_correct/result.csv -g fakegrammarexp3_permutation_correct
#python compile_results.py -f trans-results/fakegrammarexp3 -O trans_scores/fakegrammarexp3_permutation_incorrect/result.csv -g fakegrammarexp3_permutation_incorrect
