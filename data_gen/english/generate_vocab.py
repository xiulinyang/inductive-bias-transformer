from pathlib import Path
close_class = ['a', 'the', 'one', 'my', 'your', 'this', 'an', 'her', 'his', 'dank'] + ['institutionalise', 'internationalise', 'black-and-white', 'well-documented', 'intellectualise', 'departmentalise', 'inconsequential', 'impressionable', 'counterbalance', 'happy-go-lucky']
filtered_vocab = [x for x in set(Path('vocab_source.txt').read_text().strip().split('\n')) if x not in close_class and ' ' not in x and not x.endswith('ze') and x.isalpha() and len(x)>3]

with open('vocab_source_filtered.txt', 'w') as f:
    f.write('\n'.join(filtered_vocab))
