import re
regexy = [r'\d{3}[- ]?\d{3}[- ]?\d{3}', r'\S*@\S*\.\S*', r'[A-ZĆŁŃŚŻŹ][a-zążźćęóńł]+ [A-ZĆŁŃŚŻŹ][a-zążźćęóńł]+', r'\d+[.,]\d{2}zł', r'\d{2}[.-]\d{2}[.-]\d{4}', r'\d{2}[- ]?\d{4}[- ]?\d{4}[- ]?\d{4}[- ]?\d{4}[- ]?\d{4}[- ]?\d{4}']
nazwy = ["NRTELEFONU", "MAIL", "OSOBA", "KWOTA", "DATA", "NRKONTA"]
def anonimizacja(text, r=regexy, n=nazwy):
    for i in range(len(r)):
        wzorzec = r[i]
        nazwa = n[i]
        tnr = {}
        i = 0  
        def zamien(nr):
            nonlocal i
            nr=re.sub("[- ]","",nr)
            if nr not in tnr:
                tnr[nr] = nazwa + f"{i}"
                i+=1
            return tnr[nr]
        text = re.sub(wzorzec, lambda m: zamien(m.group(0)), text)   
    return text

print("ALA ma kota")

