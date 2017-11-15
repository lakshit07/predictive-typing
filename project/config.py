import re
from collections import defaultdict

delimiters = ","," ","\n"
regexPattern = '|'.join(map(re.escape, delimiters))
unigram = defaultdict(lambda: 0)
bigram = defaultdict(lambda: 0)
trigram = defaultdict(lambda: 0)
count_unigram = defaultdict(lambda: 0)
count_bigram = defaultdict(lambda: 0)
count_trigram = defaultdict(lambda: 0)
count_distinct_uni = defaultdict(lambda: 0)
count_distinct_bi = defaultdict(lambda: 0)
voc_size = 0
total_unigrams = 0
