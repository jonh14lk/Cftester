import os
import re
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

def process(s : str):
    pattern = r'<div[^>]*>'

    s = re.sub(pattern, '', s)
    s = s.replace('</div>', '\n')
    s = s.replace('<pre>','').replace('</pre>','')
    s = s.replace('&gt;','>')
    s = s.replace('&lt;','<')
    s = s.replace('&quot;','"')
    s = s.replace('&amp;','&')
    s = s.replace('<br />','\n')
    s = s.replace('<br/>','\n')
    s = s.replace('</ br>','\n')
    s = s.replace('</br>','\n')
    s = s.replace('<br>','\n')
    s = s.replace('< br>','\n')
    s = s.split('\n')

    return s

def main():
    with open('config.json') as f:
        jsonfile = json.load(f)
        folderPath = jsonfile['folderPath']
        testColor = jsonfile['testColor']
        acceptedColor = jsonfile['acceptedColor']
        waColor = jsonfile['waColor']
        outputColor = jsonfile['outputColor']
        answerColor = jsonfile['answerColor']
        isGym =  jsonfile['isGym']
    
    url = 'http://www.codeforces.com/contest/' + code + '/problem/' + problem

    if isGym:
         url = 'http://www.codeforces.com/gym/' + code + '/problem/' + problem

    soup = BeautifulSoup(urlopen(Request(url)).read(), 'html.parser')
    p = soup.findAll('pre')
    
    ret = ''
    ans = ''
    q = len(p)
    index = 1

    for i in range(q):
        if (i % 2 == 0):
            input = process(str(p[i]))
            f = open(folderPath + str(index) + '.in', 'w')
            for j in input:
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
            output = process(str(p[i]))
            print(colored('Answer:', answerColor))
            for j in output:
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
            ans = ''

main()
