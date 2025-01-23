#!/bin/bash
 
python compile_results.py -m trans -g gn_grammarexp1_permutation_correct
python compile_results.py -m trans -g gn_grammarexp1_permutation_incorrect

python compile_results.py -m trans -g gn_grammarexp1_correct
python compile_results.py -m trans -g gn_grammarexp1_incorrect

python compile_results.py -m trans -g gn_grammarexp1
python compile_results.py -m trans -g gn_grammarexp1_permutation


python compile_results.py -m trans -g gn_grammarexp2_permutation_correct
python compile_results.py -m trans -g gn_grammarexp2_permutation_incorrect

python compile_results.py -m trans -g gn_grammarexp2_correct
python compile_results.py -m trans -g gn_grammarexp2_incorrect

python compile_results.py -m trans -g gn_grammarexp2
python compile_results.py -m trans -g gn_grammarexp2_permutation

python compile_results.py -m trans -g gn_grammarexp3_permutation_correct
python compile_results.py -m trans -g gn_grammarexp3_permutation_incorrect

python compile_results.py -m trans -g gn_grammarexp3_correct
python compile_results.py -m trans -g gn_grammarexp3_incorrect

python compile_results.py -m trans -g gn_grammarexp3
python compile_results.py -m trans -g gn_grammarexp3_permutation


python compile_results.py -m trans -g grammar42exp1
python compile_results.py -m trans -g grammar42exp1_permutation

python compile_results.py -m trans -g grammar41exp1
python compile_results.py -m trans -g grammar41exp1_permutation

python compile_results.py -m trans -g grammar53exp1
python compile_results.py -m trans -g grammar53exp1_permutation