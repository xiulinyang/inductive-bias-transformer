from asyncore import write
from glob import glob
import csv
from pathlib import Path
import statistics
# correct_files = sorted(glob('trans_scores/*correct/result.csv'))
all_files = sorted(glob('trans_scores/*/result.csv'))
#
# # Exclude files in paths containing "correct"
excluded_files = [file for file in all_files if 'correct' not in file]
#
#
fieldnames_correct = [ 'grammar', 'tst_av', 'tst_sd']
#
# fieldnames = ['grammar', 'tst_av', 'tst_sd']
#
# correct_output = 'result_correct_incorrect.csv'
# output = 'result_scores.csv'
# with open(correct_output, 'w') as ac:
#     ac.write(','.join(fieldnames_correct))
#     ac.write('\n')
#     for f in correct_files:
#         correct = f.split('/')[1]
#         score = ','.join(Path(f).read_text().strip().split('\n')[-1].split(',')[1:])
#         ac.write(f'{correct},{score}\n')
#
# print(excluded_files)

correct_rate = []
for i in range(10):
    correct = Path(f'/Users/xiulinyang/Desktop/TODO/artificial-languages/trans_sentence_scores_no_end/fakegrammarexp3_permutation/correct_{str(i)}.test.txt').read_text().strip().split('\n')
    incorrect = Path(f'/Users/xiulinyang/Desktop/TODO/artificial-languages/trans_sentence_scores_no_end/fakegrammarexp3_permutation/incorrect_{str(i)}.test.txt').read_text().strip().split('\n')
    c=0
    for c_score, i_score in zip(correct, incorrect):
        if float(c_score)<float(i_score):
            c+=1
    correct_rate.append(c/len(correct))


print(statistics.mean(correct_rate))
print(statistics.stdev(correct_rate))