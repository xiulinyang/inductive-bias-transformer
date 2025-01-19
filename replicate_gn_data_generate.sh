#!/bin/bash

python replicate_gn.py gn_grammarexp1
python replicate_gn.py gn_grammarexp2
python replicate_gn.py gn_grammarexp3


python generate_test_gn.py gn_grammarexp1
python generate_test_gn.py gn_grammarexp2
python generate_test_gn.py gn_grammarexp3