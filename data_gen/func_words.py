from pathlib import Path

def get_function_words(num):
    num = max(0, num - 3)
    dets = [x.split()[-1] for x in Path('english/dets.txt').read_text().splitlines()][:num] + ['an', 'a', 'the']
    preps = [x.split()[-1] for x in Path('english/prep.txt').read_text().splitlines()][:num] + ['on', 'at', 'in']
    suffx = [x.split()[-1] for x in Path('english/suffix.txt').read_text().splitlines()][:num] + ['-ed', '-s', '-es']
    return suffx, dets, preps

SUFF30, DETS30, PREPS30 = get_function_words(30)
SUFF50, DETS50, PREPS50 = get_function_words(50)
SUFF60, DETS60, PREPS60 = get_function_words(60)
FUNC_WORDS = {
    'grammar_close_then_open_3_r': {2: {'Vaff': ['-ed', '-s', '-es']},
                                  3: {'Det': ['an', 'a', 'the']}, 4: {'Prep': ['on', 'at', 'in']}},
    'grammar_close_then_open_3': {2: {'Vaff': ['-ed', '-s', '-es']}, 3: {'Det': ['an', 'a', 'the']}, 4: {'Prep': ['on', 'at', 'in']}},
    'grammar_close_then_open_30':  {2: {'Vaff': SUFF30},  3: {'Det': DETS30},  4: {'Prep': PREPS30}},
    'grammar_close_then_open_50': {2: {'Vaff': SUFF50}, 3: {'Det': DETS50}, 4: {'Prep': PREPS50}},
    'grammar_close_then_open_60': {2: {'Vaff': SUFF60}, 3: {'Det': DETS60}, 4: {'Prep': PREPS60}},
    # 'grammar_close_then_open_long': {1: {'Comp': [ ]}, 2: {'Vaff': []}, 3: {'Det': []}, 4: {'Prep': []}},
    'grammar_close_then_open_30_r':  { 2: {'Vaff': SUFF30},  3: {'Det': DETS30},  4: {'Prep': PREPS30}},
    'grammar_close_then_open_50_r': {2: {'Vaff': SUFF50}, 3: {'Det': DETS50},
                                       4: {'Prep': PREPS50}},
    'grammar_close_then_open_60_r': {2: {'Vaff': SUFF60}, 3: {'Det': DETS60}, 4: {'Prep': PREPS60}},

    'grammar_close_then_open_3_reverse_r': {2: {'Vaff': ['-ed', '-s', '-es']},
                                  3: {'Det': ['an', 'a', 'the']}, 4: {'Prep': ['on', 'at', 'in']}},
    'grammar_close_then_open_3_reverse': {2: {'Vaff': ['-ed', '-s', '-es']}, 3: {'Det': ['an', 'a', 'the']}, 4: {'Prep': ['on', 'at', 'in']}},
    'grammar_close_then_open_30_reverse':  {2: {'Vaff': SUFF30},  3: {'Det': DETS30},  4: {'Prep': PREPS30}},
    'grammar_close_then_open_50_reverse': {2: {'Vaff': SUFF50}, 3: {'Det': DETS50}, 4: {'Prep': PREPS50}},
    'grammar_close_then_open_60_reverse': {2: {'Vaff': SUFF60}, 3: {'Det': DETS60}, 4: {'Prep': PREPS60}},
    # 'grammar_close_then_open_long': {1: {'Comp': [ ]}, 2: {'Vaff': []}, 3: {'Det': []}, 4: {'Prep': []}},
    'grammar_close_then_open_30_reverse_r':  { 2: {'Vaff': SUFF30},  3: {'Det': DETS30},  4: {'Prep': PREPS30}},
    'grammar_close_then_open_50_reverse_r': {2: {'Vaff': SUFF50}, 3: {'Det': DETS50},
                                       4: {'Prep': PREPS50}},
    'grammar_close_then_open_60_reverse_r': {2: {'Vaff': SUFF60}, 3: {'Det': DETS60}, 4: {'Prep': PREPS60}},

# 'grammar_close_then_open_150': {1: {'Comp': COMPS150}, 2: {'Vaff': SUFF150}, 3: {'Det': DETS150}, 4: {'Prep': PREPS150}},
}