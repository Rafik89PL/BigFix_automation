#! C:\Python27

from barc import Client
from getpass import getpass
import csv
import code
def get_credentials():
    username = raw_input("Podaj usera: ").rstrip()
    passwd = getpass('Podaj haslo dla {}: '.format(username))
    passwd = '!w4eKuvW55e7hCIw'
    return username, passwd

def get_bfservers():
    with open('serverlist.csv', 'r') as f:
        rows = csv.DictReader(f, delimiter=',', quotechar='\n')
    return rows
if __name__ == "__main__":
    cred = get_credentials()
    print (cred[0], cred[1])
    bfservers = get_bfservers()
    print (bfservers)
    code.interact(local=dict(globals(), **locals()))