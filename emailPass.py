# -*- coding: utf-8 -*-
import webbrowser
import urllib.request
import re
import platform
import os,sys
import random
import string
import argparse

if __name__ == "__main__":
    parse = argparse.ArgumentParser()
    parse.add_argument("email", help ="email do alvo")
    
    args = parse.parse_args()
 
so = platform.system()
     
if  so == 'Windows':
    os.system("cls")
        
else:
   os.system("clear")
     
txtFile = 'D:\\log.txt'
fileOpen = open(txtFile, 'w')
    
fileOpen.write('''
       [+]Tool developed by Pedro[+]          
[+]Updated to Python 3 by Douglas Chalegre[+] 
           [+]Update: 27/03/2018[+]            
              [+]Attack Email[+]               

\n''')
   
     
fileOpen.write("Email: %s\n" % args.email)
f = urllib.request.urlopen("https://br.search.yahoo.com/search?p=pastebin.com+%s&fr=yfp-t-707" % args.email)
a = f.read().decode('utf-8')
resultados = re.findall(r"https://pastebin.com/[\w1]+[\w2]", a)
     

    
        
for line in resultados:
   fileOpen.write("Possivel senha em -> %s\n" % line)
        
fileOpen.close()
