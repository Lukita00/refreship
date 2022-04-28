from bs4 import BeautifulSoup 
import requests
import setup

AUTOMATION_PATH = setup.AUTOMATION_PATH

class Helper(object):

    def __init__(self) -> None:pass

    def myip():
        url = 'http://www.meuip.com.br'
        data = requests.get(url)
        data = BeautifulSoup(data.content,'html5lib')
        rest = data.find_all('h3',{'class':'m-0 font-weight-bold'})
        rest = rest[0].text
        rest = rest[8:].strip(' ')
        return rest

    def attip():
        arquivo = open(AUTOMATION_PATH,'r')
        conteudo = arquivo.readlines()
        arquivo.close()
        i = 0
        for linha in conteudo:
            if linha[0:10] == 'AllowLucas':
                novaLinha =  linha[0:11] + Helper.myip() + '\n'
                conteudo[i] = novaLinha
            i += 1
        
        arquivo = open(AUTOMATION_PATH,'w')
        arquivo.writelines(conteudo)
        arquivo.close()

    def ipinrepo():
        arquivo = open(AUTOMATION_PATH,'r')
        conteudo = arquivo.readlines()
        arquivo.close()
        for linha in conteudo:
            if linha[0:10] == 'AllowLucas':
                return linha[11:].strip(' ').strip('''
                ''')

        
                

if __name__ == "__main__":
    print(Helper.myip())
    print(Helper.ipinrepo())
    # Helper.attip()