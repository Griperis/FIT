#!/usr/bin/env python3

import fileinput

words = []
for line in fileinput.input():
    words.append(line.rstrip())
#if checking whether something is present or not, its better to use set
words = set(words)
palindroms = [w for w in words if w == w[::-1]]
#palindroms = set(palindroms)
result = [w for w in words if w not in palindroms and w[::-1] in words]

print(sorted(result))
