import os
from helper import Helper

class Main:

    def __init__(self):

        myip     = Helper.myip()
        ipinrepo = Helper.ipinrepo()

        os.system('clear')
        print('''
        --------------------------------------------------
        --==        Iniciar atualização de IP         ==--
        --------------------------------------------------
        ''')

        os.system('''
                echo \n
                cd /Users/lucasaraujo/Development/Azure_Automation/
                echo \n
                git fetch --all
                git reset --hard origin/master
                git pull
                \n
            ''')

        print(f'-----------------------------------------')
        print(f'IP Externo atual  ----> {myip}')
        print(f'IP no repositorio ----> {ipinrepo}')
        print(f'-----------------------------------------')

        if myip != ipinrepo.strip('\n'):


            print(f'\n Atualizar arquivo ....... \n')

            Helper.attip()

            os.system('''
                echo \n
                cd /Users/lucasaraujo/Development/Azure_Automation/
                git add DEV/users_access_restrictions_apps.txt
                git commit -m "add new ip"
                git push origin master
            ''')

            print(f'\n IP Atualizado no repositório: {Helper.myip()}')
            print('--------------------------------------------------')
        
        else:
            print('\n IPs iguais atualização não executado ... \n')


if __name__ == "__main__":
    Main()
