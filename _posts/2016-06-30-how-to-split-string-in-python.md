---
layout: post
title: "How to split string in Python?"
date: 2016-06-30 09:20:00 +0000
categories: [Python]
tags: [python, string, split, regex]
author: "Daniel Dai"
reading_time: 5
---

## Split string with identical separator

```python
path = '45.63.130.248:15+221.160.226.9:329+101.240.154.40:1197'

nodes = path.split('+')

print nodes
```

    ['45.63.130.248:15', '221.160.226.9:329', '101.240.154.40:1197']



```python
path = '45.63.130.248:15*+221.160.226.9:329*+101.240.154.40:1197'

nodes = path.split('*+') # separator can have more than one charactor

print nodes
```

    ['45.63.130.248:15', '221.160.226.9:329', '101.240.154.40:1197']


## Split string with non-identical separator

```python
ticket_key = '45.63.120.248:1195&221.160.226.9:329^101.240.154.40:1197'
# how about this one? It has 2 diffrent separators '&' and '^'

node1 = ticket_key.split('&')[0]
node2 = ticket_key.split('&')[1].split('^')[0]
node3 = ticket_key.split('&')[1].split('^')[1]

print node1, node2, node3
```

    45.63.120.248:1195 221.160.226.9:329 101.240.154.40:1197



```python
# A more elegent way, is to use the re.split()
import re

ticket_key = '45.63.120.248:1195&221.160.226.9:329^101.240.154.40:1197'

nodes = re.split('[&\^]', ticket_key)
print nodes
```

    ['45.63.120.248:1195', '221.160.226.9:329', '101.240.154.40:1197']
