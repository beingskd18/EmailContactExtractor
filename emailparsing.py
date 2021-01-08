import re
import email
import os
import itertools
import sys

#first argument shall be path of the directory containing mail files and the second argument shall be path of text file for storing info
path = sys.argv
listing = os.listdir(path[1])
parsedFile = open(path[2],"w")

for fle in listing:
    if str.lower(fle[-3:])=="eml":
        msg = email.message_from_file(open("g:\\inbox\\"+fle))
        print("Searching from file : "+str(fle))
        mailList = re.findall("E-mail:\s.+[@].+",msg.as_string())
        nameList = re.findall("Name:\s[a-zA-Z ]+",msg.as_string())
        numList = re.findall("Phone:\s\d+",msg.as_string())
        rep = ""
        for (i,j,k) in itertools.zip_longest(mailList,nameList,numList):
            if(str(i)+str(j)+str(k)!=rep):
                parsedFile.write("\n")
                parsedFile.write((str(i))[7:])
                parsedFile.write(",")
                parsedFile.write((str(j))[6:])
                parsedFile.write(",")
                parsedFile.write((str(k))[7:])
                rep = str(i)+str(j)+str(k)
parsedFile.close()
            
