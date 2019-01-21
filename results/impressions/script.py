import numbers as np
num = {}
for exponent in range(0, 32):
    num[str(2**exponent)] = 0

with open('/home/puneet/scratch/impressions/results/impressions/c_mod.csv') as f:
    count = 0
    for line in f:
        count += 1
        line.strip()
        val = int(line)
        for i in range(1, 32):
            if (2 ** (i - 1) <= val < 2 ** i):
                num[str(2 ** (i - 1))] += 1
                break


for k in sorted(num.iterkeys()):
    print k+','+str(num[k])
