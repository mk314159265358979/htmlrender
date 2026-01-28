import sys,re
from langdetect import detect
from deep_translator import GoogleTranslator

regexy=[r'\d{3}[- ]?\d{3}[- ]?\d{3}',r'\S*@\S*\.\S*',
r'[A-ZĆŁŃŚŻŹ][a-zążźćęóńł]+ [A-ZĆŁŃŚŻŹ][a-zążźćęóńł]+',
r'\d+[.,]\d{2}zł',r'\d{2}[.-]\d{2}[.-]\d{4}',
r'\d{2}[- ]?\d{4}[- ]?\d{4}[- ]?\d{4}[- ]?\d{4}[- ]?\d{4}[- ]?\d{4}']
nazwy=["NUMER TELEFONU","MAIL","OSOBA","KWOTA","DATA","NUMER KONTA"]

def anon(t):
 l=detect(t)
 for i,w in enumerate(regexy):
  n=GoogleTranslator(source='pl',target=l).translate(nazwy[i])
  m={};c=0
  def z(x):
   nonlocal c
   k=re.sub('[- ]','',x.group(0))
   if k not in m:m[k]=f"{n}{c}";c+=1
   return m[k]
  t=re.sub(w,z,t)
 return t

sys.stdout.write(anon(sys.stdin.read()))