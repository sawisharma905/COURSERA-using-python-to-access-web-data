import re

sample_file=open("week2text.txt")

x=sample_file.read()

num_regex='[0-9]+'

f=re.findall(num_regex,x)

total=sum(int(num) for num in f)

print(total)

sample_file.close()

