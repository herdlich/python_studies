with open('stop_words.txt') as f_stop:
    l_stop = [line.strip() for line in f_stop]

with open('data.txt','r') as f:
    l = [line.strip() for line in f if line.strip() not in l_stop]

print(*l, sep='\n')