# Use this to check if any wallet was already used in blockchain
# Return Wallets already used.
# Use a list generated with vanitygen

import urllib

def loadWords(wallet_list="C:\Users\Felipe\Desktop\\bitcoin\\teste2.txt"):
    """
    Returns a list of valid wallets.
    """
    print "Loading wallet list from file..."
    # inFile: file
    inFile = open(wallet_list, 'r', 0)
    # wordList: list of strings
    wordList = []
    for line in inFile:
        #print line
        if 'Address: ' in line:
            wordList.append((line.strip('Address: ')).rstrip())
    print "  ", len(wordList), "words loaded."
    return wordList

def pp(w_list):
    sites = []
    for wallet in w_list:
        a = urllib.urlopen('https://blockchain.info/pt/address/' + wallet)
        print wallet
        b = 'falha'
        for i in xrange(0, 102):
            if i == 101:
                b = a.readline()
            a.readline()
        print b
        try:
            c =  b[44]
        except IndexError:
            pass
        print c
        if c != '0':
            sites.append(a.geturl())
    return sites
