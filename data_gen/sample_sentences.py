import argparse
import os
import random


class PCFG:
    """
    PCFG to sample sentences from
    """
    def __init__(self, grammar_file):
        self.rules = None
        self.change_rules = None
        self.load_rules(grammar_file)

    def load_rules(self, grammar_file):
        new_rules = {}
        change = {}
        g_file = open(grammar_file, 'r')
        lines = g_file.readlines()
        for l in lines:
            if l.startswith(('#', " ", "\t", "\n")) or len(l) < 1:
                continue
            else:
                if l.find("#") != -1:
                    l = l[:l.find("#")]
                idx = -1
                if len(l.rstrip().split("\t")) == 3:
                    weight, lhs, rhs = l.rstrip().split("\t")
                elif len(l.rstrip().split("\t")) == 4:
                    weight, lhs, rhs, idx = l.rstrip().split("\t")
                if lhs not in new_rules.keys():
                    new_rules[lhs] = []
                poss_rhs = new_rules[lhs]
                poss_rhs.append([rhs, float(weight)])
                if idx != -1:
                    change[lhs + "\t" + rhs] = idx
        for lhs, poss in new_rules.items():
            total = 0
            for rhs in poss:
                total += rhs[1]
            for rhs in poss:
                rhs[1] /= total
        self.rules = new_rules
        self.change_rules = change

    def sample_sentence(self, max_expansions, bracketing):
        self.expansions = 0
        done = False
        sent = ["ROOT"]
        idx = 0
        while not done:
            if sent[idx] not in self.rules.keys():
                idx += 1
                if idx >= len(sent):
                    done = True
                continue
            else:
                replace, change_idx = self.expand(sent[idx])
                if bracketing:
                    if change_idx == -1:
                        sent = (sent[:idx]
                            + ["(", sent[idx]] + replace + [")"]
                            + sent[idx + 1:])
                        # print(sent)
                    else:
                        sent = (sent[:idx]
                            + ["(", change_idx + sent[idx]] + replace + [")"]
                            + sent[idx + 1:])
                        # print(sent)
                else:
                    sent = sent[:idx] + replace  + sent[idx + 1:]

                self.expansions += 1
                if bracketing:
                    idx += 2
                if self.expansions > max_expansions:
                    done = True
                if idx >= len(sent):
                    done = True
        # print('final')
        # print(sent)
        if self.expansions > max_expansions:
            for idx in range(len(sent)):
                if not bracketing:
                    if sent[idx] in self.rules.keys():
                        sent[idx] = "..."
                else:
                    if sent[idx] in self.rules.keys() and sent[idx - 1] != "(":
                        sent[idx] = "..."
        # print('wtf::::')
        # print(' '.join(sent))
        return ' '.join(sent)

    def expand(self, symbol):
        poss = self.rules[symbol]
        sample = random.random()
        val = 0.0
        rhs = ""
        idx = -1
        for p in poss:
            val += p[1]
            if sample <= val:
                if symbol + "\t" + p[0] in self.change_rules.keys():
                    idx = self.change_rules[symbol + "\t" + p[0]]
                rhs = p[0]
                break
        return rhs.split(), idx



def sample_sentences(grammar_file, n, m, output_folder, bracketing):
    sents =[]
    if not os.path.exists(output_folder):
            os.mkdir(output_folder)
    grammar_name = grammar_file[:-3].split("/")[-1]
    output_file = open(os.path.join(output_folder, grammar_name + "_b.txt") , 'w')
    grammar = PCFG(grammar_file)
    for i in range(n):
        sents.append(grammar.sample_sentence(m, bracketing))
    #     print('hhhhhhhhhhhhhh')
    #     print(grammar.sample_sentence(m, bracketing))
    #     # output_file.write(grammar.sample_sentence(m, bracketing) + "\n")
    # print('helo:')
    # print(sents)
    output_file.write('\n'.join(sents))

parser = argparse.ArgumentParser(description="Sample sentences from PCFG")

parser.add_argument("-g", "--grammar_file", type=str, default='',
    help="Path to grammar file")
parser.add_argument("-n", "--number_samples", type=int, required=True, 
    help="Number of sentences to sample")
parser.add_argument("-m", "--max_expansions", type=int, default=600,
    help="Max number of expansions performed")
parser.add_argument("-O", "--output_folder", type=str, 
    help="Location of output files")
parser.add_argument("-b", "--bracketing", action='store_true',
    help="Include bracketing of constituents")
parser.add_argument("-s", "--random_seed", type=int, default=42,
    help="Include bracketing of constituents")

args = parser.parse_args()
random_seed = args.random_seed
random.seed(random_seed)
if args.grammar_file == '':
    print("Please provide grammar files")
elif args.grammar_file != '':
    sample_sentences(args.grammar_file, args.number_samples, 
        args.max_expansions, args.output_folder, args.bracketing)