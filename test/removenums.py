import os,re

for i in os.listdir():
	os.rename(i,re.sub('[0-9]+\. *','',i))
