nums = {'pow1': 0, 'pow2':0, 'pow3':0, 'pow4':0, 'pow5':0, 'pow6':0, 'pow7':0, 'pow8':0, 'pow9':0, '1k':0, '2k':0, '4k':0, '8k':0, '16k':0 }
with open('c_mod.csv') as f:
    for line in f:
        line.strip()
	val = int(line)
	if 0 <= val <=2:
	    nums['pow1'] +=1
        else:
            pass

print nums