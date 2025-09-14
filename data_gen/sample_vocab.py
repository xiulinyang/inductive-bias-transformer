from pathlib import Path
from random import sample

adjectives = Path('english/adj.txt').read_text().strip().split('\n')
nounp = Path('english/nounp.txt').read_text().strip().split('\n')
nouns = Path('english/nouns.txt').read_text().strip().split('\n')
verbs = Path('english/verb.txt').read_text().strip().split('\n')

adjs = sample(adjectives, 200)
nps = sample(nounp, 200)
nss = sample(nouns, 200)
vbs = sample(verbs, 800)

ivbs = vbs[:200]
ivbps = vbs[200:400]
tvbs = vbs[400:600]
tvbps = vbs[600:]

print(len(ivbs), len(ivbps), len(tvbs), len(tvbps))
with open('grammar_close_then_open.gr' ,'a') as grammar:
    for adj in adjs:
        grammar.write(f'1\tAdj\t{adj}\n')
    grammar.write('\n\n')

    for np in nps:
        grammar.write(f'1\tSNoun_P\t{np}\n')
    grammar.write('\n\n')

    for ns in nss:
        grammar.write(f'1\tSNoun_S\t{ns}\n')
    grammar.write('\n\n')

    for ivb in ivbs:
        grammar.write(f'1\tIVerb_S\t{ivb}\n')
    grammar.write('\n\n')

    for ivp in ivbps:
        grammar.write(f'1\tIVerb_P\t{ivp}\n')
    grammar.write('\n\n')
    for tvb in tvbs:
        grammar.write(f'1\tTVerb_S\t{tvb}\n')
    grammar.write('\n\n')
    for tvp in tvbps:
        grammar.write(f'1\tTVerb_P\t{tvp}\n')
    grammar.write('\n\n')



