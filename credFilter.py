import re
import csv

#Get The file to read in
filename=input("What is the name of the file? ")

#convert the file into a dict so we can iterate through it, also remove all end of line characters if they exist
dictofAccounts = {}
dictofResults = {}
with open(filename,"r") as openFile:
    for line in openFile:
        (key,val) = line.rstrip("\n").split(":")
        dictofAccounts[str(key)]=val

#iterate through the dict
for keyinDict in dictofAccounts:
    #Get value from the key
    valueinDict=dictofAccounts.get(keyinDict, "none")
    #search for passwords that match our password policy
    if re.search(r'(?=.*\d)(?=.*[a-z])(?=.*[A-Z])(.{8,24})',valueinDict):
       #Add matching passwords and emails to the results dict
       dictofResults[keyinDict]=valueinDict

#Exit if there are no results
if bool(dictofResults)==False:
    print('Scanned', len(dictofAccounts.keys()), 'accounts and found no probable passwords')
    exit()
    
#Output results to a file, provided that there are results
if bool(dictofResults)==True:
    w = csv.writer(open("probableAccounts.csv", "w"))
    for key, val in dictofResults.items():
        w.writerow([key,val])
    print('Scanned', len(dictofAccounts.keys()),'accounts and found',len(dictofResults.keys()), 'probable passwords.')
    print('Results are located in probableAccounts.csv')
    exit()
