from conllu import parse
from tqdm import tqdm
from glob import glob
from pathlib import Path

noun_s=[]
noun_p=[]
adj=[]
verb = []

gum_tb = Path('/Users/xiulinyang/Downloads/en_gum-ud-train.conllu').read_text().strip().split('\n\n')
for sent in gum_tb:
    parsed_sent = parse(sent)[0]
    for word in parsed_sent:
        word_form = word['form'].lower()
        if not word_form[0].isnumeric():
            if word['upos'] == 'NOUN':
                if 'Number' in word['feats']:
                    if word['feats']['Number'] == 'Sing' and len(word_form)>4:
                        noun_s.append(word_form)
                    elif word['feats']['Number'] == 'Plur' and len(word_form)>4:
                        noun_p.append(word_form)
                    else:
                        continue
            elif word['upos'] == 'ADJ' and len(word_form)>4:
                adj.append(word_form)
            elif word['upos'] == 'VERB' and len(word_form)>4:
                verb.append(word_form)

print(len(set(noun_s)), len(set(noun_p)), len(set(adj)), len(set(verb)))

noun_s = [x for x in list(set(noun_s)) if x not in noun_p + adj + verb]
noun_p = [x for x in list(set(noun_p)) if x not in noun_s+adj+verb]
verb = [x for x in list(set(verb)) if x not in noun_s+adj+noun_p]
adj = [x for x in list(set(adj)) if x not in noun_s+noun_p+verb]

print(len(noun_s), len(noun_p), len(verb), len(adj))
with (open('adj.txt', 'w') as adj_f, open('nouns.txt', 'w') as nouns_f,
      open('verb.txt', 'w') as verb_f, open('nounp.txt', 'w') as nounp_f):
    adj_f.write('\n'.join(adj))
    nouns_f.write('\n'.join(noun_s))
    nounp_f.write('\n'.join(noun_p))
    verb_f.write('\n'.join(verb))
