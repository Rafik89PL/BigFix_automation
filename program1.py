#! C:\Python27

from barc import Client
from getpass import getpass
import csv
from urllib import urlencode
import code

relevance = '(name of it, (if exists client settings whose (name of it contains "C_Code") of it and exists value of ' \
            'client setting whose (name of it contains "C_Code") of it then value of client setting whose (name of it ' \
            'contains "C_Code") of it else "N/A")) of bes computers '


def get_credentials():
    username = raw_input("Podaj usera: ").rstrip()
    passwd = getpass('Podaj haslo dla {}: '.format(username))
    return username, passwd


def get_bfservers():
    f = open('serverlist.csv', 'r')
    rows = csv.DictReader(f, delimiter=',', quotechar='\n')
    return rows


def run_relevance(c):
    res = c.post('/query', urlencode({'relevance': relevance}))
    print("Relevance result for {} server:".format(server_hostname))
    if res[0].Error == None:
        return res
    elif res[0] != None:
        print(res[0].Error)


if __name__ == "__main__":
    cred = get_credentials()
    # print (cred[0], cred[1])
    bfservers = get_bfservers()
    for elem in bfservers:
        server_ip = elem['IP']
        server_hostname = elem['Hostname']
        c = Client(server_ip, 52311, cred[0], cred[1])
        c.login()
        res = run_relevance(c)
        # print(res[0].Result)
        # sites = c.get('/sites')
        # print('Na serwerze {} jest {} siteow.'.format(server_hostname, len(sites)))
        #code.interact(local=dict(globals(), **locals()))
        for elem in res[0].Result:
            print(' | '.join(elem))