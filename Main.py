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
ans = '' 
ret = ''
CRED3 = '\033[43m'
CRED1 = '\033[42m'
CRED2 = '\033[41m'
CEND =  '\033[0m'

for i in range(q):
    if (i % 2 == 0):
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
        print(CRED3 + 'Test ' + str(index) + CEND)
        print('')
        print('Your Output:')
        com = 'g++ ' + file + ' -o main' ;
        comm = './main <' + str(index) + '.in'
        os.system(com)
        ret = os.popen(comm).read()
        print(ret)
    else:
        Out = str(p[i])
        Out = Out.replace('<pre>','').replace('</pre>','')
        Out = Out.replace('&gt;','>')
        Out = Out.replace('&lt;','<')
        Out = Out.replace('&quot;','"')
        Out = Out.replace('&amp;','&')
        Out = Out.replace('<br />','\n')
        Out = Out.replace('<br/>','\n')
        Out = Out.replace('</ br>','\n')
        Out = Out.replace('<br>','\n')
        Out = Out.split('\n')
        ans = ''
        print('Answer:')
        for j in Out:
            y = j.replace('\n' , '')
            if(y != '' and y != ' '):
                ans = ans + y + '\n'
        print(ans)
        print('Verdict:')
        if (ret == ans):
            print(CRED1 + 'ACCEPTED' + CEND)
        else:
            print(CRED2 + 'WRONG ANSWER' + CEND)
        print('')
        index = index + 1