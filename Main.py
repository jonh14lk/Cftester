from bs4 import BeautifulSoup
from urllib.request import Request
from urllib.request import urlopen
import subprocess
import os
import sys
from os.path import expanduser

home = expanduser('~')
url = 'http://www.codeforces.com/contest/'
pos = '/problem/'

print('------------------')
print('|    cftester    |')
print('------------------')  
print('')                                                                                                                                                                  
print('Contest code:')
code = input()
print('Problem:')
problem = input()

url = url + code + pos + problem
req = Request(url)
response = urlopen(req)
page = response.read()
soup = BeautifulSoup(page, 'html.parser')
p = soup.findAll('pre')
q = len(p)
inde = 1

for i in range(q):
  if(i % 2 == 0):
    In = str(p[i])
    In = In.replace('<pre>','').replace('</pre>','')
    In = In.replace('&gt;','>')
    In = In.replace('&lt;','<')
    In = In.replace('&quot;','"')
    In = In.replace('&amp;','&')
    In = In.replace('<br />','\n')
    In = In.replace('<br/>','\n')
    In = In.replace('</ br>','\n')
    In = In.replace('</br>','\n')
    In = In.replace('<br>','\n')
    In = In.replace('< br>','\n')
    In = In.split('\n')
    pathe = '/Área de Trabalho/Cftester/' + str(inde) + '.in'
    f = open(home + pathe , 'w')
    for j in In:
      y = j.replace('\n', '')
      if(y != '' and y != ' '):
        f.write(y + '\n')
    f.close()
    print('')
    print('Test:' , inde)
    os.system("g++ a.cpp -o a")
    comm = "./a <"
    comm = comm + str(inde) + '.in'
    os.system(comm)
    inde = inde + 1