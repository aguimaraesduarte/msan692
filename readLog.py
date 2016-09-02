import sys
import re
import collections

filename = sys.argv[1]
f = open(filename, "r")
lines = f.readlines()
f.close()

records = []
for line in lines:
    ip = re.findall('^.*? ', line)
    ip = ip[0].strip()
    # print ip
    date_brackets = re.findall('\\[.*?\\]', line)
    date = date_brackets[0]
    date = date[1:len(date)-1]
    # print date
    quoted_strings = re.findall('".*?"', line)
    quoted_strings = [s[1:len(s)-1] for s in quoted_strings]
    # print quoted_strings
    records.append( [ip,date]+quoted_strings )

counter_ip = collections.Counter()
gets = collections.Counter()
for r in records:
	counter_ip[r[0]] += 1
	if 'GET' in r[2]:
		gets[r[2].split('GET ')[1]] += 1

print counter_ip
print gets