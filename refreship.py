import os
import platform
import setup
from helper import Helper

AZURE_AUTOMATION = setup.AZURE_AUTOMATION
class Main:

    def __init__(self):

        myip     = Helper.myip()
        ipinrepo = Helper.ipinrepo()

        if platform.system() == 'Windows':
            os.system('cls')
        else:
            os.system('clear')
            
        print('''
--------------------------------------------------
--==        Iniciar atualização de IP         ==--
--------------------------------------------------
        ''')

        os.system(f'''
                cd {AZURE_AUTOMATION}
                git fetch --all
                git reset --hard origin/master
                git pull
            ''')

        print('-----------------------------------------')
        print(f'IP Externo atual  ----> {myip}')
        print(f'IP no repositorio ----> {ipinrepo}')
        print('-----------------------------------------')

        if myip != ipinrepo.strip('\n'):
            print('\n Atualizar arquivo ....... \n')

            Helper.attip()

            os.system(f'''
                cd {AZURE_AUTOMATION}
                git add DEV/users_access_restrictions_apps.txt
                git commit -m "Atualização de IP"
                git push origin master
            ''')

            print(f'\nIP Atualizado no repositório: {Helper.myip()}')
            print('-----------------------------------------')
        
        else:
            print('\nIPs iguais, atualização não executada ...')


if __name__ == "__main__":
    Main()
