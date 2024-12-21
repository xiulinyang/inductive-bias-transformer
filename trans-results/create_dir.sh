#!/bin/bash

mkdir -p fakegrammarexp3/fakegrammarexp3_correct
mkdir -p fakegrammarexp3/fakegrammarexp3_incorrect
mkdir -p fakegrammarexp3/fakegrammarexp3_permutation_correct
mkdir -p fakegrammarexp3/fakegrammarexp3_permutation_incorrect


mv fakegrammarexp3/fakegrammarexp3_permutation/*.correct*.txt  fakegrammarexp3/fakegrammarexp3_permutation_correct/
mv fakegrammarexp3/fakegrammarexp3_permutation/*.incorrect*.txt fakegrammarexp3/fakegrammarexp3_permutation_incorrect/
#mv fakegrammarexp3/fakegrammarexp2_permutation/*.correct*.txt  fakegrammarexp2/fakegrammarexp2_permutation_correct/
#mv fakegrammarexp3/fakegrammarexp2_permutation/*.incorrect*.txt fakegrammarexp2/fakegrammarexp2_permutation_incorrect/


#mv fakegrammarexp3/fakegrammarexp3/*.correct*.txt  fakegrammarexp3/fakegrammarexp3_correct/
#mv fakegrammarexp3/fakegrammarexp3/*.incorrect*.txt fakegrammarexp3/fakegrammarexp3_incorrect/
#mv fakegrammarexp2/fakegrammarexp2/*.correct*.txt  fakegrammarexp2/fakegrammarexp2_correct/
#mv fakegrammarexp2/fakegrammarexp2/*.incorrect*.txt fakegrammarexp2/fakegrammarexp2_incorrect/