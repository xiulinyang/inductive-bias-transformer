import string
new_fws = []
for letter1 in list(string.ascii_lowercase):
    for letter2 in list(string.ascii_lowercase):
        new_fws.append(letter1 + letter2)

print(len(new_fws))
new_fws = [x for x in new_fws if x not in ['at', 'on', 'in', 'an', 'ed',
                                           'es']]
print(len(new_fws), len(set(new_fws)))
suffs = [f'-{x}' for x in new_fws[:200]]
preps = new_fws[:200]
dets = new_fws[200:400]
comps = new_fws[400:600]

with (open('prep.txt', 'w') as p_f, open('suffix.txt', 'w') as s_f,
      open('dets.txt', 'w') as d_f, open('comps.txt', 'w') as c_f):
    for p in preps:
        p_f.write(f'1\tPrep\t{p}\n')
    for s in suffs:
        s_f.write(f'1\tVaff\t{s}\n')
    for d in dets:
        d_f.write(f'1\tDet\t{d}\n')
    for c in comps:
        c_f.write(f'1\tComp\t{c}\n')

