import StringIO
import urllib
import zipfile
import re

zip_file = zipfile.ZipFile(StringIO.StringIO(urllib.urlopen('http://www.pythonchallenge.com/pc/def/channel.zip').read()))

def next(nothing):
    nothing_number = zip_file.read('%s.txt' % nothing)
    m = re.match('Next nothing is ([0-9]+)', nothing_number)
    if not m:
        print nothing_number
        return 0
    return m.group(1)

chain_files = []
nothing = 90052
for i in range(len(zip_file.namelist())):
    chain_files.append(nothing)
    if next(nothing) is 0:
        break
    nothing = next(nothing)

print chain_files

for nothing in chain_files:
    print zip_file.getinfo('%s.txt' % nothing).comment


print ''.join([zip_file.getinfo('%s.txt' % nothing).comment for nothing in chain_files])
