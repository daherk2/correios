# -*- coding: utf-8 -*-
import urllib2 as l2
import re
import sys

def encomenda(listado):
    var = []
    var = str(listado).split(' ')
    for lista in var:
        content = []
        address = 'http://websro.correios.com.br/sro_bin/txect01$.QueryList?P_ITEMCODE=&P_LINGUA=001&P_TESTE=&P_TIPO=001&P_COD_UNI='
        url = l2.urlopen(str(address) + str(lista))
        for line in url.readlines():
            content.append(line.decode('iso-8859-1').encode('utf-8'))
            
                
        content = [ elem.rstrip() for elem in content if 'rowspan' in elem ]
       
        if len(content) == 0:
            print('Encomenda {0} não foi encontrada'.format(lista))
        else:
            print('\n\nHistórico do objeto: {0}\n'.format(lista))
            for data in content:
                [(dia, local, sit)] = re.findall('<tr><td rowspan.+>(.*)</td><td>(.*)</td><td><FONT.*>(.*)</font>.*', data)
                dia = " ".join(dia.split())
                local = " ".join(local.split())
                sit = " ".join(sit.split())
                
                print('Data: {0}'.format(dia))
                print('Local: {0}'.format(local))
                print('Situação: {0}'.format(sit))
                print(' ')
def main():
    var = raw_input("Insira os codigos com espaço. Exemplo : XXXXXXXXXXXXX XXXXXXXXXXXXX : ")
    encomenda(var)
  
if __name__ == '__main__':
    main()

