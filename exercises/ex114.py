#ex114
#Crie um código em Python que teste se o site Pudim está acessível pelo computador usado.
import requests

def check_conection(url):
    try:
        response = requests.get(url)   
        if response.status_code == 200:
            return True
        return False
    except:
        return False

resp = check_conection('https://www.pudim.com.br')
print(resp)

