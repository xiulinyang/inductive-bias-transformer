#!/bin/bash
python compile_results.py -m trans -o perplexity.csv
python compile_results.py -m lstm -o perplexity.csv

python dep_accuracy.py -m trans -o accuracy.csv
python dep_accuracy.py -m lstm -o accuracy.csv