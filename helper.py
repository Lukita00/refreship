from bs4 import BeautifulSoup 
import requests
import setup

AZURE_AUTOMATION = setup.AZURE_AUTOMATION + '/DEV/users_access_restrictions_apps.txt'
NOME             = setup.NOME

class Helper(object):

    def __init__(self) -> None:pass

    def myip():
        url  = 'http://www.meuip.com.br'
        data = requests.get(url)
        data = BeautifulSoup(data.content,'html5lib')
        rest = data.find_all('h3',{'class':'m-0 font-weight-bold'})
        rest = rest[0].text
        rest = rest[8:].strip(' ')
        return rest

    def attip():
        arquivo  = open(AZURE_AUTOMATION,'r')
        conteudo = arquivo.readlines()
        arquivo.close()
        i = 0
        for linha in conteudo:
            nome = linha.split('=')[0]
            if nome == f'Allow{NOME}':
                novaLinha   =  nome+ '=' + Helper.myip() + '\n'
                conteudo[i] = novaLinha
            i += 1
        
        arquivo = open(AZURE_AUTOMATION,'w')
        arquivo.writelines(conteudo)
        arquivo.close()

    def ipinrepo():
        arquivo  = open(AZURE_AUTOMATION,'r')
        conteudo = arquivo.readlines()
        arquivo.close()
        for linha in conteudo:
            nome,ip = linha.split('=')
            if nome == f'Allow{NOME}':
                return ip.strip(' ').strip('''
                ''')

        
                

if __name__ == "__main__":
    print(Helper.myip())
    print(Helper.ipinrepo())
    # Helper.attip()