#! C:\Python27

from barc import Client
from getpass import getpass
import csv
import code
def get_credentials():
    username = raw_input("Podaj usera: ").rstrip()
    passwd = getpass('Podaj haslo dla {}: '.format(username))
    return username, passwd

def get_bfservers():
    f = open('serverlist.csv', 'r')
    rows = csv.DictReader(f, delimiter=',', quotechar='\n')
    return rows

if __name__ == "__main__":
    cred = get_credentials()
    #print (cred[0], cred[1])
    bfservers = get_bfservers()
    for elem in bfservers:
            server_ip = elem['IP']
            server_hostname = elem['Hostname']
            c =  Client(server_ip, 52311, cred[0], cred[1])
            c.login()
            sites = c.get('/sites')
            print('Na serwerze {} jest {}'.format(server_hostname), len(sites))