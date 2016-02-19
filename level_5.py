import pickle

with open('banner.p', 'rb') as handle:
  b = pickle.load(handle)

for c in b:
    line = ""
    for a in c:
        output =""
        for count in range(0,a[1]):
            output += a[0];
        line += output
    print line
