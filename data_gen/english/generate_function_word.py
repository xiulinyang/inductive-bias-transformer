from wuggy import WuggyGenerator
from tqdm import tqdm
prep = ['at', 'on', 'in', 'for']
dets = ['an', 'a', 'the', 'this']
suffix = ['as', 'ad','is', 'is']
comps = ['that', 'which', 'who', 'why']

func_words = [(prep, 'prep.txt', 'Prep'), (dets, 'dets.txt','Det'), (comps, 'comps.txt','Comp'), (suffix, 'suffix.txt','Vaff')]
g = WuggyGenerator()
g.load("orthographic_english")

all_pwords = []
for f_cat, f_p, cat_name in tqdm(func_words):
    with open(f_p, 'w') as f:
        for match in g.generate_classic(f_cat,ncandidates_per_sequence=30):
            generated_word = match["pseudoword"]
            if match["pseudoword"] not in all_pwords:
                f.write(f'1\t{cat_name}\t{generated_word}\n')

