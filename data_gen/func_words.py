from pathlib import Path

def get_function_words(num):
    num = max(0, num - 3)
    dets = [x.split()[-1] for x in Path('data_gen/english/dets.txt').read_text().splitlines()][:num] + ['an', 'a', 'the']
    comps = [x.split()[-1] for x in Path('data_gen/english/comps.txt').read_text().splitlines()][:num] + ['that', 'which', 'who']
    preps = [x.split()[-1] for x in Path('data_gen/english/prep.txt').read_text().splitlines()][:num] + ['on', 'at', 'in']
    suffx = [x.split()[-1] for x in Path('data_gen/english/suffix.txt').read_text().splitlines()][:num] + ['-ed', '-s', '-es']
    return comps, suffx, dets, preps

COMPS50, SUFF50, DETS50, PREPS50 = get_function_words(50)
COMPS100, SUFF100, DETS100, PREPS100 = get_function_words(100)
COMPS150, SUFF150, DETS150, PREPS150 = get_function_words(150)

FUNC_WORDS = {
'grammar_close_then_open': {1: {'Comp': ['that', 'which', 'who']}, 2: {'Vaff': ['-ed', '-s', '-es']}, 3: {'Det': ['an', 'a', 'the']}, 4: {'Prep': ['on', 'at', 'in']}},
    'grammar_close_then_open_50':  {1: {'Comp': COMPS50},  2: {'Vaff': SUFF50},  3: {'Det': DETS50},  4: {'Prep': PREPS50}},
    'grammar_close_then_open_100': {1: {'Comp': COMPS100}, 2: {'Vaff': SUFF100}, 3: {'Det': DETS100}, 4: {'Prep': PREPS100}},
    'grammar_close_then_open_150': {1: {'Comp': COMPS150}, 2: {'Vaff': SUFF150}, 3: {'Det': DETS150}, 4: {'Prep': PREPS150}},
}