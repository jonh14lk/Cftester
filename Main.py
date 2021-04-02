import subprocess
import os
import sys
import json
from termcolor import colored
from bs4 import BeautifulSoup
from urllib.request import Request
from urllib.request import urlopen
from os.path import expanduser

home = expanduser('~')
file = sys.argv[1]
code = sys.argv[2]
problem = sys.argv[3]

def main():
    url = 'http://www.codeforces.com/contest/' + code + '/problem/' + problem
    soup = BeautifulSoup(urlopen(Request(url)).read(), 'html.parser')
    p = soup.findAll('pre')

    with open('config.json') as f:
        jsonfile = json.load(f)
        folderPath = jsonfile['folderPath']
        testColor = jsonfile['testColor']
        acceptedColor = jsonfile['acceptedColor']
        waColor = jsonfile['waColor']
        outputColor = jsonfile['outputColor']
        answerColor = jsonfile['answerColor']
    
    ret = ''
    ans = ''
    q = len(p)
    index = 1

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
            f = open(folderPath + str(index) + '.in', 'w')
            for j in In:
                y = j.replace('\n', '')
                if(y != '' and y != ' '):
                    f.write(y + '\n')
            f.close()
            print(colored('Test ' + str(index), testColor))
            print()
            print(colored('Your Output:', outputColor))
            os.system('g++ ' + file + ' -o main')
            ret = os.popen('./main <' + str(index) + '.in').read()
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
            print(colored('Answer:', answerColor))
            for j in Out:
                y = j.replace('\n' , '')
                if(y != '' and y != ' '):
                    ans = ans + y + '\n'
            print(ans)
            print('Verdict:')
            if (ret == ans):
                print(colored('ACCEPTED', acceptedColor))
            else:
                print(colored('WRONG ANSWER', waColor))
            print()
            index = index + 1

main()
