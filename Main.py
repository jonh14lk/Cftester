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

file = sys.argv[1]
code = sys.argv[2]
problem = sys.argv[3]
url = url + code + pos + problem
req = Request(url)
response = urlopen(req)
page = response.read()
soup = BeautifulSoup(page, 'html.parser')
p = soup.findAll('pre')
q = len(p)
index = 1

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
    pathe = '/home/joao/Área de Trabalho/Cftester/' + str(index) + '.in'
    f = open(pathe , 'w')
    for j in In:
      y = j.replace('\n', '')
      if(y != '' and y != ' '):
        f.write(y + '\n')
    f.close()
    print('')
    print('Test:' , index)
    com = 'g++ ' + file + ' -o main' ;
    comm = './main <' + str(index) + '.in'
    os.system(com)
    os.system(comm)
    index = index + 1
