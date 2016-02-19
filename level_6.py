import StringIO
import urllib
import zipfile
import re

zip_file = zipfile.ZipFile(StringIO.StringIO(urllib.urlopen('http://www.pythonchallenge.com/pc/def/channel.zip').read()))

def next(nothing):
    nothing_number = zip_file.read('%s.txt' % nothing)
    m = re.match('Next nothing is ([0-9]+)', nothing_number)
    if not m:
        return 0
    return m.group(1)

comments = ""
nothing = 90052
for i in range(len(zip_file.namelist())):
    comments += zip_file.getinfo('%s.txt' % nothing).comment
    if next(nothing) is 0:
        break
    nothing = next(nothing)

print comments
