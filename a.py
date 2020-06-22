#!/usr/bin/env python
import subprocess

BIB = {}

with open('./ref.bib', 'r') as f:
    content = f.readlines()
    article = 'preamble'
    BIB[article] = []
    for line in content:
        if line:
            line = line.lstrip(' ')
            if line[0] == '@':
                article = line[9:-1]
                if article in BIB:
                    print(article)
                BIB[article] = [line]
            elif line[0] in ['%', '}']:
                BIB[article].append(line)
            else:
                if len(line.split('=')) == 1:
                    line = ' '*8 + line
                else:
                    line = ' '*4 + line
                BIB[article].append(line)

articles = list(BIB.keys())
duplicate = ''.join([''.join(BIB[article]) for article in articles])

with open('./ref.bib', 'w') as f:
    f.write(duplicate)

subprocess.check_call(['cp', './ref.bib', './Biblio/ref.bib'])
