#!/usr/bin/python

import math

# subprogram definitions
def avg(pct_list):
    return sum(pct_list) / len(pct_list)

def std(pct_list):
    n = len(pct_list)
    if n <= 1: return 0 # evade divide by zero
    m = avg(pct_list)
    s = 0.
    for x in pct_list:
        s += (x - m)**2
    return math.sqrt(s / (n - 1))

def med(pct_list):
    n = len(pct_list)
    s = sorted(pct_list)
    if n%2 is not 0:
        return s[n/2]
    else:
        return (s[n/2-1]+s[n/2])/2

def mad(pct_list):
    n = len(pct_list)
    m = med(pct_list)
    dev = []
    for x in pct_list:
        dev.append(abs(x-m))
    return med(dev)

def compute_table(state_pcts, party):
    table = {}
    for state in sorted(state_pcts):
        pct_list = state_pcts[state][party]
        table[state] = {}
        table[state]['min'] = min(pct_list)
        table[state]['max'] = max(pct_list)
        table[state]['avg'] = avg(pct_list)
        table[state]['std'] = std(pct_list)
        table[state]['med'] = med(pct_list)
        table[state]['mad'] = mad(pct_list)
    return table 

def print_table(table, party):
    print
    print party + ' %'
    print '{:20}'.format('state'),
    print '{:>8}'.format('min'),
    print '{:>8}'.format('max'),
    print '{:>8}'.format('avg'),
    print '{:>8}'.format('std'),
    print '{:>8}'.format('med'),
    print '{:>8}'.format('mad')
    for state in sorted(table):
        if state is 'U. S.': continue
        print '{:20}'.format(state),
        print format(table[state]['min'], '8.2f'),
        print format(table[state]['max'], '8.2f'),
        print format(table[state]['avg'], '8.2f'),
        print format(table[state]['std'], '8.2f'),
        print format(table[state]['med'], '8.2f'),
        print format(table[state]['mad'], '8.2f')
    print '{:20}'.format('U. S.'),
    print format(table['U. S.']['min'], '8.2f'),
    print format(table['U. S.']['max'], '8.2f'),
    print format(table['U. S.']['avg'], '8.2f'),
    print format(table['U. S.']['std'], '8.2f'),
    print format(table['U. S.']['med'], '8.2f'),
    print format(table['U. S.']['mad'], '8.2f')


def print_sorted_stats(table, party, stat):
    print
    print party + ' % sorted by ' + stat
    print '{:20}'.format('state'),
    print '{:>8}'.format('min'),
    print '{:>8}'.format('max'),
    print '{:>8}'.format('avg'),
    print '{:>8}'.format('std'),
    print '{:>8}'.format('med'),
    print '{:>8}'.format('mad')
    for key, value in sorted(table.items(), key=lambda item: item[1][stat]):
        print '{:20}'.format(key),
        print format(value['min'], '8.2f'),
        print format(value['max'], '8.2f'),
        print format(value['avg'], '8.2f'),
        print format(value['std'], '8.2f'),
        print format(value['med'], '8.2f'),
        print format(value['mad'], '8.2f')

# main program
state_pcts = {}
i = 0
infile = open('statepcts.dat', 'r')
for line in infile:
    state = line[:20].strip()
    if state not in state_pcts: 
        state_pcts[state] = {}
        state_pcts[state]['Democratic'] = []
        state_pcts[state]['Republican'] = []
        state_pcts[state]['Other'] = []
    fields = line[22:].split()
    state_pcts[state]['Democratic'].append(float(fields[0]))
    state_pcts[state]['Republican'].append(float(fields[1]))
    state_pcts[state]['Other'].append(float(fields[2]))
infile.close()

# processing
democratic_table = compute_table(state_pcts, 'Democratic')
republican_table = compute_table(state_pcts, 'Republican')
other_table = compute_table(state_pcts, 'Other')

# output tables
print_table(democratic_table, 'Democratic')
print_table(republican_table, 'Republican')
print_table(other_table, 'Other')

stat_list = [ 'min', 'max', 'avg', 'std', 'med', 'mad' ]

for stat in stat_list: print_sorted_stats(democratic_table, 'Democratic', stat)
for stat in stat_list: print_sorted_stats(republican_table, 'Republican', stat)
for stat in stat_list: print_sorted_stats(other_table, 'Other', stat)
